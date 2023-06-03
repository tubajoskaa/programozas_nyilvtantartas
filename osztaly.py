from pprint import pprint
with open('Nyilvantartaspy.txt','r', encoding='utf-8') as forrasfajl:
    class Elemezes:
        def __init__(self,nev,fut,suly,tavol,helybol,magas):
            self.nev = nev
            self.fut = fut
            self.suly = suly
            self.tavol = tavol
            self.helybol = helybol
            self.magas = magas


    nevek = forrasfajl.readline().strip().split(";")
    futas = forrasfajl.readline().strip().split(";")
    sulydobas = forrasfajl.readline().strip().split(";")
    tavolugras = forrasfajl.readline().strip().split(";")
    helybol_tavolugras = forrasfajl.readline().strip().split(";")
    magasugras = forrasfajl.readline().strip().split(";")
    list = []
    for i in range(12):
        diak = Elemezes(nevek[0],futas[0],sulydobas[0],tavolugras[0],helybol_tavolugras[0],magasugras[0])
        del nevek[0]
        del futas[0]
        del sulydobas[0]
        del tavolugras[0]
        del helybol_tavolugras[0]
        del magasugras[0]
        list.append(diak)


    futas = 0
    min_futas = 100
    max_futas = 0
    sulylokes = 0
    min_sulylokes = 100
    max_sulylokes = 0
    tavol = 0
    min_tavol = 100
    max_tavol = 0
    helybol = 0
    min_helybol = 100
    max_helybol = 0
    magas = 0
    min_magas = 100
    max_magas = 0
    for diak in list:
        sulylokes += float(diak.suly)
        futas += float(diak.fut)
        tavol += float(diak.tavol)
        helybol += float(diak.helybol)
        magas += float(diak.magas)

        if min_futas > float(diak.fut):
            min_futas = float(diak.fut)
        if min_sulylokes > float(diak.suly):
            min_sulylokes = float(diak.suly)
        if min_tavol > float(diak.tavol):
            min_tavol = float(diak.tavol)
        if min_helybol > float(diak.helybol):
            min_helybol = float(diak.helybol)
        if min_magas > float(diak.magas):
            min_magas = float(diak.magas)


        if max_futas < float(diak.fut):
            max_futas = float(diak.fut)
        if max_sulylokes < float(diak.suly):
            max_sulylokes = float(diak.suly)
        if max_tavol < float(diak.tavol):
            max_tavol = float(diak.tavol)
        if max_helybol < float(diak.helybol):
            max_helybol = float(diak.helybol)
        if max_magas < float(diak.magas):
            max_magas = float(diak.magas)



    #FUTÁS
    print('\nFutás!\n')
    print('Az összesen lefutott táv:',futas)
    print('A lefutott távok átlaga:', futas/len(list))
    print('A legkevesebbet futott távolság:', min_futas)
    print('A legtöbbet futott távolság:', max_futas)
    print(f'{list[1].nev} lefutott távja: {list[1].fut}')
    print('----------------------\n')

    #SÚLYLÖKÉS
    print('Súlylökés!\n')
    print('Az összesen súlyt lökött táv:',sulylokes)
    print('A súlylökések átlaga:', sulylokes/len(list))
    print('A legkisebbet lökött távolság:', min_sulylokes)
    print('A legnagyobbat lökött távolság:', max_sulylokes)
    print(f'{list[5].nev} súlylökése: {list[5].tavol}')
    print('----------------------\n')

    #TÁVOLUGRÁS
    print('Távolugrás!\n')
    print('Az összesen ugrott táv:',tavol)
    print('Az ugrások átlaga:', tavol/len(list))
    print('A legkisebbet ugrott távolság:', min_tavol)
    print('A legnagyobbat ugrott távolság:', max_tavol)
    print(f'{list[0].nev} távolugrása: {list[0].tavol}')
    print('----------------------\n')


    #HELYBOL TAVOLUGRAS
    print('Helyből távolugrás!\n')
    print('Az összesen ugrott táv:',helybol)
    print('Az ugrások átlaga:', helybol/len(list))
    print('A legkisebbet ugrott távolság:', min_helybol)
    print('A legnagyobbat ugrott távolság:', max_helybol)
    print(f'{list[3].nev} helyből távolugrása: {list[3].helybol}')
    print('----------------------\n')

    #MAGASUGRÁS
    print('Magasugrás!\n')
    print('Az összesen ugrott magasság:',magas)
    print('Az ugrások átlaga:', magas/len(list))
    print('A legkisebb magasság:', min_magas)
    print('A legnagyobb magasság:', max_magas)
    print(f'{list[-1].nev} magasugrása: {list[-1].tavol}')
    print('----------------------\n')
    

