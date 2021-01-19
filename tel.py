#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import requests
import json
import time
import urllib
import os

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   HEADER = '\033[95m'
   OKBLUE = '\033[94m'
   OKGREEN = '\033[92m'
   WARNING = '\033[93m'
   FAIL = '\033[91m'

class config:
	key = "3c742a205217b96571c24800e5d011e2" 
	       
def banner():
	os.system('clear')
	print( color.YELLOW + """
 ____  _____ ____  _   _    _    _  _______     __
| __ )| ____|  _ \| \ | |  / \  | |/ / _ \ \   / /
|  _ \|  _| | | | |  \| | / _ \ | ' / | | \ \ / /
| |_) | |___| |_| | |\  |/ ___ \| . \ |_| |\ V /
|____/|_____|____/|_| \_/_/   \_\_|\_\___/  \_/
	Version - dev-1.0                 
	""" + color.END)

def main():
	banner()
	if len(sys.argv) == 2:
		number = sys.argv[1]
		api = "http://apilayer.net/api/validate?access_key=" + config.key + "&number=" + number + "&country_code=&format=1"
		output = requests.get(api)
		content = output.text
		obj = json.loads(content)
		country_code = obj['country_code']
		country_name = obj['country_name']
		location = obj['location']
		carrier = obj['carrier']
		line_type = obj['line_type']

		print( color.YELLOW + "[+] " + color.END + "Сбор информации о номере телефона")
		print( "--------------------------------------")
		time.sleep(0.2)
 
		if country_code == "":
			print(" - Получение страны		[ " + color.RED + "FAILED " + color.END + "]")
		else:
			print(" - Получение страны		[ " + color.GREEN + "OK " + color.END + "]")

		time.sleep(0.2)
		if country_name == "":
			print(" - Получение названия страны		[ " + color.RED + "FAILED " + color.END + "]")
		else:
			print(" - Получение названия страны		[ " + color.GREEN + "OK " + color.END + "]")

		time.sleep(0.2)
		if location == "":
			print(" - Получение местоположения		[ " + color.RED + "FAILED " + color.END + "]")
		else:
			print( " - Получение местоположения		[ " + color.GREEN + "OK " + color.END + "]")

		time.sleep(0.2)
		if carrier == "":
			print(" - Получение провайдера		[ " + color.RED + "FAILED " + color.END + "]")
		else:
			print(" - Получение провайдера		[ " + color.GREEN + "OK " + color.END + "]")

		time.sleep(0.2)
		if line_type == None:
			print(" - Получение устройства		[ " + color.RED + "FAILED " + color.END + "]")
		else:
			print(" - Получение устройства		[ " + color.GREEN + "OK " + color.END + "]")

		
		print( color.YELLOW + "[+] " + color.END + "Вывод информации")
		print("--------------------------------------")
		print( " - Телефонный номер: " + str(number))
		print(" - Страна: " + str(country_code))
		print(" - Country Name: " + str(country_name))
		print( " - Расположение: " + str(location))
		print( " - провайдер: " + str(carrier))
		print(" - устройства: " + str(line_type))
	else:
		print("[?] Применение:")
		print("	python3 %s <phone-number>" % (sys.argv[0]))
		print( " \n Пример: \n python3 %s +13213707446" % (sys.argv[0]))

main()
