import socket
import json
import requests

url = 'http://feedthisdragon4.chall.malicecyber.com/api/v1'
session = '3baeca52-8433-4fc6-b6c4-21b27803d7c6'

# Création d'une socket pour capturer le trafic réseau

sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)

while True:
try:
packet, _ = sock.recvfrom(1000000)  # Recevoir le paquet
packet_data = packet.decode('utf-8', errors='ignore')
	if 'GET' in packet_data:
		continue
	if 'HTTP' in packet_data and '"items":' in  packet_data:

		#print("HTTP Packet captured:------------------", packet_data)

		body = packet_data.split('\\r\\n\\r\\n', 1)[1]

		if(body[-2] != '}'):
			continue

		#print(json_string)


		data = json.loads(body)
		#print(data)

		items = data.get('items')
		#print(items)

		if(len(items) != 0):
			for item in items:
				if(item['type'] != 'trap' and item['type'] != 'fox'):
					headers = {
						'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0',
						'Accept': '*/*',
						'Accept-Language': 'en-US,en;q=0.5',
						'Accept-Encoding': 'gzip, deflate',
						'Referer': '<http://feedthisdragon4.chall.malicecyber.com/>',
						'Authorization': 'mynotsosecrettoken',
						'Session': session,
						'Update': 'true',
						'ItemUuid': item['uuid'],
						'Content-Type': 'application/json',
						'Origin': '<http://feedthisdragon4.chall.malicecyber.com>',
						'Connection': 'close',
						'Cookie': session + '; achievements=%5B%7B%22slug%22%3A%22free%22%2C%22name%22%3A%22This%20One%20Is%20Free%22%2C%22description%22%3A%22No%20need%20for%20thanks%2C%20really.%22%2C%22delay%22%3A1700605929361%7D%5D',
						'Content-Length': '0'
					}
					requests.post(url, headers=headers)
except Exception as error:
	#continue
    	print("Error occurred:", error)

