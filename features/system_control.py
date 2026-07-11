import os
import ctypes
import psutil
import time
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import screen_brightness_control as sbc
from engine.speak import speak


# ===================== VOLUME CONTROL ===================== #

def _get_volume_interface():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_,
        CLSCTX_ALL,
        None
    )
    return cast(interface, POINTER(IAudioEndpointVolume))


def set_volume(level):
    try:
        level = int(level)

        if level < 0:
            level = 0
        if level > 100:
            level = 100

        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_,
            CLSCTX_ALL,
            None
        )

        volume = cast(interface, POINTER(IAudioEndpointVolume))

        # Convert 0-100 to 0.0-1.0
        volume.SetMasterVolumeLevelScalar(level / 100.0, None)

        speak(f"Volume set to {level} percent")

    except Exception as e:
        print("Volume error:", e)
        speak("Unable to change volume")


def increase_volume(step=10):
    volume = _get_volume_interface()
    current = volume.GetMasterVolumeLevelScalar() * 100
    set_volume(current + step)


def decrease_volume(step=10):
    volume = _get_volume_interface()
    current = volume.GetMasterVolumeLevelScalar() * 100
    set_volume(current - step)


def mute():
    volume = _get_volume_interface()
    volume.SetMute(1, None)
    speak("Volume muted")


def unmute():
    volume = _get_volume_interface()
    volume.SetMute(0, None)
    speak("Volume unmuted")


# ===================== BRIGHTNESS CONTROL ===================== #

def set_brightness(level):
    level = max(0, min(100, int(level)))
    sbc.set_brightness(level)
    speak(f"Brightness set to {level} percent")


# ===================== POWER CONTROL ===================== #

def lock_pc():
    speak("Locking your system")
    ctypes.windll.user32.LockWorkStation()


def sleep_pc():
    speak("Putting system to sleep")
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")


def shutdown_pc(confirm=False):
    if not confirm:
        speak("Confirmation required to shut down")
        return
    speak("Shutting down the system")
    os.system("shutdown /s /t 5")


def restart_pc(confirm=False):
    if not confirm:
        speak("Confirmation required to restart")
        return
    speak("Restarting the system")
    os.system("shutdown /r /t 5")