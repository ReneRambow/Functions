def printTafel(TafelVan):
    for i in range(1,11):
        print(f'{i} x {TafelVan} = {i*TafelVan}')

getalvraag = int(input("Welke tafel wilt u weten?"))

printTafel(getalvraag)