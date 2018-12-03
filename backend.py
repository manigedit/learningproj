""""import wolframalpha
import wikipedia

input = raw_input("your question: ")


try:
	app_id = "WRQAAL-YPU7VA5R4J"
	client = wolframalpha.Client(app_id)
	res = client.query(input)
	answer = next(res.results)
	print "Wolfraam says" + answer 

except:
	print "wikipedia says" + wikipedia.summary(input , sentences =3)
"""
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

        t.insert(END, "\n\n----------------------------MOVIE INFORMATION-------------------------\n")
        t.insert(END, "\n\t TITLE       : \t\t"+title)
        t.insert(END, "\n\t IMDB RATING : \t\t"+rating)
        t.insert(END, "\n\t RELEASED ON : \t\t"+year)
        t.insert(END, "\n\t DURATION    : \t\t"+str(duration)+" mins")
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
        t.insert(END,"\nNo such movie titled '"+name+"' found!\n")
        status.write ("\nNo such movie titled '"+name+"' found!\n")






