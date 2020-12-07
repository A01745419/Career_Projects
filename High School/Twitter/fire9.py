from firebase import firebase
import json
import matplotlib.pyplot as plt
import itertools
import io
import sys
from collections import Counter
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#conexion a la base de datos
firebase = firebase.FirebaseApplication('https://tec-twitter.firebaseio.com/', None)

#codigo que saca una sola instancia de palabras de la base de datos y cuenta la frecuencia de la misma


result = firebase.get('/tec-twitter/Words', '')

palabras=[]
for x in result:
    palabras.append(result[x])
print (palabras[23])

pal=[]
for x in palabras[23]:
    pal.append(x.lower())
print (pal)
conta= dict()

#contando la frecuencia de las palabras en una base de datos, la salida es un diccionario
for word in pal:
    if word in conta:
        conta[word]+=1
    else:
        conta[word]=1

print (conta)

#getting the first 10 elements of the most repeated words
N=50
dictionary = dict(itertools.islice(conta.items(), N))
print (dictionary)

#plotting histogram

plt.bar(list(dictionary.keys()), dictionary.values(), color='g')
plt.show()




