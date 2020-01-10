@echo off
%1 mshta vbscript:CreateObject("Shell.Application").ShellExecute("cmd.exe","/c %~s0 ::","","runas",1)(window.close)&&exit
cd /d "%~dp0"

python -m pip install --upgrade pip

pip install -i https://pypi.doubanio.com/simple/ -r requirements.txt

pause