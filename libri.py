catalogo = []
libriprestati = []

def aggiuntalibro():
    titolo = input("Come si chiama il Libro?")
    if titolo in catalogo:
        print("Lo abbiamo già")
    else:
        catalogo.append(titolo)
        print("il tuo libro chiamato", titolo, "è stato aggiunto al catalogo" )
        print("Catalogo:", catalogo)

def prestitolibro(titolo):
    if titolo in catalogo:
        catalogo.remove(titolo)
        libriprestati.append(titolo)
        print("libri prestati: ", libriprestati)
        print("catalogo: ", catalogo)
    elif titolo in libriprestati:
        print("Attualmente non è disponibile, è in prestito")
    else:
        print("non lo abbiamo")

def riportalibro(titolo):
    if titolo in libriprestati:
        libriprestati.remove(titolo)
        catalogo.append(titolo)
        print("Hai riportato il libro chiamato", titolo, ", è stato aggiunto al catalogo" )
        print(catalogo)
    else:
        ("Questo libro non è nostro, però se vuoi puoi comunque lasciarcelo")

def disponibilelibro(titolo):
    if titolo in catalogo:
        print("Lo abbiamo")
    elif titolo in libriprestati:
        print("Attualmente non è disponibile, ma tornerà presto")     
    else:
        print("Non lo abbiamo mi dispiace")


    



    