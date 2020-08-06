%1 mshta vbscript:CreateObject("Shell.Application").ShellExecute("cmd.exe","/c %~s0 ::","","runas",1)(window.close)&&exit
cd /d "%~dp0"

set /p name=请输入要安装的库名：

pip install %name% -i https://pypi.douban.com/simple/

pause