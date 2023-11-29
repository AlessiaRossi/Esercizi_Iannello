'''Creare uno script che legge una lista di nomi dal file 'nomi.json' e una lista di numeri dal
file 'età.json', entrambi in formato JSON, verificare che le due liste sono di uguale
lunghezza e creare un dizionario che ha per chiavi le stringe della lista letta dal file
'nomi.json' e per informazioni associate i corrispondenti numeri della lista letta dal file
'età.json'. Salvare infine il dizionario in un file in formato JSON'''

import json
eta = json.load(open("eta.json"))
nomi = json.load(open("nomi.json"))
valori_eta=[]
valori_nomi=[]
for i in eta['eta']:
    valori_eta.append(i)

for j in nomi['nomi']:
    valori_nomi.append(j)

if len(valori_nomi)==len(valori_eta):
    print('Le due liste sono di uguale lunghezza')
else :
    print('Le due liste non sono di uguale lunghezza')


diz = dict(zip(valori_nomi,valori_eta))

print(diz)





