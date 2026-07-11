import sys
import psutil
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QTimer


HTML_CODE = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<style>
body {
    background:#000; display:flex; justify-content:center; align-items:center;
    height:100vh; margin:0; font-family:'Segoe UI', sans-serif; color:#00f2ff; overflow:hidden;
}
.hud-container { position:relative; width:600px; height:600px; display:flex; justify-content:center; align-items:center; }
.title { position:absolute; top:20px; text-align:center; letter-spacing:3px; }
.title h1 { font-size:24px; margin:0 }
.title p { font-size:10px; margin:0; opacity:.8 }

.ring { position:absolute; border-radius:50%; border:1px solid rgba(0,242,255,.25); display:flex; justify-content:center; align-items:center; }

.outer-ring { 
width:450px; height:450px; 
border-top:2px solid #00f2ff; border-bottom:2px solid #00f2ff; 
animation:rotate 10s linear infinite; 
box-shadow:0 0 20px rgba(0,242,255,.4); 
}

.inner-waveform { 
width:280px; height:280px; 
border:4px double #ff00ff; 
box-shadow:0 0 15px rgba(255,0,255,.5); 
animation:pulse 2s ease-in-out infinite; 
}

.center-core { 
width:60px; height:60px; 
border:8px double #00f2ff; 
border-radius:50%; 
box-shadow:0 0 20px #00f2ff; 
transition:all .4s ease; 
}

.thinking-dots { position:absolute; display:flex; gap:6px; bottom:150px; opacity:0; }
.thinking-dots span { width:6px; height:6px; background:#00f2ff; border-radius:50%; animation:blink 1.4s infinite; }
.thinking-dots span:nth-child(2){animation-delay:.2s}
.thinking-dots span:nth-child(3){animation-delay:.4s}

.status-panel { position:absolute; bottom:80px; font-size:11px; display:flex; gap:25px; letter-spacing:1px; }

.data-label { position:absolute; font-size:12px; text-transform:uppercase; top:50%; }
.left { left:40px; } 
.right { right:40px; }

.listening .outer-ring { animation-play-state:running; }

.speaking .outer-ring { animation-play-state:paused; }
.speaking .center-core { box-shadow:0 0 40px #00f2ff, 0 0 60px #00f2ff; }

.thinking .outer-ring { animation-play-state:paused; }
.thinking .thinking-dots { opacity:1; }
.thinking .center-core { box-shadow:0 0 25px #ff00ff, 0 0 45px #ff00ff; }

@keyframes rotate { from{transform:rotate(0deg)} to{transform:rotate(360deg)} }
@keyframes pulse { 0%,100%{transform:scale(1);opacity:.8} 50%{transform:scale(1.05);opacity:1} }
@keyframes blink { 0%,80%,100%{opacity:.2} 40%{opacity:1} }

</style>
</head>

<body>

<div class="hud-container listening" id="hud">

<div class="title">
<h1>R.U.D.R.A</h1>
<p>Your Personal Voice Assistant</p>
</div>

<div class="ring outer-ring"></div>
<div class="ring inner-waveform"></div>
<div class="center-core"></div>

<div class="thinking-dots">
<span></span><span></span><span></span>
</div>

<div class="data-label left" id="cpu">CPU: 0%</div>
<div class="data-label right" id="ram">RAM: 0%</div>

<div class="status-panel">
<span id="time"></span>
<span id="date"></span>
<span id="status">STATUS: LISTENING</span>
</div>

</div>

<script>

const hud = document.getElementById("hud");
const statusText = document.getElementById("status");

function updateClock(){
const now = new Date();

document.getElementById("time").innerText =
"TIME: " + now.toLocaleTimeString();

document.getElementById("date").innerText =
"DATE: " + now.toLocaleDateString();
}

setInterval(updateClock,1000);


function updateStats(cpu,ram){

document.getElementById("cpu").innerText = "CPU: " + cpu + "%";
document.getElementById("ram").innerText = "RAM: " + ram + "%";

}


function setUIState(state){

hud.classList.remove("listening","speaking","thinking");

hud.classList.add(state);

statusText.innerText =
"STATUS: " + state.toUpperCase();

}

</script>

</body>
</html>
"""


class RudraApp(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("R.U.D.R.A - HUD")

        self.setFixedSize(800,700)

        self.browser = QWebEngineView()

        self.browser.setHtml(HTML_CODE)

        self.setCentralWidget(self.browser)

        # CPU RAM realtime timer
        self.stats_timer = QTimer()

        self.stats_timer.timeout.connect(self.update_system_info)

        self.stats_timer.start(1000)   # every 1 second


    def update_system_info(self):

        cpu = psutil.cpu_percent(interval=None)

        ram = psutil.virtual_memory().percent

        self.browser.page().runJavaScript(
            f"updateStats({cpu},{ram});"
        )


    def set_state(self,state):

        self.browser.page().runJavaScript(
            f"setUIState('{state}');"
        )


if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = RudraApp()

    window.show()

    sys.exit(app.exec_())