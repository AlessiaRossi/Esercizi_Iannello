'''Dato un testo , cercare e contare quante volte una stringa è presente nel testo
ed indicare la posizione della stringa nel testo '''

#leggo un testo ed una stringa da cercare
testo = input('Fornisci un testo:\n ') # \n e per chedere il testo dalle riga successiva e non appiccicato
stringa_da_cercare = input('Quale strige si deve cercare:\n ')

l=len(stringa_da_cercare) # numero di lettere , variabile di appaggio

#scandisce il testo cercando la stringa
conta = 0
i = 0
while i < len(testo): # prof mette -l perche se siamo troppo vicini alla fine del testo non possiamo trovare striga
    if testo[i:i+l] == stringa_da_cercare:
        #trova un'altra occorrenza
        conta += 1
        #stampa dove è stata trovara l'occorrenza
        print('Trovata la stringa', stringa_da_cercare,'in posizione',i)
        #vanza di l caratteri
        i += l
    else:
        # se non trovo stringa avanti di un carattere
        i += 1
print ('travate', conta, 'occorrenze della stringa', stringa_da_cercare)
