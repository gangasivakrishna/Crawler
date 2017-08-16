from bs4 import BeautifulSoup
import re
import requests
import pymongo
import pprint
from pymongo import MongoClient
client=MongoClient('mongodb://root:'+'6Cwm7s.5Dk'+ '@192.168.1.219')
db=client.rocketreach
me=db.company
me1=db.mails
for m in range(14828,17180,2):
	a=(me.find_one({'_id':m}))
	for n in a.keys():
		if(n=='domain'):
			urln=(a[n])
			domain=(a['domain'])
			cidno=(a['cid'])
			idno=m
			proc=[]	
			car=[]
			contact=[]
			about=[]
			mail=[]
			try:
				response = requests.get(urln)
				soup=BeautifulSoup(response.text, "html.parser")
				links = [a.attrs.get('href') for a in soup.select('a[href]')]
				for i in links:
					if("career" in i or "Career" in i):
						car.append(i)
					elif("contact" in i or "Contact" in i):
						contact.append(i)
					elif("about" in i or ("About" in i)):
						about.append(i)
					else:
						pass
				car=list(set(car))
				contact=list(set(contact))
				about=list(set(about))
				proc=car+contact+about
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
								mail.append(k)
					else:
						newurl=urln+j
						r=requests.get(newurl)
						data=r.text
						soup=BeautifulSoup(data,'html.parser')
						for name in soup.find_all('a'):
							k=name.text
							a=bool(re.match('[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',k))
							if('dot' in k and 'at' in k)or ('@' in k and a==True):
								k=k.replace(" ",'').replace('\r','')
								k=k.replace('\n','').replace('\t','')
								mail.append(k)
				mail=set(mail)
				print("Emails:",m,mail,cidno,domain)
				if(len(mail)!=0):
					post={"_id":m,"domain":domain,"cid":cidno,"emails":list(mail)}
					db.mails.insert(post)
					print("inserted")
				else:
					post={"_id":m,"domain":domain,"cid":cidno}
					db.mails.insert(post)
					print("inserted")
			except requests.exceptions.RequestException as e:
				post={"_id":m,"domain":domain,"cid":cidno,"status":1}
				db.mails.insert(post)
				print(e)

