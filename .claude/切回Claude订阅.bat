@echo off
set PY=C:\Users\Administrator\AppData\Local\Programs\Python\Python311\python.exe
set CODE=C:\Users\Administrator\AppData\Local\Programs\Microsoft VS Code\Code.exe
set SW=C:\Users\Administrator\.claude\switch_model.py
set ASK=C:\Users\Administrator\.claude\auto_ask_model.py

echo.
echo Switching to Claude Pro...
"%PY%" "%SW%" claude
if errorlevel 1 ( echo FAILED & pause & exit /b )

echo Done. Closing VS Code...
timeout /t 1 /nobreak >/dev/null
taskkill /im Code.exe >/dev/null 2>&1
timeout /t 3 /nobreak >/dev/null

echo Restarting VS Code...
start "" "%CODE%"

start "" /B "%PY%" "%ASK%"
