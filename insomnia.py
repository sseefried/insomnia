#!/usr/bin/env python3
import os
import subprocess

script_dir = os.path.dirname(os.path.abspath(__file__))
try:
    msg="Turning off insomnia. Computer will now go to sleep as normal"
    pid = subprocess.check_output(["pgrep", "-f", "caf.py"]).decode("utf-8").strip()
    subprocess.Popen(["kill", pid])
    subprocess.Popen(["notify-send", msg])
    print(msg)
except:
    msg="Computer will now stay awake..."
    subprocess.Popen(["/bin/bash", "-c", script_dir+"/"+"caf.py"])
    subprocess.Popen(["notify-send", msg])
    print(msg)
