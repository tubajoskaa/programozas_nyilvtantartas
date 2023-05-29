from pprint import pprint
with open('Nyilvantartaspy.txt','r', encoding='utf-8') as forrasfajl:
    nevek = forrasfajl.readline().strip().split(";")
    futas = forrasfajl.readline().strip().split(";")
    sulydobas = forrasfajl.readline().strip().split(";")
    tavolugras = forrasfajl.readline().strip().split(";")
    helybol_tavolugras = forrasfajl.readline().strip().split(";")
    magasugras = forrasfajl.readline().strip().split(";")
    list = []
    for i in range(12):
        dictionary = 'diak'+str(i)
        dictionary = {
            'Név': nevek[0],
            'Futás': float(futas[0]),
            'Súlydobás': float(sulydobas[0]),
            'Távolugrás': float(tavolugras[0]),
            'Helyből_Távolugrás': float(helybol_tavolugras[0]),
            'Magasugrás': float(magasugras[0]),
        }
        del nevek[0]
        del futas[0]
        del sulydobas[0]
        del tavolugras[0]
        del helybol_tavolugras[0]
        del magasugras[0]
        list.append(dictionary)

for i in list:
    max = 0
    if max < i['Súlydobás']:
        max = i['Súlydobás']
    print(max)
