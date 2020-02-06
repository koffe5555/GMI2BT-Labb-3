import requests
import json
import sys

ContainerSave = []

class MainMenu():
    def __init__(self):
        self.menu()
    def menu(self):
        #answer = input('1. Sök film\n2. Visa senaste sökning\n3. Avsluta\n\n')
        try:
            while True:
                answer = input('1. Sök film\n2. Visa senaste sökning\n3. Avsluta\n\n')
                if answer == '1':
                    Movie()
                    History()
                elif answer == '2':
                    menu2()
                elif answer == '3':
                    break
                else:
                    print('Fel val!!')
        except ValueError as error:
            print(error)
    


class Movie():
    def __init__(self):
        self.ApiMovie()
    def ApiMovie(self):
        movie = input('Search: ')
        try:
            api = requests.get(f'http://www.omdbapi.com/?apikey=fa029d1c&s={movie}')
            info = api.json() #Hämta api från URL
        except FileNotFoundError as error:
            print(error)
        try:
            with open('Movie.json', 'w', encoding='utf-8') as fpoint:
                json.dump(info, fpoint, ensure_ascii=False, indent=4) # Lägger api i json som string
        except FileNotFoundError as error:
            print(error)
        count = 0
        dic = info['Search']
        for s in dic: # Skriver ut innehåll av json med title och year
            count += 1
            print(count,'. ',s['Title'], s['Year'])

        search = int(input('Skriv siffran på filmen du vill välja: \n')) #Användaren väljer vilken film de vill ha
        try:
            with open('Movie.json', 'r', encoding='utf-8') as j_file:
                Readjson = json.load(j_file)
                choice = Readjson.get('Search')[search-1]
                ContainerSave.append(choice)
        except FileNotFoundError as error:
            print(error)      

        try:
            with open('SearchMovies.json', 'w', encoding='utf-8') as j_fil:
                json.dump(choice, j_fil, ensure_ascii=False, indent=4)
        except FileNotFoundError as error:
            print(error)


#Lista till json kunna skriva ut vilka filmer man valt, 2.2 ska sedan kunna gå in i listan och skriva ut vilken man väljer som for med count
class menu2():
    def __init__(self):
        self.menusecond()
    def menusecond(self):
        
        try:
            userin = int(input('1 Visa information om senaste sökta filmer\n2. Visa information om vald film\n'))
            if userin == 1:
                for line in ContainerSave:
                    print(line['Title'], line['Year'])
            elif userin == 2:
                History()
            else:
                self.menusecond()     
        except ValueError:
            print('Skriv 1 eller 2 !!')


class History():
    def __init__(self):
        self.SearchHistory()
    def SearchHistory(self):
        try:
            with open('SearchMovies.json', 'r', encoding='utf-8') as file_read:
                show = json.load(file_read)
                place = show['imdbID']
                imdb = requests.get(f'http://www.omdbapi.com/?apikey=fa029d1c&i={place}')
                data = imdb.json()
                print(f"Title: {data['Title']}\nYear: {data['Year']}\nGenre: {data['Genre']}\nPlot: {data['Plot']}\n")
        except FileNotFoundError as error:
            print(error)