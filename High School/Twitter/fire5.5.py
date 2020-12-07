from firebase import firebase
import json
import sys
import io
from collections import Counter
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
 
#conexion a la base de datos
firebase = firebase.FirebaseApplication('https://tec-twitter.firebaseio.com/', None)

#codigo que saca una sola instancia de hashtags de la base de datos y cuenta la frecuencia de la misma


result = firebase.get('/tec-twitter/Hashtags', '')

#print (result)
hashtags= []
for x in result:
    for y in result [x]:
        hashtags.append(y.lower())
for item in [hashtags]:
    frecuencias = []
    c = Counter(item)
    frecuencias.append(c)
    frecuencias.sort(reverse=True)
    print (frecuencias)

#for label, data in ('Word', frecuencias):
    #pt = PrettyTable(field_names=[label, 'Count'])
    #[ pt.add_row(kv) for kv in frecuencias]
    #pt.align[label], pt.align['Count'] = 'l', 'r' # Set column alignment
    #print(pt) 