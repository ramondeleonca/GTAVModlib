import webview
import easygui
import platform
import os
import json
import configparser
import webbrowser
import subprocess
import sys
from dotenv import load_dotenv

load_dotenv()
FROZEN = getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS')
IS_DEV = os.getenv("IS_DEV", "false") == "true" and not FROZEN
DEBUG = os.getenv("DEBUG", "false") == "true" and not FROZEN
COMPUTER_NAME = platform.node()
URL = "res/build/index.html" if not IS_DEV else "http://localhost:3000"
MANIFEST = None
CONFIG = configparser.RawConfigParser()
CONFIG.read("conf/main.ini")

with open("res/build/manifest.json", "r") as manifest_json:
    MANIFEST = json.loads(manifest_json.read())
    manifest_json.close()

computer_name_is_utf8 = True
try:
    COMPUTER_NAME.encode("utf-8")
except UnicodeError:
    computer_name_is_utf8 = False

if not computer_name_is_utf8:
    easygui.msgbox(f"Computer name '{COMPUTER_NAME}' contains non-UTF-8 characters, please change it and restart.", "Non-UTF-8 Name")
    exit()

class API:
    def isOpenIVInstalled(self, *args):
        return os.path.exists(os.path.expandvars(CONFIG.get("PATHS", "openiv")))
    
    def openOpenIV(self, *args):
        if self.isOpenIVInstalled():
            popen = subprocess.Popen(os.path.join(os.path.expandvars(CONFIG.get("PATHS", "openiv")), "OpenIV.exe"), args)
            return popen.pid
        else:
            easygui.msgbox("OpenIV is not installed. Please install it at https://openiv.com", "OpenIV not installed")
            return None

    def open(self, url: str, *args):
        return webbrowser.open_new_tab(url)
    
    def getMods(self, *args):
        return []
        
WINDOW = webview.create_window(
    MANIFEST["name"],
    width=1360,
    height=600,
    background_color="#000000",
    resizable=False,
    url=URL,
    js_api=API()
)

webview.start(debug=IS_DEV or DEBUG, http_server=not IS_DEV)