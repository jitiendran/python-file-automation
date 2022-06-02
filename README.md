# File Automation
Since I am very lazy this program is going to organize my files

## Depencencies
```
pip install watchdog
```
#

Since opening the terminal and running the python file is too much work. Let's create a bat file and add it to the startup folder (i.e) C:\Users\username\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup in your desktop

```
@echo off
python your file path\automate.py %*
pause
```
