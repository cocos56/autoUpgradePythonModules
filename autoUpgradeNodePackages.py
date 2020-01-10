import subprocess
import os
from colorama import init, Fore
init(autoreset=True)

command = "npm -g outdated"

print('正在获取需要升级的包信息，请稍后...')
print()

outdatelist = subprocess.Popen (command, stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell = True).stdout.readlines()
updatelist = []

# print(outdatelist)
for i in outdatelist:
    i = str(i, encoding='utf-8')
    # print(i,end='')
    i = i[:i.find(' ')]
    updatelist.append(i)
    # print('\n', i, len(i))

updatelist = updatelist[1:]
# print(updatelist)

c = 1
total = len(updatelist)
if updatelist :
    for x in updatelist:
        if x == 'npm':
            print(Fore.RED + "检测到您需要更新npm，请至官网手动下载并安装。")
            os.system("start https://nodejs.org/en/download/current/")
            continue
        print('\n', c, '/', total, ' upgrading ', x, sep='')
        c += 1
        if x == 'cnpm': cmd = "npm install -g cnpm --registry=https://registry.npm.taobao.org"
        else: cmd = "cnpm -g install " + x
        # print(cmd)
        os.system(cmd)
    print("\n所有模块都已更新完毕！")
else :
    print("\n没有模块需要更新！")
print('\n请按回车键以退出程序。')
input()