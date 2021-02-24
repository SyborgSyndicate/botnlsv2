import requests
import json
import os
import sys
import time
from sys import stdout
from time import sleep

try:
	import requests
except ImportError:
   print("\n [!] Silahkan install module requests")
   print("     ketik : pip2 install requests  ")
   sys.exit()

def gerak(kalimat):
    for shidqi in kalimat:
        stdout.write(shidqi)
        stdout.flush()
        sleep(0.1)
if __name__=='__main__':
     os.system("clear")
     gerak("\n[~] \33[1;31mThanks To my Friend ")
     time.sleep(0.5)
     gerak("\n[~] \33[1;37mGreetz : NORTH , xN5 , TriXploit , Wolf.ID , SyZyrus , Fardikhia , Dll\n")
     time.sleep(0.5)
     os.system("clear")

logo = '''\33[1;31m
   ___             _      _  _   
  | _ )    ___    | |_   | \| |  
  | _ \   / _ \   |  _|  | .` |  
  |___/   \___/   _\__|  |_|\_| \33[1;37m 
_|"""""|_|"""""|_|"""""|_|"""""|
"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-' 
\33[1;31m‹---------------------------------›
 \33[1;31mCoded by : Haz3ll & Friend
 \33[1;37mTeam     : SyborgSyndicate
 \33[1;31mWebsite  : https://syborgcate.com/
 \33[1;37mGithub   : https://github.com/SyborgSyndicate
 \33[1;31mBlog     : https://blog.syborgcate.com/
\33[1;37m‹---------------------------------›
''' 

print(logo)

def bek():
    inp = input("[•] \33[1;31mMasukan Teks :")
    time.sleep(2)
    print("[~] \33[1;37mini Hasilnya tod :")
    ajg = requests.get("http://salism3.pythonanywhere.com/nulis?text="+inp)
    for kntl in json.loads(ajg.content)["images"]:
        print(kntl)
        print("[!] \33[1;31mNote : Klik link untuk melihat gambar...")
        time.sleep(1)
        print("[!] \33[1;37mNote : Jika link tidak bisa di buka , copy link trus pastekan di browser lu...")
        print()
        time.sleep(1)
        balik = input("[?] \33[1;31mMau Lagi? (y/n) :")
        if balik == "y":
        	os.system("clear")
        	print(logo)
        	bek()
        elif balik == "n":
        	time.sleep(0.5)
        	print()
        	print("[~] \33[1;37mOkeh bye tod :)")
        	time.sleep(0.5)
        	sys.exit()
        	
       
bek()