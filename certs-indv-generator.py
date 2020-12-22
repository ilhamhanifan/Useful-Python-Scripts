#!/usr/bin/python3
import pandas as pd
import csv
from PIL import Image, ImageDraw, ImageFont

#names = {"Muhammad Ilham Hanifan ZERO PUNCTUASDNn asd","Bari Rehatta Alfredo Sulistyo Wati","Farhan Al Fayyadh"}

file = open('/home/maki/dev/scripts/generate-certificate/webinar-ccug-1/jpeg/datas/Mhs.GETSertif.csv')
reader = csv.reader(file)
names = list(reader)
file.close()
print(type(names))

for i in names:
	name = i[0].split(' ')
	if len(name) > 3:
		tmp = ''
		for x in range(len(name)):
			if x <= 2:
				tmp += f"{name[x]} ".capitalize()		
			else:
				tmp += f"{str(name[x][0]).capitalize()}"

		name = ''.join(str(tmp))
	else:

		name = ' '.join(name).title()

	im = Image.open(r"/home/maki/dev/scripts/generate-certificate/webinar-ccug-1/jpeg/datas/peserta.png") #webinar-ccug-2020.png")
	#im = Image.new('RGB', ima.size(), (255, 255, 255))
	#im.paste(ima, mask=ima.split()[3])

	im = im.convert('RGB')

	d = ImageDraw.Draw(im)
	text_color = (255,255,255)
	font = ImageFont.truetype("/home/maki/dev/scripts/generate-certificate/webinar-ccug-1/jpeg/datas/IBMPlexMono-Bold.ttf",100)

	print(name)
	print(type(name))

	im_width = im.width
	text_width,_ = d.textsize(name,font=font)

	location = ((im_width-text_width)/2,450)
	print(location)
	d.text(location, name, fill=text_color, font = font)
	im.save("cert_" + name + ".jpeg")
