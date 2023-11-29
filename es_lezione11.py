'''Con riferimento alle seguenti informazioni composte, creare file in formato JSON che le
contenga:
- - il numero di studenti presenti a ognuna delle lezioni erogate nell'ultimo anno
accademico
- - i dati anagrafici di una persona
- - le squadre partecipanti a un torneo di calcio
- - il costo dei prodotti in vendita in un neglzio
- - le telefonate ricevute nelle due ultime settimane"'''


import json
dizionario={'Presenza' : {'prima lezione': 10 ,'seconda lezione': 7 ,'terza lezione': 18,'quarta lezione': 11},
            'Dati Anagradici': {'Nome':'Alessia','Cognome':'Rossi','Data Nascita':'28 Luglio 2000','Sesso':'Femmina'},
            'Squadre':{"Squadra1": "Juventus","Squadra2": "Milan","Squadra3": "Inter","Squadra4": "Roma","Squadra5": "Napoli","Squadra6": "Lazio",
    "Squadra7": "Atalanta","Squadra8": "Fiorentina"},
            'Prodotti':{"Prodotto1": 10.50, "Prodotto2": 20.25,"Prodotto3": 15.75,"Prodotto4": 30.00,"Prodotto5": 12.99, "Prodotto6": 8.49, "Prodotto7": 25.00},
            'Telefonate':{"Settimana1": 50,  "Settimana2": 45}}

json_creato = json.dumps(dizionario, indent=4)
fout= open('es_lezione11.json','w')
fout.write(json_creato)
fout.close()


