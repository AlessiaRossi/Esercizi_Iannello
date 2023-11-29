'''Scrivere uno script che legge un testo, verifica che dopo un punto c'è sempre almeno
uno spazio seguito da una lettera maiuscola e stampa un messaggio che comunica il
risultato della verifica'''

import argparse
testo = input('Scrivere un testo:\n')
verificato=bool

for i in range(len(testo)):
    if testo[i]== '.' and testo[i+1] ==' ' and testo[i+2].isupper():
        verificato=True


if verificato==True:
    print ('La condizione è verificata')
else:
    print('La condizione non è verificata')

