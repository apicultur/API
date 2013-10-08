# -*- encoding: utf8 -*-

##   Simple exmaple of an API call for APICULTUR APIs [GET]
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

def apicultur_get(query,endpoint):    

## Headers info, the answer it's a JSON structure and the access key: Remember to change it

    headers = {'content-type': 'application/json', 'Authorization':'Bearer '+ AccessToken}
    
    r = requests.get(endpoint+query,  headers=headers)

    if r.status_code == 200:
        results = r.json()
        print 'JSON Object returned by the API( a list in this case):'
        print results
        print
        return (results)
    else:
        print 'Bad answer, error code', r.status_code,'value returned', r.json()
        return False

## Este es el inicio del programa:
## en primer lugar ponemos la dirección del end point
## Y después el valor    
    
endpoint = "http://store.apicultur.com/api/categoriza/1.0.0/"
query = "como"
   
response = apicultur_get(query,endpoint)

if response <> False:
     
    print 'Info word to process (dictionary element): ', response['categorias']  
    print
    print 'Value of palabra field [dictionary]:', response['palabra']
    print
    print 'Value of the first value of the categories', response['categorias'][0]
    print
    print 'Value of the second valueof the categorias', response['categorias'][1]
    print
else:
       print "Wrong answer for ", query

print "\nfinished"
