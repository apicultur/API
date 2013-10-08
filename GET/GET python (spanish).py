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

AccessToken = 'XXXXXXXXXXXXXXXXXXXXXXXX'

## La función que llama a las APIs

def apicultur_get(query,endpoint):    

## Info de los headers, respuesta en JSON y clave de acceso: Recuerda cambiarla

    headers = {'content-type': 'application/json', 'Authorization':'Bearer '+ AccessToken}
    
    r = requests.get( endpoint+query,  headers=headers)

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
## Y después el valor que pasamos
## endpoint + query es la llamada que haremos
    
endpoint = "http://store.apicultur.com/api/categoriza/1.0.0/"
query = "como"
   
response = apicultur_get(query,endpoint)

if response <> False:
     
    print 'Datos palabra a procesar (elemento del diccionario): ', response['categorias']  
    print
    print 'Valor del campo palabra [diccionario]:', response['palabra']
    print
    print 'Valor del primer valor de las categorias', response['categorias'][0]
    print
    print 'Valor del segundo valor de las categorias', response['categorias'][1]
    print
    
else:
       print "Respuesta errónea", query

print "\nfinished"
