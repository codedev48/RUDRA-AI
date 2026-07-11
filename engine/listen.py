import sounddevice as sd
import soundfile as sf
import numpy as np
import os
import librosa
from scipy.spatial.distance import cosine
import speech_recognition as sr

VOICE_FOLDER = "voice_memory"
FS = 16000
DURATION = 5  # seconds

# ---------------- Voice Recording ----------------
def record_audio(duration=DURATION, fs=FS):
    """Record audio and return as numpy array"""
    print("Recording audio...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    return np.squeeze(audio)

def save_temp_audio(audio, filename="temp.wav", fs=FS):
    """Save temporary audio for processing"""
    sf.write(filename, audio, fs)

# ---------------- Voice Recognition ----------------
def extract_features(file_path):
    """Extract MFCC features from audio"""
    y, sr_ = librosa.load(file_path, sr=FS)
    mfcc = librosa.feature.mfcc(y=y, sr=sr_, n_mfcc=13)
    return np.mean(mfcc.T, axis=0)

def recognize_user(audio):
    """
    Compare recorded audio with all users in voice_memory
    Returns the best matched username or 'user' if no match
    """
    temp_file = "temp_user.wav"
    save_temp_audio(audio, temp_file)
    input_feat = extract_features(temp_file)

    if not os.path.exists(VOICE_FOLDER):
        return "user"

    users = [d for d in os.listdir(VOICE_FOLDER) if os.path.isdir(os.path.join(VOICE_FOLDER, d))]
    if not users:
        return "user"

    best_user = "user"
    best_score = 1.0  # cosine distance, lower is better

    for user in users:
        user_path = os.path.join(VOICE_FOLDER, user)
        user_files = [f for f in os.listdir(user_path) if f.endswith(".wav")]
        for f in user_files:
            feat = extract_features(os.path.join(user_path, f))
            score = cosine(input_feat, feat)
            if score < best_score:
                best_score = score
                best_user = user

    os.remove(temp_file)
    return best_user

# ---------------- Speech to Text ----------------
def listen_command():
    """Record audio and convert to text"""
    audio = record_audio(duration=DURATION)
    temp_file = "temp_command.wav"
    save_temp_audio(audio, temp_file)

    r = sr.Recognizer()
    try:
        with sr.AudioFile(temp_file) as source:
            audio_data = r.record(source)
            text = r.recognize_google(audio_data)
    except Exception as e:
        print("Could not understand audio:", e)
        text = ""

    os.remove(temp_file)
    return text
