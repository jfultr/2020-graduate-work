import requests

url = '127.0.0.1/cam_pic.php'
p = requests.get(url)
out = open("img.jpg", "wb")
out.write(p.content)
out.close()

