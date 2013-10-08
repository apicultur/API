# -*- encoding: utf8 -*-

##   Simple exmaple of an API call for APICULTUR APIs [POST]
##   The only use is to show hos make tha calls and to see how extract some of the answer values
##  [The API returns a list but we only take the values for the first word an the first lema of the list]
##
##   VERY IMPORTANT: You need to add the Access token value in order to work!  
##  remember to install the requests an JSON modules

import requests
import json

## IMPORTANT: Insert your acces token value here

AccessToken = 'XXXXXXXXXXXXXXXXXXXXX'

## This is the function that calls the APIs's

def apicultur_post(query,endpoint):    

## Headers info, the answer it's a JSON structure and the access key: Remember to change it

    headers = {'content-type': 'application/json', 'Authorization':'Bearer '+ AccessToken}
    
    r = requests.post( endpoint, data=json.dumps(query),  headers=headers)

    if r.status_code == 200:
        results = r.json()
        print 'JSON Object returned by the API( a list in this case):'
        print results
        print
        return (results)
    else:
        print 'Bad answer, error code', r.status_code, 'value returned', r.json()
        return False

## The beginning of thhe program:
## End point address
## Value to pass trough    
    
endpoint = "http://store.apicultur.com/api/etiqueta/1.0.0"
query = {"texto": "Me llamo eduardo."}
   
response = apicultur_post(query,endpoint)

if response <> False:
     
    print 'First word to process data (first list element): ', response[0]  
    print
    print 'Value of the field palabra [dictionary]:', response[0]['palabra']
    print
    print 'Value of the field lemas [diccionario] returns a list:', response[0]['lemas']
    print
    print 'Value of the field categoría [first elementy of the list of lemas with the dictionary value categoria]:', response[0]['lemas'][0]['categoria']
    print
    print 'Value of the field lema [fisrs element od the list of lemas with the dictionary value lema]:', response[0]['lemas'][0]['lema']    
    print
else:
       print "Wrong answer for ", query

print "\nfinished"
