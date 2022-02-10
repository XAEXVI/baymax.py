import requests
import json
import os
import webbrowser

def streaming():


    services = ['Netflix','netflix','Disney+','disney+','Disney','disney','Disney +','disney +', 'Hbo Max', 'hbo Max', 'HboMax', 'hbomax', 'Hbomax', 'Hbomax','hbo','Hbo', 'Prime video', 'prime video', 'Prime', 'prime', 'Amazon Prime','amazon prime',' Crunchyroll', 'crunchyroll']
    urln = 'https://www.netflix.com'
    urld = 'https://www.disneyplus.com'
    urlp = 'https://www.primevideo.com'
    urlh = 'https://play.hbomax.com'
    urlc = 'https://www.crunchyroll.com'
    urlg = 'https://globoplay.globo.com/'
    urlf = 'https://www.funimation.com'
    urla = 'https://tv.apple.com'
    urlst = 'https://www.starplus.com'
    urls = [ urld, urln, urlp, urlh, urlc, urlg, urlf, urla]
    
    sr = str(input('Choose your Streaming service: '))
    if sr in ['quit']:
                quit = True
                print('Welcome back to the main menu')
    elif sr.lower() in ["netflix"]: 
                print('Opening the desired streaming service.')
                webbrowser.open(urln)    
    elif sr.lower() in  ["disney", "disney+", "disney +"]:
                print('Opening the desired streaming service.')
                webbrowser.open(urld)           
    elif sr.lower() in  ["amazon prime", "prime", "prime video"]:
                print('Opening the desired streaming service.')
                webbrowser.open(urlp)
    elif sr.lower() in  ["hbo", "hbo max"]:
                print('Opening the desired streaming service.')
                webbrowser.open(urlh)
    elif sr.lower() in  ["Crunchy", "crunchyroll"]:
                print('Opening the desired streaming service.')
                webbrowser.open(urlc)
    elif sr.lower() in  ["globoplayer", "globo play", 'globo']:
                print('Opening the desired streaming service.')
                webbrowser.open(urlg)
    elif sr.lower() in  ["funimation"]:
                print('Opening the desired streaming service.')
                webbrowser.open(urlf)
    elif sr.lower() in  ["apple tv", "Apple"]:
                print('Opening the desired streaming service.')
                webbrowser.open(urla)
    elif sr.lower() in  ["star +", "star+", 'star']:
                print('Opening the desired streaming service.')
                webbrowser.open(urlst)
    else:
        while sr.lower() not in services:
                sr = input("It wasn't possible to recognize the desired streaming service Please try again: " )
                quit = False
                if sr.lower() in ['quit']:
                        quit = True
                elif sr.lower() in ["netflix", "Tudum"]: 
                        print('Opening the desired streaming service.')
                        webbrowser.open(urln)    
                elif sr.lower() in  ["disney", "disney+", "disney +"]:
                        print('Opening the desired streaming service.')
                        webbrowser.open(urld)           
                elif sr.lower() in  ["amazon prime", "prime", "prime video"]:
                        print('Opening the desired streaming service.')
                        webbrowser.open(urlp)
                elif sr.lower() in  ["hbo", "hbo max"]:
                        print('Opening the desired streaming service.')
                        webbrowser.open(urlh)           
                elif sr.lower() in  ["Crunchy", "crunchyroll"]:
                        print('Opening the desired streaming service.')
                        webbrowser.open(urlc)
                elif sr.lower() in  ["globoplayer", "globo play", 'globo']:
                            print('Opening the desired streaming service.')
                            webbrowser.open(urlg)
                elif sr.lower() in  ["funimation"]:
                            print('Opening the desired streaming service.')
                            webbrowser.open(urlf)
                elif sr.lower() in  ["apple tv", "Apple"]:
                            print('Opening the desired streaming service.')
                            webbrowser.open(urla)
                elif sr.lower() in  ["star +", "star+", 'star']:
                            print('Opening the desired streaming service.')
                            webbrowser.open(urlst)
streaming()
