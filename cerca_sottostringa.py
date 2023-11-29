'''Dato un testo , cercare e contare quante volte una stringa è presente nel testo
ed indicare la posizione della stringa nel testo -- utilizzando metodi della classe str'''

# legge un testo e una stringa da cercare
testo = input('Dammi un testo\n')
stringa_da_cercare = input('Dammi la stringa da cercare: ')

l = len(stringa_da_cercare)  # variabile di appoggio

# scandisce il testo cercando la striga 
conta = 0 
i = 0
while i < len(testo)-l:
    if testo[i:i+l] == stringa_da_cercare:
        # trovata un'altra occorrenza
        conta += 1
        # stampa dove è stata trovata l'occorrenza
        print('Trovata la stinga', stringa_da_cercare, 'in posizione', i)
        # avanza di l = len(stringa _da_cercare) caratteri
        i += l
    else:
        # non trovata un'occorrenza: avanza di un carattere
        i += 1

# stampa il numero di occorrenze trovate
print('trovate', conta, 'occorrenze della stringa', stringa_da_cercare)
