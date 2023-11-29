'''Dato in ingresso un testo e un insieme di caratteri sotto forma di stringa, creare un
à
dizionario che ha come chiavi i caratteri dell'insieme e come informazioni associate le
occorrenza di ciascun carattere nel testo. Visualizzare infine il contenuto del dizionario'''

testo = input('Scrivere un testo:\n')
s = input('Fornire un insieme di caratteri (ad esempio: s,c,d):\n')

''' cane neve renna
n v a
n:4
v:1
a:2 '''

con=[]
s=s.split(' ') #mi indentifica lo spazio , e non lo fa valere come elemento
#print (s)
for x in s:
 #print(x)
 con.append(testo.count(x))
 #print(con)


diz={}
contatore=0
for c in s:
 diz[c]=con[contatore]
 contatore +=1

#for x in s:
 #diz[x]=testo.count(x)


print(diz)