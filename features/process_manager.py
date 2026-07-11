import psutil
from engine.speak import speak


# ---------------- SHOW RUNNING PROCESSES ---------------- #

def list_processes():
    processes = []

    for proc in psutil.process_iter(['pid', 'name']):
        try:
            processes.append(proc.info['name'])
        except:
            pass

    unique_processes = list(set(processes))

    print("\nRunning Processes:\n")
    for p in unique_processes[:20]:  # show first 20
        print(p)

    speak("Showing running processes in console.")


# ---------------- KILL PROCESS ---------------- #

def kill_process_by_name(name):
    killed = False

    for proc in psutil.process_iter(['name']):
        try:
            if name.lower() in proc.info['name'].lower():
                proc.kill()
                killed = True
        except:
            pass

    if killed:
        speak(f"{name} has been closed")
    else:
        speak("Process not found")


# ---------------- TOP CPU PROCESS ---------------- #

def top_cpu_process():
    max_cpu = 0
    max_process = None

    for proc in psutil.process_iter(['name', 'cpu_percent']):
        try:
            cpu = proc.cpu_percent(interval=0.1)
            if cpu > max_cpu:
                max_cpu = cpu
                max_process = proc.info['name']
        except:
            pass

    if max_process:
        speak(f"{max_process} is using highest CPU at {max_cpu} percent")
    else:
        speak("Unable to detect top CPU process")


# ---------------- TOP RAM PROCESS ---------------- #

def top_ram_process():
    max_ram = 0
    max_process = None

    for proc in psutil.process_iter(['name', 'memory_info']):
        try:
            mem = proc.info['memory_info'].rss
            if mem > max_ram:
                max_ram = mem
                max_process = proc.info['name']
        except:
            pass

    if max_process:
        ram_mb = max_ram / (1024 * 1024)
        speak(f"{max_process} is using highest memory at {ram_mb:.2f} MB")
    else:
        speak("Unable to detect top memory process")