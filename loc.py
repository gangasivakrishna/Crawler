from bs4 import BeautifulSoup
import re
import requests
from pymongo import MongoClient
client=MongoClient('localhost',27017)
db=client.locatefamily
count=0
for i in range(15953,16218):
	url="http://www.locatefamily.com/Street-Lists/Afghanistan/index-"+str(i)+".html"
	response = requests.get(url)
	soup=BeautifulSoup(response.text, "html.parser")
	try:
		for link in soup.find_all('tr'):
			a=link.text
			k=a.split('\n')
			k.pop(0)
			k.pop(0)
			k.pop()
			print(k)
			new_list=k
			print(i)
			if("Name" not in new_list and "Address" not in new_list)and(new_list is not None):
				count+=1
				post={"_id":count,"name":new_list[0],"address":new_list[1],"mobile":new_list[2]}
				db.Afghanistan.insert(post)
	except requests.exceptions.RequestException as e:
			print(e)
