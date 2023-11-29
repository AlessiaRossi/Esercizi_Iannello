''' Scrivere uno script che legge due parole (con lettere tutte minuscole) e visualizza un
messaggio che indica se la prima parola precede la seconda in ordine alfabetico, se sono
uguali o se la seconda precede la prima --> clausola elif'''

parola1 = input('Scrivi la prima parola:\n')
parola2 = input('Scrivi la seconda parola:\n')

prima_parola = parola1.lower()
seconda_parola =parola2.lower()

if prima_parola < seconda_parola:
    print ('La parola', prima_parola,'precede la',seconda_parola )
elif prima_parola > seconda_parola:
    print('La parola', prima_parola,'segue la',seconda_parola )
else:
    print('Le due parole sono uguali')






