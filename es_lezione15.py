''' Creare uno script che contiene le seguenti funzioni:
- una funzione che riceve come parametri una lista di numeri e restituisce un valore
logico che indica se la lista contiene numeri tutti diversi
- una funzione che riceve come parametri due liste di numeri e restituisce due insiemi:
l'insieme dei numeri che sono presenti in entrambe le liste e l'insieme dei numeri che
sono presenti nella prima, ma non nella seconda,
- una funzione che riceve come parametri una lista di numeri e una parola e che
restituisce il numero di numeri pari presenti nella lista se la parola è "even" e il
numero di numeri dispari presenti nella ilsta se la parola è "odd". Prevedere per la
stinga un valore di dafault uguale a "even" '''

'''
numeri=input('Dammi una lista di numeri \n ')
def lista_numeri(numeri):

  #caso di test : 11111 True , 12322 False , 1346 False
    if len(set(numeri))==1: # len(set(numeri)) restituisce il nuemro di elementi diversi, con set tolgo i dulicati
        verifica= True
    else:
         verifica = False
    return(verifica)

#print (len(set(numeri)), verifica)

print(lista_numeri(numeri))'''
'''
prima=input('Dammi la prima lista di numeri \n ')
seconda=input('Dammi la seconda lista di numeri \n ')
# casi di test: 123  345  [], [123] ; 111  123 [1], [11]
def numeri_prsenti(lista1,lista2):
    uguali=[]
    diversi=[]
    lista1.split()
    lista2.split()
    lista1=set(lista1)
    seconda=set(lista2)
    #print(prima,seconda)
    for i in lista1:
        for j in lista2:
            if i == j:
                 uguali.append(i)
        if i not in uguali:
            diversi.append(i)

    return(uguali, diversi)

print (numeri_prsenti(prima,seconda))'''

parola=input('Dammi una parola (even o odd)\n' ) or 'even' #parola di default è even
numeri=input('Dammi una lista di numeri \n')


numeri.split()
pari=int()
dispari=int()
print(parola)
parole=str(parola)
if (parola != 'even') and (parola != 'odd'):
  print('Parola non valida,la parola deve essere o even o odd')
for i in numeri:
    if parole=='even' and int(i)%2==0:
        pari +=1

    if parole=='odd' and int(i)%2 !=0:
      dispari +=1

print (pari, dispari)













