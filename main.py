from libri import *
while True:
    print("-------------------------------------------------------------")
    print("Benvenuti in libreria")
    print("1 - Aggiungi un Libro")
    print("2 - Prendi un libro in prestito")
    print("3 - Riporta un libro")
    print("4 - Controlla disponbibilità di un Libro")
    print("5 - Lista dei libri disponibili")
    print("6 - Libri attualmente non disponibili (in prestito)")
    print("0 - Niente")

    scelta = int(input("Cosa vorresti fare? "))

    if scelta == 1:
        aggiuntalibro()

    elif scelta == 2:
        titolo = input("Che libro vuoi prendere in prestito?") 
        prestitolibro(titolo)
    
    elif scelta == 3:
        titolo = input("Che libro vuoi riportare?")
        riportalibro(titolo)
    
    elif scelta == 4:
        titolo = input("Che libro stai cercando?")
        disponibilelibro(titolo)

    elif scelta == 5:
        print(catalogo)

    elif scelta == 6:
        print(libriprestati)
        
    elif scelta == 0:
        print("Grazie di aver utilizzato il nostro gestionale")

    else:
        print("Scegli un numero da 0 a 6")
    



