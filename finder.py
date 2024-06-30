import requests as req
from colorama import init as c_init,Fore
from pyfiglet import Figlet
from time import sleep
from os import system as console
from platform import system as os_name


c_init(autoreset=True)


os=os_name()

banner=Figlet(font="doom").renderText("ADMIN PANEL\nFINDER")


while True:
	print(Fore.CYAN+banner+(" "*40)+Fore.RED+"By MAMOSKO")
	print(Fore.YELLOW+"Type the site which you want to find the admin panel(URL): ",end="")
	URL=input()

	if not (URL.startswith("http://") or URL.startswith("https://")):
		print(Fore.RED+"Please type a valid URL")
		sleep(3)
		if os.lower()=="windows":console("cls")
		elif os.lower()=="linux" or os.lower()=="darwin":console("clear")
		else: print("What the "+Fore.RED+"f0*k"+Fore.RESET+" are you using OS?!")
		continue

	if not URL[-1]=="/":URL+="/"

	print(Fore.YELLOW+"Type world list file directory(for default: d): ",end="")
	wlist=input("")
	if wlist=="d":wlist="wordlist.txt"

	try:
		open(wlist,"r")
	except:
		print(Fore.RED+"Please type a valid directory")
		sleep(3)
		if os.lower()=="windows":console("cls")
		elif os.lower()=="linux" or os.lower()=="darwin":console("clear")
		else: print("What the "+Fore.RED+"f0*k"+Fore.RESET+" are you using OS?!")
		continue

	wordList=open(wlist,"r").read().split("\n")

	for word in wordList:
		try:
			if req.get(URL+word).status_code==200:print(f"{Fore.GREEN}{URL+word}[TRUE]")
			else:print(f"{URL+word}{Fore.RED}[FALSE]")
		except:
			print(f"{Fore.RED}{URL+word}[ERROR]")

	print(f"TESTED {Fore.GREEN}{len(wordList)}{Fore.RESET} URLs!")
	print("Press to any key...")
	if os.lower()=="windows":console("pause >nul")
	elif os.lower()=="linux" or os.lower()=="darwin":console("read -rsp -n 1 key")
	else: print("What the "+Fore.RED+"f0*k"+Fore.RESET+" are you using OS?!");sleep(5)

	
	if os.lower()=="windows":console("cls")
	elif os.lower()=="linux" or os.lower()=="darwin":console("clear")
	else: print("What the "+Fore.RED+"f0*k"+Fore.RESET+" are you using OS?!")