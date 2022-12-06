# Python imports
import webview
import json
import sys
import os
import platform
import tkinter
import shutil
import screeninfo
import subprocess
import tkinter.messagebox
from pathlib import Path
from dotenv import load_dotenv

# Local imports
from internal.util import *
from internal.Enum import Enum
from internal import admin

# System variables
load_dotenv()
FROZEN = getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS')
COMPUTER_NAME = platform.node()
argv = sys.argv[1:]

# Ap variables
DEBUG = os.getenv("DEBUG", "false") == "true" and not FROZEN
IS_DEV = os.getenv("IS_DEV", "false") == "true" and not FROZEN
URL = get_path("./res/build") if not IS_DEV else "http://localhost:3000"
MANIFEST = json.loads(readcl(get_path("./res/public/manifest.json")))

# Use default settings if settings.json file is not found and if settings are missing, fill them in with the default
DEFAULT_SETTINGS = json.loads(readcl(get_path("./conf/default.json")))
SETTINGS_PATH = Path(get_path(DEFAULT_SETTINGS["config"]["appStorage"]), "settings.json")
SETTINGS = DEFAULT_SETTINGS | json.loads(readcl(SETTINGS_PATH)) if os.path.isfile(SETTINGS_PATH) else DEFAULT_SETTINGS

# Config vars
GTA_PATH = SETTINGS["gtav"]["paths"][SETTINGS["config"]["gtavpath"]]

# JS API
class API:
    def listDir(self, dir: os.PathLike, *args): 
        """List a directory's files"""
        path = dir
        # If the path is relative, make sure it starts in the res/src folder (since tsx files are only found here)
        if not pathlib.Path(path).is_absolute():
            path = pathlib.Path("./res/src", dir)
        return os.listdir(get_path(path))
    
    def launch(self, launch_type: Enum.LaunchType, do_launch: bool = True, *args):
        # Hide the main window (can't destroy iy or it will end the webview process and exit)
        WINDOW.hide()
        
        # Create the window and center it on the screen
        width, height = 500, 400
        monitor = list(filter(lambda monitor: monitor.is_primary, screeninfo.get_monitors()))[0]
        launch_window = webview.create_window(
            MANIFEST["name"],
            width=width,
            height=height,
            background_color="#000000",
            resizable=False,
            url=URL+"/launch",
            js_api=API(),
            frameless=True,
            easy_drag=True,
            transparent=False,
            x=int((monitor.width / 2) - (width / 2)),
            y=int((monitor.height / 2) - (height / 2)),
            confirm_close=True
        )
        
        # Exit if launch window closed
        launch_window.events.closed += lambda event: exit()
        
        modpack = json.loads(readcl(Path(GTA_PATH, "modpack.json")))
        
        if do_launch:
            # If the launch type is modded, move all files from the pseudo game folder to the game folder
            if launch_type == Enum.LaunchType.MODDED:
                files = os.listdir(get_path(SETTINGS["config"]["pseudoGameFolder"]))
                for curr, file in enumerate(files):
                    fp = Path(get_path(SETTINGS["config"]["pseudoGameFolder"]), file)
                    if os.path.isfile(fp) or os.path.exists(fp):
                        shutil.move(fp, GTA_PATH)
                        launch_window.evaluate_js(f"""window.globalThis.setProgress({curr / len(files) * 100})""")
                        
            # If the launch type is vanilla, move all mod files to the pseudo game folder
            elif launch_type == Enum.LaunchType.VANILLA:
                modpack_items = dict.items(modpack)
                for curr, [display_name, file] in enumerate(modpack_items):
                    if not str(display_name).startswith("$"):
                        fp = Path(get_path(SETTINGS["config"]["pseudoGameFolder"]), file)
                        if os.path.isfile(fp) or os.path.exists(fp):
                            shutil.move(fp, GTA_PATH)
                            launch_window.evaluate_js(f"""window.globalThis.setProgress({curr / len(modpack_items) * 100})""")
        
            # Open the Rockstar Launcher
            subprocess.Popen(Path(SETTINGS["gtav"]["launcher"]["path"], SETTINGS["gtav"]["launcher"]["filename"]))
            
            # Exit the program so it doesn't consume more resources
            exit()
        

# Create a root Tkinter window for showing errors and info windows (It may use more resources but it should'nt be significant)
ROOT = tkinter.Tk()

# Main window object
WINDOW = webview.create_window(
    MANIFEST["name"],
    width=1360,
    height=600,
    background_color="#000000",
    resizable=False,
    url=URL,
    js_api=API(),
)

WINDOW.events.closed += lambda event: exit()

# Starting function
def main():
    # If not running as admin, rerun as admin
    if not admin.isUserAdmin():
        admin.runAsAdmin()
    
    # Hide the Root Tkinter window
    ROOT.withdraw()
    
    # Check if the computer has a utf-8 character-set name (causes problems with the http server included with pywebview)
    computer_name_is_utf8 = True
    try:
        COMPUTER_NAME.encode("utf-8")
    except UnicodeError:
        computer_name_is_utf8 = False

    # Warn the user if the computer's name is not utf-8
    if not computer_name_is_utf8:
        tkinter.messagebox.showerror(MANIFEST["name"], f"Computer name '{COMPUTER_NAME}' contains non-UTF-8 characters, please change it and restart.")
        exit()
        
    # If there isn't a modpack.json file in the GTA V Folder, copy the default one
    if not os.path.isfile(Path(GTA_PATH, "modpack.json")):
        shutil.copy(get_path("./conf/modpack.json"), GTA_PATH)
    
    # If the app storage folder doesn't exist, create it
    if not os.path.exists(get_path(SETTINGS["config"]["appStorage"])):
        os.makedirs(get_path(SETTINGS["config"]["appStorage"]))
    
    # For each subfolder in the app dir, if it doesn't exist, create it
    for folder in ["Pseudo Game Folder", "Downloads", "Temp"]:
        fp = Path(get_path(SETTINGS["config"]["appStorage"]), folder)
        if not os.path.exists(fp):
            os.mkdir(fp)

    # Show reminder to always install mods in the mods folder
    tkinter.messagebox.showinfo(MANIFEST["name"], "REMINDER: When installing mods, in OpenIV, select \"Install in mods folder\". \n\nIf you add external files, make sure to add them to the modpack.json file in your GTA V Folder")
    
    # Start the webview process
    webview.start(debug=IS_DEV or DEBUG, http_server=not IS_DEV)

# Start the app
if __name__ == "__main__":
    main()