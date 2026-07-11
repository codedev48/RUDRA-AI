# =========================================================
#                       IMPORTS
# =========================================================

import os
import datetime
from pandas import read_clipboard # type: ignore
import sys
import psutil
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QTimer

os.system("color 0A")

# ---------------- VOICE SYSTEM ---------------- #
from voice_system.voice_recognizer import identify_user

# ---------------- ENGINE ---------------- #
from engine.speak import speak
from engine.listen import listen_command
from engine.auto_type import auto_type
# from engine.wake_word import start_wake_word

# ---------------- BRAIN ---------------- #
from brain.multi_command import split_commands
from brain.smart_understanding import normalize_command
from brain.ai_brain import process_ai_query
from brain.fallback_genrator import generate_fallback
from brain.mini_ai import mini_ai_response

# ---------------- FEATURES ---------------- #
from features.daily_intelligence import daily_briefing
from features.introduction import rudra_introduction
from features.weather import get_weather
from features.system_control import *
from features.apps import *
from features.search import *
from features.system import *
from features.todo import *
from features.memory import *
from features.news import *
from features.report import *
from features.filesearch import *
from features.music import *
from features.summarize import *
from features.system_monitor import *
from features.game_quiz import play_quiz
from features.game_snake import play_snake
from features.game_rps import play_rps
from features.game_tictactoe import play_complex_maze
from features.process_manager import *
from features.gaming_mode import *
from features.modes import *
from features.transaction_logger import log_transaction, get_today_transactions
from features.hangman import hangman_game
from features.math_challenge import math_challenge
# from features.speedtest import check_internet_speed
from features.ip_address import get_ip_address
from features.internet_check import check_internet_connection
# from features.timer import start_timer
from features.alarm import set_alarm
from features.screenshot import take_screenshot
from features.system_info import get_system_info
from features.ai_memory import remember, recall
from features.clipboard_reader import read_clipboard

# =========================================================
#                       GUI SYSTEM
# =========================================================

import threading


class RudraApp(QMainWindow):
    HTML_CODE = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">

<style>

body{
background:#000;
display:flex;
justify-content:center;
align-items:center;
height:100vh;
margin:0;
overflow:hidden;
font-family:'Segoe UI',sans-serif;
color:#00f2ff;
}

.hud{
position:relative;
width:600px;
height:600px;
display:flex;
justify-content:center;
align-items:center;
}

/* OUTER RING */

.outer-ring{
position:absolute;
width:450px;
height:450px;
border-radius:50%;
border-top:2px solid #00f2ff;
border-bottom:2px solid #00f2ff;
box-shadow:0 0 25px #00f2ff;
}

/* INNER RING */

.inner-ring{
position:absolute;
width:300px;
height:300px;
border-radius:50%;
border:2px solid rgba(0,242,255,0.4);
}

/* CENTER */

.center{
width:80px;
height:80px;
border-radius:50%;
border:4px solid #00f2ff;
box-shadow:0 0 25px #00f2ff;
transition:all .4s ease;
}

/* CPU RAM */

.cpu{
position:absolute;
left:40px;
top:50%;
transform:translateY(-50%);
font-size:12px;
}

.ram{
position:absolute;
right:40px;
top:50%;
transform:translateY(-50%);
font-size:12px;
}

/* STATUS */

.status{
position:absolute;
bottom:60px;
font-size:12px;
letter-spacing:2px;
}

/* TIME */

.time{
position:absolute;
top:40px;
font-size:12px;
}

/* ROTATION */

@keyframes rotate{
from{transform:rotate(0deg);}
to{transform:rotate(360deg);}
}

/* LISTENING */

.listening .outer-ring{
animation:rotate 6s linear infinite;
}

.listening .center{
box-shadow:0 0 25px #00f2ff;
}

/* SPEAKING */

.speaking .outer-ring{
animation:none;
}

.speaking .center{
box-shadow:0 0 50px #00f2ff,0 0 90px #00f2ff;
}

/* THINKING */

.thinking .outer-ring{
animation:none;
}

.thinking .center{
box-shadow:0 0 40px #ff00ff;
}

</style>
</head>

<body>

<div class="hud listening" id="hud">

<div class="outer-ring"></div>
<div class="inner-ring"></div>

<div class="center"></div>

<div class="cpu" id="cpu">CPU: 0%</div>
<div class="ram" id="ram">RAM: 0%</div>

<div class="status" id="status">STATUS: LISTENING</div>

<div class="time" id="time"></div>

</div>

<script>

/* CLOCK */

setInterval(()=>{
let now=new Date();
document.getElementById("time").innerText=now.toLocaleTimeString();
},1000);

/* CPU RAM */

function updateStats(cpu,ram){
document.getElementById("cpu").innerText="CPU: "+cpu+"%";
document.getElementById("ram").innerText="RAM: "+ram+"%";
}

/* UI STATE */

