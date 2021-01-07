from requests import get
from os import getcwd
from os import path

username = input("Type the instagram username: ")
header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0"}
r = get("https://www.instagram.com/"+username+"/?__a=1", headers=header)
info = r.json()
photo_url = info["graphql"]["user"]["profile_pic_url_hd"]
photo = get(photo_url)

if r.status_code == 200:
	path = path.join(getcwd(), "ProfilePhotos", f"{username}.png")
	with open(path, 'wb') as handler:
		handler.write(photo.content)
		print('Profile photos downloaded!')
else:
	print(r.status_code)
