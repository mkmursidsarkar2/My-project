a ="\033[0m"       # Text Reset
bred="\033[1;31m"         # Red
bgreen="\033[1;32m"       # Green
bblue="\033[1;34m"        # Blue
bcyan="\033[1;36m" 

import os 
import time 
os.system("clear")
time.sleep(7)
#time.sleep(0.1)
os.system('termux-open https://github.com/')

baner = (f"""{bblue}=======================================
{bgreen}[+]AUTHOR       :     Md Mursid Sarkar
[+]Facebook     :     Md Mursid Sarkar
[+]gitub        :                                    
[+]Tools        :     Sms Bomber
{bblue}======================================="""+a)
#b = int(input(bgreen+'[>]Enter you Namber: '+bblue))
print(baner)

c = "Md Mursid Sarkar"
d = "Md Mursid"
e = input(bgreen+"[>]Enter you username: "+bblue)
if e== c:
    print(bcyan+"caret username")
    f = input(bgreen+"[>]Enter you password: "+bblue)
    
    if f == d:
        print(bcyan+'caret password')
        time.sleep(1)
        os.system('clear')
        print(baner)
        tool = (bgreen+" \n [1]wifi hack \n [2]phon hack \n [3]website hosting")
        print(tool)
        inpu=int(input("\n [>]Enter you Namber: "+bblue))
        if inpu==1:
          print('wifi hack')
        elif inpu==2:
          print('phon hack')
        elif inpu==3:
          print('website hosting')
        
        #for i in tool:
          #print(i)
    else:
        print(bred+'rong password')
else :
    print(bred+"rong username")
