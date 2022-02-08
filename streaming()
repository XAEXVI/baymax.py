from re import I
import requests
import json
import os
import webbrowser

def streaming():
    
    urln = 'https://www.netflix.com/browse'
    urld = 'https://www.disneyplus.com/pt-br/home'
    urlp = 'https://www.primevideo.com/?ref_=av_auth_return_redir&language=pt_br'
    urlh = 'https://play.hbomax.com/page/urn:hbo:page:home/'
    urlc = 'https://www.crunchyroll.com/pt-br'
    urls = [ urld, urln, urlp, urlh]
    
    sr = str(input('Choose your Streaming service: '))
    services = ['Netflix','netflix','tudum' ,'Tudum', 'Disney+','disney+','Disney','disney','Disney +','disney +', 'Hbo Max', 'hbo Max', 'HboMax', 'hbomax', 'Hbomax', 'Hbomax','hbo','Hbo', 'Prime video', 'prime video', 'Prime', 'prime', 'Amazon Prime','amazon prime',' Crunchyroll', 'crunchyroll']
    quit = False
    if sr.lower() in ['quit']:
       quit = True
        #hp ()
    if  sr.lower() == "netflix": 
            print('Opening the desired streaming service.')
            webbrowser.open(urln)    
    if sr.lower() in  ["disney", "disney+", "disney +"]:
            print('Opening the desired streaming service.')
            webbrowser.open(urld)           
    if sr.lower() in  ["amazon prime", "prime", "prime video"]:
            print('Opening the desired streaming service.')
            webbrowser.open(urlp)
    if sr.lower() in  ["hbo", "hbo max"]:
            print('Opening the desired streaming service.')
            webbrowser.open(urlh)
    if sr.lower() in  ["Crunchy", "crunchyroll"]:
            print('Opening the desired streaming service.')
            webbrowser.open(urlc)

    elif sr != services:
        srr = str(input("It wasn't possible to recognize the desired streaming service, please try again: " ))
        
        quit = False
        if srr.lower() in ['quit']:
                quit = True
        
        if  srr.lower() == "netflix": 
                print('Opening the desired streaming service.')
                webbrowser.open(urln)    
        if srr.lower() in  ["disney", "disney+", "disney +"]:
                print('Opening the desired streaming service.')
                webbrowser.open(urld)           
        if srr.lower() in  ["amazon prime", "prime", "prime video"]:
                print('Opening the desired streaming service.')
                webbrowser.open(urlp)
        if srr.lower() in  ["hbo", "hbo max"]:
                print('Opening the desired streaming service.')
                webbrowser.open(urlh)           
        if sr.lower() in  ["Crunchy", "crunchyroll"]:
            print('Opening the desired streaming service.')
            webbrowser.open(urlc)
streaming()
    
