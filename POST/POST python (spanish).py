# -*- encoding: utf8 -*-

##   Ejemplo simple de llamada a las APis de Apicultur desde python 
##   Sólo sirve para ver como se hacen las llamdas, y como se seleccionan algunos valores
##  de la respuesta. [se devuelve una lista pero sólo se sacan valores de la primera palabra y el primer
##  lema de la lista]
##   IMPORTANTE: Debes colocar el valor del Access Token para que funcione!  
##  necesitas instalar el modulo requests y el modulo JSON 


import requests
import json

## IMPORTANTE: PON EL VALOR DE TU ACCESS TOKEN

AccessToken = 'XXXXXXXXXXXXXXXXXXXX'

## La función que llama a las APIs

def apicultur_post(query,endpoint):    

## Info de los headers, respuesta en JSON y clave de acceso: Recuerda cambiarla

    headers = {'content-type': 'application/json', 'Authorization':'Bearer '+ AccessToken}
    
    r = requests.post( endpoint, data=json.dumps(query),  headers=headers)

    if r.status_code == 200:
        results = r.json()
        print 'Objeto JSON devuelto por la API( en este caso es una lista):'
        print results
        print
        return (results)
    else:
        print 'respuesta erronea, codigo de error', r.status_code, 'valor devuelto', r.json()
        return False

## Este es el inicio del programa:
## en primer lugar ponemos la dirección del end point
## Y después el valor    
    
endpoint = "http://store.apicultur.com/api/etiqueta/1.0.0"
query = {"texto": "Me llamo eduardo."}
   
response = apicultur_post(query,endpoint)

if response <> False:
     
    print 'Datos primera palabra a procesar (primer elemento de la lista): ', response[0]  
    print
    print 'Valor del campo palabra [diccionario]:', response[0]['palabra']
    print
    print 'Valor del campo lemas [diccionario] que devuelve una lista:', response[0]['lemas']
    print
    print 'Valor del campo categoria [primer elemento de la lista de lemas con el valor dicccionario categoria]:', response[0]['lemas'][0]['categoria']
    print
    print 'Valor del campo lema [primer elemento de la lista de lemas con el valor dicccionario lema]:', response[0]['lemas'][0]['lema']    
    print
else:
       print "Respuesta erronea", query

print "\nfinished"
