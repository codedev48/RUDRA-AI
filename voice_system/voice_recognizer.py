import os
import numpy as np
import librosa
import sounddevice as sd
from scipy.spatial.distance import cosine

VOICE_FOLDER = "voice_memory"
FS = 16000


def record_test_voice(duration=3):

    print("Speak now...")

    audio = sd.rec(int(duration * FS), samplerate=FS, channels=1)

    sd.wait()

    return np.squeeze(audio)


def extract_features(audio):

    mfcc = librosa.feature.mfcc(y=audio, sr=FS, n_mfcc=40)

    return np.mean(mfcc.T, axis=0)


def load_user_features(user_folder):

    features = []

    for file in os.listdir(user_folder):

        if file.endswith(".wav"):

            path = os.path.join(user_folder, file)

            audio, sr = librosa.load(path, sr=FS)

            features.append(extract_features(audio))

    return features


def identify_user():

    if not os.path.exists(VOICE_FOLDER):

        print("No registered users")

        return None

    test_audio = record_test_voice()

    test_features = extract_features(test_audio)

    best_user = None

    best_score = 0

    for user in os.listdir(VOICE_FOLDER):

        user_folder = os.path.join(VOICE_FOLDER, user)

        if not os.path.isdir(user_folder):
            continue

        registered_features = load_user_features(user_folder)

        similarities = []

        for feature in registered_features:

            similarity = 1 - cosine(feature, test_features)

            similarities.append(similarity)

        avg_similarity = np.mean(similarities)

        print(f"{user} similarity:", avg_similarity)

        if avg_similarity > best_score:

            best_score = avg_similarity

            best_user = user

    if best_score > 0.75:

        print(f"\nUser identified: {best_user}")

        return best_user

    else:

        print("\nUnknown voice")

        return None


if __name__ == "__main__":

    user = identify_user()

    if user:
        print("Access granted")
    else:
        print("Access denied")