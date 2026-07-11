import os
import string
import nltk
import PyPDF2
from collections import defaultdict
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from engine.speak import speak


# Download required NLTK data (runs once)
nltk.download("punkt", quiet=True)
nltk.download("stopwords", quiet=True)


# ---------------- CORE SUMMARY ENGINE ---------------- #

def generate_summary(text, num_sentences=3):
    if not text or len(text.strip()) == 0:
        return "No content available for summarization."

    sentences = sent_tokenize(text)
    words = word_tokenize(text.lower())

    stop_words = set(stopwords.words("english"))
    word_frequencies = defaultdict(int)

    for word in words:
        if word not in stop_words and word not in string.punctuation:
            word_frequencies[word] += 1

    sentence_scores = defaultdict(int)

    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in word_frequencies:
                sentence_scores[sentence] += word_frequencies[word]

    if len(sentence_scores) == 0:
        return "Could not generate summary."

    summary_sentences = sorted(
        sentence_scores,
        key=sentence_scores.get,
        reverse=True
    )[:num_sentences]

    return " ".join(summary_sentences)


# ---------------- TEXT FILE SUMMARY ---------------- #

def summarize_text_file(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            text = file.read()

        summary = generate_summary(text)

        new_file = "summary_" + os.path.basename(filepath)

        with open(new_file, "w", encoding="utf-8") as file:
            file.write(summary)

        speak("Summary created successfully")
        print("Summary saved as:", new_file)

    except Exception as e:
        speak("Error summarizing the text file")
        print("Error:", e)


# ---------------- PDF SUMMARY ---------------- #

def summarize_pdf_file(filepath):
    try:
        reader = PyPDF2.PdfReader(filepath)
        text = ""

        for page in reader.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted

        summary = generate_summary(text)

        new_file = "summary_" + os.path.basename(filepath).replace(".pdf", ".txt")

        with open(new_file, "w", encoding="utf-8") as file:
            file.write(summary)

        speak("PDF summary created successfully")
        print("Summary saved as:", new_file)

    except Exception as e:
        speak("Error summarizing the PDF file")
        print("Error:", e)


# ---------------- FOLDER SEARCH + AUTO DETECT ---------------- #

def summarize_from_folder(filename):
    speak(f"Searching for {filename}")

    for root, dirs, files in os.walk("C:\\"):
        for file in files:
            if filename.lower() in file.lower():

                full_path = os.path.join(root, file)

                speak("File found. Generating summary.")

                if file.endswith(".pdf"):
                    summarize_pdf_file(full_path)
                elif file.endswith(".txt"):
                    summarize_text_file(full_path)
                else:
                    speak("File format not supported. Only TXT and PDF allowed.")
                return

    speak("File not found")