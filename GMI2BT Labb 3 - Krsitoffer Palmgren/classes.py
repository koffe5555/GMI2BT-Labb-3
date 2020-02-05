import requests
import json

ContainerSave = []

class MainMenu():
    def __init__(self):
        def menu(self):
            answer = input('1. Sök film\n2. Visa senaste sökning\n3. Avsluta\n\n')
            try:
                while True:
                    if answer == '1':
                        Movie()
                        menu(self)
                        break
                    elif answer == '2':
                        menu2()
                        menu(self)
                        break
                    #elif answer == '3':
                        #break
                    else:
                        break
            except ValueError as error:
                print(error)
        menu(self)


class Movie():
    def __init__(self):
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
                    json.dump(ContainerSave, j_fil, ensure_ascii=False, indent=4)
            except FileNotFoundError as error:
                print(error)

        ApiMovie(self)
#Lista till json kunna skriva ut vilka filmer man valt, 2.2 ska sedan kunna gå in i listan och skriva ut vilken man väljer som for med count
class menu2():
    def __init__(self):
        def menu2(self):
            
            try:
                userin = int(input('1 Visa information om senaste sökta filmer\n2. Visa information om vald film\n'))
                if userin == 1:
                    for line in ContainerSave:
                        print(line['Title'], line['Year'])
                elif userin == 2:
                    History()
                else:
                    menu2(self)       
            except ValueError:
                print('Skriv 1 eller 2 !!')
        menu2(self)

class History():
    def __init__(self):
        def SearchHistory(self):
            try:
                with open('SearchMovies.json', 'r', encoding='utf-8') as file_read:
                    show = json.load(file_read)
                    print(show['Title'])
            except FileNotFoundError as error:
                print(error)
        SearchHistory(self) 
