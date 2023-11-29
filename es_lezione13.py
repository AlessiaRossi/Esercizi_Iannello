'''Riscrivere lo script cerca_sottostringa sostituendo in tutte le chiamate alla funzione print
un'unica f-string al posto dei parametri'''

'''Dato un testo , cercare e contare quante volte una stringa è presente nel testo
ed indicare la posizione della stringa nel testo -- utilizzando metodi della classe str'''

testo = input('Dammi un testo\n')
stringa_da_cercare = input('Dammi una stringa da cercare: ')
con=[]
pos=[]
testo=testo.split(' ')
stringa_da_cercare=stringa_da_cercare.split()
print (type(testo), type(stringa_da_cercare))
for x in stringa_da_cercare:
   con=testo.count(x)
   pos=testo.index(x)




print (f'la stringa {stringa_da_cercare} ha occorrenza {con}   nella posizione {pos} del testo' )