'''1. Scrivere uno script che legge un testo seguito da un numero intero N e visualizza gli ultimi
N carateri del testo
2. Scrivere uno script che legge un testo, seguito da una stringa S, seguita da un numero
intero N, e visualizza tutti i gruppi di N caratteri consecutivi presenti nel testo che iniziano
con S. Si assuma N >= len(S)'''

'''1. 
testo = input('Scrivi un testo : \n')
numero = input ('Scrivi un numero N:ì+\n')
N= int(numero)
print(testo[:N])'''

testo = input('Scrivi un testo : \n')
s = input('Scrivi una parola : \n')
numero = input ('Scrivi un numero N :ì+\n')
N= int(numero)

if len(s) > N:
        print("Errore: La lunghezza della stringa S deve essere minore o uguale a N.")

for i in range(len(testo)):

    if len(testo[i])==N and testo[i:i+len(s)] == s :# recupera i singoli caratteri della parola e verifica se sono u
        #uguali a s
        gruppo = testo[i]
    print('Questi sono i ',gruppo)
