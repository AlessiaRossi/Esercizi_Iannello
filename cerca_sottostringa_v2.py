'''Dato un testo , cercare e contare quante volte una stringa è presente nel testo
ed indicare la posizione della stringa nel testo -- utilizzando metodi della classe str'''

# legge un testo e una stringa da cercare
testo = input('Dammi un testo\n')
stringa_da_cercare = input('Dammi la stringa da cercare: ')

# scandisce il testo cercando la striga 
i = testo.find(stringa_da_cercare,0)  # cerca una prima occorrenza,
# lo 0 opzionale,  è l'indice iniziale da cui iniziare la ricercaù

while i >= 0: # dobbiamo fare ciclo perche se no mi da solo la prima che trova e poi si ferma
    # ha trovato una nuova occorrenza
    # stampa dove è stata trovata l'occorrenza
    print('Trovata la stinga', stringa_da_cercare, 'in posizione', i)
    # cerca una nuova occorrenza
    i = testo.find(stringa_da_cercare,i+len(stringa_da_cercare))

# stampa il numero di occorrenze trovate
print('trovate', testo.count(stringa_da_cercare), 
      'occorrenze della stringa', stringa_da_cercare)
