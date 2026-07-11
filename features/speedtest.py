import speedtest
from engine.speak import speak

def check_internet_speed():
    try:
        speak("Checking your internet speed. Please wait.")

        st = speedtest.Speedtest()

        download_speed = st.download() / 1_000_000
        upload_speed = st.upload() / 1_000_000
        ping = st.results.ping

        result = (
            f"Download speed is {download_speed:.2f} megabits per second. "
            f"Upload speed is {upload_speed:.2f} megabits per second. "
            f"Ping is {ping:.0f} milliseconds."
        )

        print(result)
        speak(result)

    except Exception as e:
        print("Speedtest error:", e)
        speak("Sorry, I could not check the internet speed.")