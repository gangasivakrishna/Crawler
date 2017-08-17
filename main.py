from bs4 import BeautifulSoup
import re
import requests
import random
import urllib.request
print("""
▀▀█ █▀▀ █▀▀█ █▀▀█ █▀▀ █▀▀█ █▀▀█ █░░ 　 █▀▀▀ █▀▀ █░█ 
▄▀░ █▀▀ █▄▄▀ █░░█ █░░ █░░█ █░░█ █░░ 　 █░▀█ ▀▀█ █▀▄ 
▀▀▀ ▀▀▀ ▀░▀▀ ▀▀▀▀ ▀▀▀ ▀▀▀▀ ▀▀▀▀ ▀▀▀ 　 ▀▀▀▀ ▀▀▀ ▀░▀ 


""")


BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'
print(("{0}Ex: {1}http://www.example.com/").format(YELLOW,WHITE))
count=0
while(True):

	print("\n")
	url=input(("{0}Place url to crawl it: ").format(GREEN))
	if(url.startswith("http://") or url.startswith("https://")):
		proc=[]
		mail=[]
		try:
			response=requests.get(url)
			soup=BeautifulSoup(response.text,'html.parser')
			print(("{0}Enter ur choice").format(YELLOW))
			print(("{0}1\t{1}Title").format(RED,MAGENTA))
			print(("{0}2\t{1}Body").format(RED,MAGENTA))
			print(("{0}3\t{1}Links").format(RED,MAGENTA))
			print(("{0}4\t{1}Emails").format(RED,MAGENTA))
			print(("{0}5\t{1}Images{2}").format(RED,MAGENTA,END))
			print(("{0}6\t{1}By using tag name and class name{2}").format(RED,MAGENTA,END))
			print(("{0}7\t{1}By using tag name and id name{2}").format(RED,MAGENTA,END))
			inp=int(input(("{0}Select your choice to crawl:{1} ").format(YELLOW,END)))
			if(inp==1):
				print("\n")
				print(soup.title.string)
				chh=input(("{0}Continue(y/n):{1}").format(YELLOW,END))
				if(chh=='n'):
					break
			elif(inp==2):
				print("\n")
				print(soup.prettify())
				chh=input(("{0}Continue(y/n):{1}").format(YELLOW,END))
				if(chh=='n'):
					break
			elif(inp==3):
				print("\n")
				for link in soup.find_all('a'):
					print(link.text,"\n"+"URL : "+link.get('href'))
					print("\n")
				chh=input(("{0}Continue(y/n):{1}").format(YELLOW,END))
				if(chh=='n'):
					break
			elif(inp==4):
				print("\n")
				links = [a.attrs.get('href') for a in soup.select('a[href]') ]
				for i in links:
					if(("contact" in i or "Contact")or("Career" in i or "career" in i))or('about' in i or "About" in i)or('Services' in i or 'services' in i):
						proc.append(i)
				proc=set(proc)
				for j in proc:
					if(j.startswith("http") or j.startswith("www")):
						r=requests.get(j)
						data=r.text
						soup=BeautifulSoup(data,'html.parser')
						for name in soup.find_all('a'):
							k=name.text
							a=bool(re.match('[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',k))
							if('dot' in k and 'at' in k)or ('@' in k and a==True):
								k=k.replace(" ",'').replace('\r','')
								k=k.replace('\n','').replace('\t','')
								if(len(mail)==0)or(k not in mail):
									print(k)
								mail.append(k)
					else:
						newurl=url+j
						r=requests.get(newurl)
						data=r.text
						soup=BeautifulSoup(data,'html.parser')
						for name in soup.find_all('a'):
							k=name.text
							a=bool(re.match('[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',k))
							if('dot' in k and 'at' in k)or ('@' in k and a==True):
								k=k.replace(" ",'').replace('\r','')
								k=k.replace('\n','').replace('\t','')
								if(len(mail)==0)or(k not in mail):
									print(k)
								mail.append(k)
				mail=set(mail)
				if(len(mail)==0):
					print(("{0}NO MAILS FOUND{1}").format(RED,END))
				chh=input(("{0}Continue(y/n):{1}").format(YELLOW,END))
				if(chh=='n'):
					break

			elif(inp==5):
				
			    for img in soup.findAll('img'):
			        src=img.get('src')
			        print(src)
			        name=random.randrange(1,100)
			        imgname=str(name)
			        lk=url+"/"+src
			        urllib.request.urlretrieve(lk,imgname)
			    chh=input(("{0}Continue(y/n):{1}").format(YELLOW,END))
			    if(chh=='n'):
			    	break
			elif(inp==6):
				tag=input(("{0}Tag name:{1}").format(YELLOW,END))
				clsname=input(("{0}class name:{1}").format(YELLOW,END))
				for data in soup.find_all(tag, { "class" : clsname }):
					text=data.text
					if(text is not None):
						print(text)
			elif(inp==7):
				tag=input(("{0}Tag name:{1}").format(YELLOW,END))
				idname=input(("{0}id name:{1}").format(YELLOW,END))
				for data in soup.find_all(tag, { "id" : idname }):
					text=data.text
					if(text is not None):
						print(text)
			else:
				print(("{0}Enter correct option\t{1}").format(RED,END))









		except requests.exceptions.RequestException as e:
					print(("{0}Exception Occured{1}").format(RED,END))
	else:
		print(("{0}Enter correct url ").format(RED))

