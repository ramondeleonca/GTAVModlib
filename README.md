<p align="center">
    <img src="./res/public/logo.png" alt="GTA V Modlib Logo" width="200"/>
</p>

![App size](https://img.shields.io/github/size/ramondeleonca/GTAVModlib/dist/GTA%20V%20Modlib.exe?style=for-the-badge)
![Downloads](https://img.shields.io/github/downloads/ramondeleonca/GTAVModlib/total?style=for-the-badge)
![Issues](https://img.shields.io/github/issues/ramondeleonca/GTAVModlib?style=for-the-badge)
![Pull Requests](https://img.shields.io/github/issues-pr/ramondeleonca/GTAVModlib?style=for-the-badge)
![License](https://img.shields.io/github/license/ramondeleonca/GTAVModlib?style=for-the-badge)
![Version](https://img.shields.io/github/package-json/v/ramondeleonca/GTAVModlib?style=for-the-badge)

#### THIS IS A WORK-IN-PROGRESS!
#### Currently only supports Epic games Version

# GTA V Modlib
GTA V Modlib is a program that allows you to import, install and manage your GTA V mods all while being lightweight and easy to use.

## How it works
Upon opening **GTA V Modlib.exe** up, you'll b met with this UI resembling the Rockstar Launcher:
![GTA V Modlib Home Screen Screenshot](./res/public/GTA_V_Modlib_Home.png)
In the bottom left you'll be prompted to download mods from [gta5-mods.com](https://gta5-mods.com) and install them in GTA V Modlib

In the middle, you'll see two buttons: Launch Modded & Launch Vanilla. It's as easy as clicking one of those two buttons to switch between modded and vanilla GTA V in a matter of seconds<sup>[1](#disclaimers)</sup>

In the left panel you can also switch mods on and off individually.

## Contributing and technologies
GTA V Modlib is built with **TypeScript** and **Python**: TypeScript is used in conjunction with **React** to create the front-end render build and python is used to put everything inside a nice window with **pywebview** and interfafce with the system with **easygui** and native Python APIs.

If you have knowledge in **React**, **Typescript** or **Python** feel free to modify and submit a pull request, help is always welcome!

## Building and Development Server
Before building make sure you have both installed:
- Python 3.8.0
- Node JS v18 or later

Then, in the **root folder** run 

```sh
npm i
```
To install the dev dependencies; afer, navigate to the **res folder** and run

```sh
npm i
```
Once again to install the dependencies for the render process, lastly, in the **root folder** run 
```sh
py -3.8 -m pip install -r requirements.txt
```
To install Python's requirements.

To start the development server, in the root folder run 
```sh
npm run dev
```
It will start the react dev server and run the app with the dev server URL.

To build the app run 
```sh
npm run build
```
And your built exe file will be in the **dist folder**

#### Disclaimers
1. Depending on the speed of your storage device