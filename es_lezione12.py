'''Dato in ingresso un testo, creare un dizionario che ha come chiavi tutti e soli i caratteri
presenti nel testo e come informazioni associate le loro occorrenza di nel testo. Salvare
infine il dizionario in un file in formato JSON'''

import json

testo = input('Scrivere un testo:\n')
diz={}
#testo=testo.split(' ')
for x in testo:
 diz[x]=testo.count(x)

del diz[" "]

print (diz)

fout=open('es_lezione12.json','w')

json.dump(diz, fout, indent=3)

fout.close()
