# file: music.py
import webbrowser
from engine.speak import speak

# ---------------- Helper function ---------------- #
def play_youtube_top_song(query):
    """
    Simply open YouTube search for the query.
    No scraping, no extra output.
    """
    speak(f"Playing top result for {query}")
    search_url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
    
    # Open YouTube search page directly (user can play top song manually)
    webbrowser.open(search_url)


# ---------------- Music Category Functions ---------------- #
def play_happy():
    play_youtube_top_song("happy bollywood songs")

def play_sad():
    play_youtube_top_song("sad bollywood songs")

def play_motivational():
    play_youtube_top_song("motivational songs")

def play_romantic():
    play_youtube_top_song("romantic songs")

def play_khandeshi():
    play_youtube_top_song("khandeshi songs")

def play_marathi():
    play_youtube_top_song("marathi songs")
def play_custom_song(song_name):
    """
    Play any custom song on YouTube by name.
    """
    if not song_name:
        speak("Please provide a song name to play.")
        return

    speak(f"Playing {song_name}")
    search_query = song_name.replace(" ", "+")
    url = f"https://www.youtube.com/results?search_query={search_query}"

    # Open YouTube search page (user can click top video)
    webbrowser.open(url)