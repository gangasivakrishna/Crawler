from tkinter import *
from tkinter import messagebox
import tkinter as tk
import random
from bs4 import BeautifulSoup
import re
import requests
import random
import urllib.request


root = Tk()
root.title('ZeroCool GSKrawler')


# scrollbar.config(command = frame.yview )
# text = Text(root)
# scrollbar = Scrollbar(root)
# scrollbar.pack(side=RIGHT, fill=Y)

# scrollbar = tk.Scrollbar(root, orient="vertical")
# listbox = Listbox(root)
# scrollbar.config(command=listbox.yview)


# headname="""
# ▀▀█ █▀▀ █▀▀█ █▀▀█ █▀▀ █▀▀█ █▀▀█ █░░ 　 █▀▀▀ █▀▀ █░█ 
# ▄▀░ █▀▀ █▄▄▀ █░░█ █░░ █░░█ █░░█ █░░ 　 █░▀█ ▀▀█ █▀▄ 
# ▀▀▀ ▀▀▀ ▀░▀▀ ▀▀▀▀ ▀▀▀ ▀▀▀▀ ▀▀▀▀ ▀▀▀ 　 ▀▀▀▀ ▀▀▀ ▀░▀ 
# """

logo=PhotoImage(file="spider.png")
logo = logo.zoom(15) #with 250, I ended up running out of memory
logo = logo.subsample(32)
w1=Label(root,image=logo).pack(side="top")

mystring =tk.StringVar(root)
def getvalue():
	url=mystring.get()
	if(url.startswith("http://") or url.startswith("https://")):
		root1 = Tk()
		root1.title('Emails')
		root1.geometry("550x350+300+300") 
		listbox = Listbox(root1)
		listbox.pack(fill=BOTH, expand=1)
		scrollbar = Scrollbar(listbox)
		scrollbar.pack(side=RIGHT, fill=Y)
		proc=[]
		mail=[]
		try:
			response=requests.get(url)
			soup=BeautifulSoup(response.text,'html.parser')
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

								listbox.insert(END,k)
								print(k)
								# text = Text(root)
								# text.pack()
								# text.insert(END, k)
    						# listbox.insert(END,k)
							mail.append(k)
					listbox.config(yscrollcommand=scrollbar.set)
					scrollbar.config(command=listbox.yview)
							
		except (requests.exceptions.RequestException) as e:
			print("Exception occured")
			messagebox.showerror(title="Exception",message=e)
	else:
		messagebox.showerror(title="Enter correct URL",message="Enter correct URL")





def getimage():
	url=mystring.get()
	if(url.startswith("http://") or url.startswith("https://")):
		root2 = Tk()
		root2.title('Images')
		root2.geometry("550x350+300+300") 
		listbox = Listbox(root2)
		listbox.pack(fill=BOTH, expand=1)
		scrollbar = Scrollbar(listbox)
		scrollbar.pack(side=RIGHT, fill=Y)
		try:
			response=requests.get(url)
			soup=BeautifulSoup(response.text,'html.parser')
			for img in soup.findAll('img'):
				src=img.get('src')
				print(src)
				name=random.randrange(1,10000)
				imgname=str(name)
				lk=url+"/"+src
				urllib.request.urlretrieve(lk,imgname)
				listbox.insert(END,imgname+" downloaded")
			listbox.config(yscrollcommand=scrollbar.set)
			scrollbar.config(command=listbox.yview)
		except(requests.exceptions.RequestException) as e:
			print("Exception Occured")
			messagebox.showerror(title="Exception",message=e)
	else:
		messagebox.showerror(title="Enter Correct URL",message="Enter Correct URL")

 #    if(url.startswith("http://") or url.startswith("https://")):
	# 	try:
	# 		response=requests.get(url)
	# 		soup=BeautifulSoup(response.text,'html.parser')
	# 		for img in soup.findAll('img'):
	# 	        src=img.get('src')
	# 	        print(src)
	# 	        name=random.randrange(1,100)
	# 	        imgname=str(name)
	# 	        lk=url+"/"+src
	# 	        urllib.request.urlretrieve(lk,imgname)
							
	# 	except (requests.exceptions.RequestException) as e:
	# 		print("Exception occured")

	# else:
	# 	messagebox.showinfo("Enter correct URL")



def getlinks():
	url=mystring.get()
	if(url.startswith("http://") or url.startswith("https://")):
		proc=[]
		mail=[]
		root3 = Tk()
		root3.title('Links')
		root3.geometry("550x350+300+300") 
		listbox = Listbox(root3)
		listbox.pack(fill=BOTH, expand=1)
		scrollbar = Scrollbar(listbox)
		scrollbar.pack(side=RIGHT, fill=Y)
		try:
			response=requests.get(url)
			soup=BeautifulSoup(response.text,'html.parser')
			for link in soup.find_all('a'):
				print(link.text,"\n"+"URL : "+link.get('href'))
				print("\n")
				k=link.text,"\n"+"URL : "+link.get('href')
				nl='\n'
				listbox.insert(END,'URL')
				listbox.insert(END,link.text)
				listbox.insert(END,link.get('href'))
				listbox.insert(END,'..........................................................')


								# text = Text(root)
								# text.pack()
								# text.insert(END, k)
    						# listbox.insert(END,k)
			listbox.config(yscrollcommand=scrollbar.set)
			scrollbar.config(command=listbox.yview)
		except (requests.exceptions.RequestException) as e:
			print("Exception occured")
			messagebox.showerror(title="Exception",message=e)
	else:
		messagebox.showerror(title="Enter correct URL",message="Enter correct URL")






w1=Label(root,justify="left",padx=10,pady=10,text="Zerocool GSKrawler",fg = "red",font='Futura 26 bold').pack(side="top")

w2=Label(root,justify="left",padx=10,pady=10,text="Ex: http://www.example.com/",fg = "green").pack(side="top")

# button = tk.Button(root, text='Stop', width=25, command=root.destroy)

# width x height + x_offset + y_offset:
e1 = Entry(root,textvariable = mystring,width=100,fg="blue",bd=3,selectbackground='violet').pack()
root.geometry("550x350+300+300") 
button1 = tk.Button(root, 
                text='Emails', 
                fg='White', 
                bg= 'dark green',height = 1, width = 10,command=getvalue).pack()

button2 = tk.Button(root, 
                text='Links', 
                fg='White', 
                bg='steel blue',height = 1, width = 10,command=getlinks).pack()
button3 = tk.Button(root, 
                text='Images', 
                fg='White', 
                bg='dark orange',height = 1, width = 10,command=getimage).pack()
button4 = tk.Button(root, 
                text='Quit', 
                fg='White', 
                bg= 'red',height = 1, width = 5,command=root.quit).pack()



# options = ['Emails','Links','Images','MobileNumbers','Quit']
# labels = range(5)
# for i in range(5):
#    ct = [random.randrange(256) for x in range(3)]
#    brightness = int(round(0.299*ct[0] + 0.587*ct[1] + 0.114*ct[2]))
#    ct_hex = "%02x%02x%02x" % tuple(ct)
#    bg_colour = '#' + "".join(ct_hex)
#    l = tk.Button(root, 
#                 text=options[i], 
#                 fg='White' if brightness < 120 else 'Black', 
#                 bg=bg_colour,height = 2, width = 15).pack()
#    # l.place(x = 20, y = 30 + i*30, width=120, height=25)
          
# root.mainloop()


root.mainloop()
