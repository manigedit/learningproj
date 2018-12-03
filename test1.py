from Tkinter import *
import ttk 
#import backend

##### simple aisha function   #########
import wolframalpha
import wikipedia


def info_movie(name):
	try:
		app_id = "WRQAAL-YPU7VA5R4J"
		client = wolframalpha.Client(app_id)
		quaery = client.query(name)
		answer = next(quaery.results).text

		return "wolfram says " + answer

	except:
		return "wiki says " + wikipedia.summary(name, sentences =3)










"""
###################   backend   function  ##################

import requests
import os
import sys
import json
import bs4

if(sys.version[0] == '3'):
    raw_input = input




status=open('info.txt','a')



def info_movie(name):
    t = name.replace(' ','%20')
    url = 'https://api.themoviedb.org/3/search/movie?api_key=ffb07b773769d55c36ccd83845385205&language=en-US&query='+str(t)+'&page=1&include_adult=false'
    response = requests.get(url)
    u = json.loads(response.text)
    results  = u['results']
    id = results[0]['id']
    url2 = 'https://api.themoviedb.org/3/movie/'+str(id)+'?api_key=ffb07b773769d55c36ccd83845385205&language=en-US'
    response = requests.get(url2)
    w = json.loads(response.text)
    try:
        title = w['title']
        imdb_id = w['imdb_id']
        year = w['release_date']
        genre = w['genres']
        language = w['spoken_languages']
        duration = w['runtime']
        plot = w['overview']

        url3 = 'http://www.imdb.com/title/'+str(imdb_id)
        response = requests.get(url3)
        html = response.text
        soup = bs4.BeautifulSoup(html,"lxml")
        data = soup.select('.ratingValue')
        rating = data[0].get_text('',strip=True)

        trap.insert(END, "\n\n----------------------------MOVIE INFORMATION-------------------------\n")
        trap.insert(END, "\n\t TITLE       : \t\t"+title)
        trap.insert(END, "\n\t IMDB RATING : \t\t"+rating)
        trap.insert(END, "\n\t RELEASED ON : \t\t"+year)
        trap.insert(END, "\n\t DURATION    : \t\t"+str(duration)+" mins")
        # print ("\n\t LANGUAGE    : \t\t"+language[0]['name'])
        #print ("\n\t GENRE       : \t\t"+genre[0]['name'])
        #print ("\n\t PLOT        : \t\t"+plot)

        status.write ("\n\n--------------------------------------MOVIE INFORMATION---------------------------------\n")
        status.write ("\n\t TITLE       : \t\t"+title)
        status.write ("\n\t IMDB RATING : \t\t"+rating)
        status.write ("\n\t RELEASED ON : \t\t"+year)
        status.write ("\n\t DURATION    : \t\t"+str(duration)+" mins")
        # status.write ("\n\t LANGUAGE    : \t\t"+language[0]['name'])
        status.write ("\n\t GENRE       : \t\t"+genre[0]['name'])
        status.write ("\n\t PLOT        : \t\t"+plot)

    except KeyError:
        trap.insert(END,"\nNo such movie titled '"+name+"' found!\n")
        status.write ("\nNo such movie titled '"+name+"' found!\n")


####################################################  End of backend function #################### 
"""


def searchclick():
	if choice.get() == 1:
		wajo = searchbox.get() + " movie"
		res =  wajo + " was searched"
		print searchbox.get()
		print wajo
		geet = info_movie(wajo)
		print geet
		trap.insert(END, geet)
		print " wolfram called to insert"
	elif choice.get() == 2:
		res = "Top " + numchoice.get() + " were searched"

	title.configure(text = res)
	trap.insert(END,  "here goes the summary of the movie")


window = Tk()
window.geometry('750x250')
window.title("movie mania")

choice = IntVar()
choice1 = Radiobutton(window, text='by name',value=1, variable=choice)
choice2 = Radiobutton(window, text='top n',value=2, variable=choice)
choice1.grid(column=0, row=0)
choice2.grid(column=1, row=0)


title = Label(window, text="enter the movie you want to search" , font=("Arial Bold", 20))
title.grid(column=0, row=1)

searchbox= Entry(window, width =40)
searchbox.grid(column=0, row=2)
searchbox.focus()

body = Label(window, text="search the top rated movies", font=("Arial Bold", 19))
body.grid(column=0 , row = 3)



numchoice = ttk.Combobox(window)
numchoice['values']= (1,2,3,4,5,6,7,8,9,10,"Text")
numchoice.grid(column=0 , row = 4)
numchoice.current(5)


searchbtn = Button(window, text="search", fg='red', bg='orange', command=searchclick)
searchbtn.grid(column=1, row=2)


s = Scrollbar(window)
trap = Text(window, height=20, width=50)
#s.pack(side=RIGHT, fill=Y)
#t.pack(side=LEFT, fill=Y)

trap.configure(yscrollcommand=s.set)
#summary = Label(window, text="API result", bg = 'green')
s.grid(column=1,row=3)
trap.grid(column=1,row=3)
trap.insert(END, " this is a lonne. ")
#summary = scrolledtext.ScrolledText(window, width=40, height=10)
#summary.grid(column = 2 , row = 0)
s.configure(command=trap.yview)






window.mainloop()