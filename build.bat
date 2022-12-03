@echo on 

cd res
start /w npm run build

cd ..
py -3.8 -m PyInstaller ^
main.py ^
--onefile ^
--noconsole ^
--name "GTA V Modlib" ^
--add-data="./res/build;res/build" ^
--add-data="package.json;." ^
--add-data="./conf;conf" ^
--icon "./res/public/favicon.ico" ^
--uac-admin ^
