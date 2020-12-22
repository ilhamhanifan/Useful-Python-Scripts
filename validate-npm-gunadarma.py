#!/usr/bin/python3
import requests
import time
from bs4 import BeautifulSoup

start = time.time()
url = "http://%s.student.gunadarma.ac.id"
datas = [x.rstrip() for x in open("npm.txt")]
print(datas[-1])
nama = "Muhammad Ilham Hanifan"

def checkValid(npm,nama):
	try:
		response = requests.get(url % (npm))
	except UnicodeError:
		return False
	soup = BeautifulSoup(response.content, 'html.parser')
	title = [ x.strip() for x in str(soup.title)[7:].split('-') ][:2]
	if title[0] == npm and len(npm)==8 : # and title[1] == nama:
		return True
	else:
		return False

#MainLoop

valid = []
invalid = []
for x in datas:
	if x=='':
		break
	status = checkValid(x,nama)
	if status:
		print(f"{x} is valid")
		valid.append(x)
	else:
		print(f"{x} is INVALID")
		invalid.append(x)

print(time.time()-start)#!/usr/bin/python3
import requests
import time
from bs4 import BeautifulSoup

start = time.time()
url = "http://%s.student.gunadarma.ac.id"
datas = [x.rstrip() for x in open("npm.txt")]
print(datas[-1])
nama = "Muhammad Ilham Hanifan"

def checkValid(npm,nama):
	try:
		response = requests.get(url % (npm))
	except UnicodeError:
		return False
	soup = BeautifulSoup(response.content, 'html.parser')
	title = [ x.strip() for x in str(soup.title)[7:].split('-') ][:2]
	if title[0] == npm and len(npm)==8 : # and title[1] == nama:
		return True
	else:
		return False

#MainLoop

valid = []
invalid = []
for x in datas:
	if x=='':
		break
	status = checkValid(x,nama)
	if status:
		print(f"{x} is valid")
		valid.append(x)
	else:
		print(f"{x} is INVALID")
		invalid.append(x)

print(time.time()-start)