function setUIState(state){

let hud=document.getElementById("hud");

hud.classList.remove("listening","speaking","thinking");

hud.classList.add(state);

document.getElementById("status").innerText=
"STATUS: "+state.toUpperCase();

}

</script>

</body>
</html>
"""

    def __init__(self):

        super().__init__()

        self.setWindowTitle("RUDRA AI")

        self.setFixedSize(800,700)

        self.browser = QWebEngineView()

        self.browser.setHtml(self.HTML_CODE)

        self.setCentralWidget(self.browser)

        # CPU RAM timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_stats)
        self.timer.start(1000)

    def update_stats(self):

        cpu = psutil.cpu_percent()
        ram = psutil.virtual_memory().percent

        self.browser.page().runJavaScript(
            f"updateStats({cpu},{ram});"
        )

    def set_state(self,state):

        self.browser.page().runJavaScript(
            f"setUIState('{state}');"
        )
# =========================================================
#                       GLOBALS
# =========================================================

CURRENT_USER = "Devendra"





# =========================================================
#                       GREETING
# =========================================================

def greet():

    try:
        start_monitoring()
    except:
        pass

    hour = datetime.datetime.now().hour

    if hour < 12:
        speak(f"Good Morning {CURRENT_USER}")
    elif hour < 18:
        speak(f"Good Afternoon {CURRENT_USER}")
    else:
        speak(f"Good Evening {CURRENT_USER}")

    speak("I am Rudra AI. How can I help you?")


# =========================================================
#                   COMMAND HANDLER
# =========================================================
def run_command(command):
    try:
        handle_command(command)
        return "Command executed successfully"
    except Exception as e:
        print("Error:", e)
        return "Sorry, I couldn't execute that command"
def handle_command(command):

    original_command = command.strip()
    normalized = normalize_command(original_command)

    print("Processing:", original_command)

    # ---------------- AI BRAIN ---------------- #
    if process_ai_query(original_command):
        log_transaction(original_command, "Success")
        return

    executed = False


    # =====================================================
    #                 TIME / DATE
    # =====================================================

    if "time" in original_command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}")
        executed = True

    elif "date" in original_command:
        today = datetime.datetime.now().strftime("%d %B %Y")
        speak(f"Today's date is {today}")
        executed = True

    elif "day" in original_command:
        today = datetime.datetime.now().strftime("%A")
        speak(f"Today is {today}")
        executed = True


    # =====================================================
    #                 MEMORY
    # =====================================================

    elif "remember" in command:
        remember(command)

    elif "what did i ask you to remember" in command or "when is" in command:
        recall(command)


    # =====================================================
    #                 TIMER / ALARM
    # =====================================================

    # elif "set timer" in command:

    #     import re
    #     numbers = re.findall(r'\d+', command)

    #     if numbers:
    #         seconds = int(numbers[0])
    #         start_timer(seconds)

    # elif "set alarm" in command:
    #     alarm_time = command.replace("set alarm", "").strip()
    #     set_alarm(alarm_time)


    # =====================================================
    #                 SYSTEM UTILITIES
    # =====================================================

    elif "take screenshot" in command:
        take_screenshot()

    elif "read clipboard" in command or "clipboard" in command:
        read_clipboard()

    elif "system info" in command or "system information" in command:
        get_system_info()

    # elif "internet speed" in command or "check speed" in command:
    #     check_internet_speed()
    #     executed = True

    elif "ip address" in command or "my ip" in command:
        get_ip_address()
        executed = True

    elif "check internet" in command or "internet connection" in command:
        check_internet_connection()
        executed = True


    # =====================================================
    #                 DAILY BRIEFING
    # =====================================================

    elif "daily briefing" in original_command or "daily intelligence" in original_command:
        daily_briefing(CURRENT_USER)
        executed = True


    # =====================================================
    #                 APPLICATIONS
    # =====================================================

    elif "open chrome" in original_command:
        open_chrome()
        executed = True

    elif "open youtube" in original_command:
        open_youtube()
        executed = True

    elif "open vscode" in original_command or "open visual studio" in original_command:
        open_vscode()
        executed = True
    
    elif "close youtube" in original_command:
        close_youtube()
        exexecuted = True

    # =====================================================
    #                 FILE SEARCH
    # =====================================================

    elif "find" in original_command:
        filename = original_command.replace("find file", "").strip()
        find_file(filename)
        executed = True


    # =====================================================
    #                 NEWS
    # =====================================================

    elif "global news" in original_command:
        get_news("global")
        executed = True

    elif "indian news" in original_command or "india news" in original_command:
        get_news("india")
        executed = True

    elif "news from" in original_command:
        state = original_command.replace("news from", "").strip()
        get_news(state)
        executed = True


    # =====================================================
    #                 GAMES
    # =====================================================

    elif "play hangman" in original_command:
        hangman_game()
        executed = True

    elif "play math challenge" in original_command:
        math_challenge()
        executed = True

    elif "play snake" in original_command:
        play_snake()
        executed = True

    elif "play quiz" in original_command:
        play_quiz(listen_command)
        executed = True

    elif "play rock paper scissors" in original_command:
        play_rps(listen_command)
        executed = True

    elif "play puzzle" in original_command:
        play_complex_maze()
        executed = True


    # =====================================================
    #                 SEARCH
    # =====================================================

    elif "search" in original_command:
        query = original_command.replace("search", "").strip()
        google_search(query)
        executed = True

    elif "wikipedia" in original_command:
        query = original_command.replace("wikipedia", "").strip()
        wikipedia_search(query)
        executed = True


    # =====================================================
    #                 REPORT
    # =====================================================

    elif "daily_report" in original_command:
        daily_report()
        executed = True


    # =====================================================
    #                 SYSTEM CONTROL
    # =====================================================

    elif "set volume to" in original_command:

        level = ''.join(filter(str.isdigit, original_command))

        if level:
            set_volume(int(level))
            executed = True
        else:
            speak("Please tell the volume level.")


    elif "set brightness" in original_command:

        level = ''.join(filter(str.isdigit, original_command))

        if level:
            set_brightness(int(level))
            executed = True
        else:
            speak("Please tell the brightness level.")


    elif "lock pc" in original_command:
        lock_pc()
        executed = True

    elif "shutdown" in original_command:
        shutdown_pc()
        executed = True

    elif "restart" in original_command:
        restart_pc()
        executed = True

    elif "list processes" in original_command:
        list_processes()
        executed=True
    # =====================================================
    #                 MUSIC
    # =====================================================

    elif "play happy songs" in original_command:
        play_happy()
        executed = True

    elif "play sad songs" in original_command:
        play_sad()
        executed = True

    elif "play motivational songs" in original_command:
        play_motivational()
        executed = True

    elif "play romantic songs" in original_command:
        play_romantic()
        executed = True

    elif "play khandeshi songs" in original_command:
        play_khandeshi()
        executed = True

    elif "play marathi songs" in original_command:
        play_marathi()
        executed = True

    # elif "play" in original_command:
    #     song_name = original_command.replace("play", "").strip()
    #     play_custom_song(song_name)
    #     executed = True


    # =====================================================
    #                 MONITORING
    # =====================================================

    elif "cpu usage" in original_command:
        cpu_usage()
        executed = True

    elif "ram usage" in original_command:
        ram_usage()
        executed = True

    elif "disk usage" in original_command:
        disk_usage()
        executed = True

    elif "battery" in original_command:
        battery_status()
        executed = True


    # =====================================================
    #                 PROCESS
    # =====================================================

    elif "show running processes" in original_command:
        list_processes()
        executed = True

    elif "kill process" in original_command:
        name = original_command.replace("kill process", "").strip()
        kill_process_by_name(name)
        executed = True


    # =====================================================
    #                 MODES
    # =====================================================

    elif "enable gaming mode" in original_command:
        enable_gaming_mode()
        executed = True

    elif "enable work mode" in original_command:
        enable_work_mode()
        executed = True

    elif "enable silent mode" in original_command:
        enable_silent_mode()
        executed = True

    elif "normal mode" in original_command:
        enable_normal_mode()
        executed = True


    # =====================================================
    #                 INTRODUCTION
    # =====================================================

    elif "who are you" in original_command or "introduce yourself" in original_command:
        rudra_introduction()
        executed = True


    # =====================================================
    #                 TRANSACTIONS
    # =====================================================

    elif "transaction" in original_command:

        transactions = get_today_transactions()

        if not transactions:
            speak("No transactions found for today")

        else:
            speak("Here are today's transactions")

            for t in transactions:
                speak(f"{t[1]} - {t[2]} - {t[3]}")

        executed = True


    # =====================================================
    #                 EXIT
    # =====================================================

    elif "exit" in original_command or "stop" in original_command:
        speak("Goodbye")
        log_transaction(original_command, "Success")
        exit()


    # =====================================================
    #                 MINI AI
    # =====================================================

    mini_reply = mini_ai_response(original_command)

    if mini_reply:
        speak(mini_reply)
        executed = True


    # =====================================================
    #                 FALLBACK
    # =====================================================

    if not executed:
        speak(generate_fallback(original_command))

    if executed:
        log_transaction(original_command, "Success")


# =========================================================
#                       MAIN LOOP
# =========================================================

def run_assistant():

    greet()

    while True:
        # gui.set_state("thinking")
        gui.set_state("listening")
        command = listen_command()

        if not command:
            continue

        command = command.lower()

        auto_type(command)

        commands = split_commands(command)

        for cmd in commands:
            gui.set_state("thinking")
            handle_command(cmd.strip())


# =========================================================
#                       ENTRY POINT
# =========================================================
if __name__ == "__main__":

    app = QApplication(sys.argv)

    gui = RudraApp()
    gui.show()

    assistant_thread = threading.Thread(target=run_assistant)
    assistant_thread.start()

    sys.exit(app.exec_())