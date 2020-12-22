#!/usr/bin/python3
import requests,re,sys
import datetime
#from idol import *

## IDOL CLASS
class Idol:
	def __init__(self,name,link,date,time):
		self.name = name
		self.link = link
		self.date = date
		self.time = time

	def is_live(self,name,now):
		pass

##



def scrape_n_clean(a,b):
    res = requests.get(a,cookies=b)
    resu = res.text
    resu = ''.join([ x for x in resu.split('<div class="holodule navbar-text" style="letter-spacing: 0.3em;">')[1:] ])
    resu = [ x for x in resu if x != ' ']
    resu = [ x for x in resu if x != '\r']
    resu = (''.join(resu)).split('\n')
    return resu

def get_idols(lines):
    name, link, date, time = '','','',''
    data = []
    for i,line in enumerate(lines):
        resul = {}
        if '2020covercorp' in line:
            break

        if re.match('\d{2}\/\d{2}',line):
            date = line

        if re.match('<a',line):
            time = lines[i+8]
            resu = lines[i+6]
            resu = resu.split("event_label")
            name = resu[0].lstrip("")[54:-3] # remove onClick=\"gtag('event','movieClick',{'event_category':' and 3 digits
            link = resu[1][11:-15] # remove ':' and ','value':1});"
            data.append(Idol(name,link,date,time))
    return data

def get_data():
    url = 'https://schedule.hololive.tv/simple'
    cookie = dict(timezone='Asia/Jakarta')
    data = scrape_n_clean(url,cookie)
    data = get_idols(data)
    data = translate_names(data)
    return data

def get_schedule():
    data = get_data()
    print('>> STREAM SCHEDULE <<')
    for x in data:
        print(f'{(x.name)}')
        print(f'{x.date}  | {x.time}  |  {x.link}')

def get_todate():
    #at = timezone('Asia/Tokyo')
    #at = datetime.datetime.now(tz=at) # for Japan time zone    return x.strftime("%m/%y")
    at = datetime.datetime.now()
    return (at.strftime('%m/%d'))

def get_tod_schedule():
    today = get_todate()
    data = get_data()
    print('>> TODAY\'S SCHEDULE <<')
    print(today)
    for x in data:
        if x.date == today:
            print(f'{(x.name)}')
            print(f'{x.date}  | {x.time}  |  {x.link}')

def translate_names(data):
    fi = open('./data/translate.csv','r')
    dic = fi.read().split('\n')
    dic = [(x.replace("'",'').split(',')) for x in dic]
    dicc = {}
    for x,y in dic:
        dicc[y] = x

    for idol in data:
        for x in dicc:
            if idol.name in dicc:
                idol.name = dicc[idol.name].title()

    return data

def main():
    get_tod_schedule()
    #get_schedule()

if __name__ == '__main__':
    main()


'''
                            <a
    href="https://www.youtube.com/watch?v=AomEZPtsPfQ"
    target="_blank"
    style="color:#212529;
            border: 0;
            "
    onClick="gtag('event','movieClick',{'event_category':'夕刻ロベル','event_label':'https://www.youtube.com/watch?v=AomEZPtsPfQ','value':1});"
>


dates = re.findall('\d{2}\/\d{2}',soup.text)
calendar = re.findall('\d{2}\:\d{2}',soup.text)

'''

#TODO
#- change timezone
#- 
