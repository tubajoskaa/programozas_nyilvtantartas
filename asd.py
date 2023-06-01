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

#Távolugrás
max_tavolugras = 0
min_tavolugras = 100
osszeg_tavolugras = 0
for i in list:
    osszeg_tavolugras += i['Távolugrás']
    if max_tavolugras < i['Távolugrás']:
        max_tavolugras = i['Távolugrás']
    if min_tavolugras > i['Távolugrás']:
        min_tavolugras = i['Távolugrás']
print(f'A legjobb távolugrás: {max_tavolugras}')
print(f'A legrosszabb távolugrás: {min_tavolugras}')
print(f'Az összesen ugrott táv: {osszeg_tavolugras}')
print(f'Az ugrott távolugrás átlaga: {osszeg_tavolugras/len(list)}')
print('\n')

#Helyből távolugrás
max_helyboltavol = 0
min_helyboltavol = 100
osszeg_helyboltavol = 0
for i in list:
    osszeg_helyboltavol += i['Helyből_Távolugrás']
    if max_helyboltavol < i['Helyből_Távolugrás']:
        max_helyboltavol = i['Helyből_Távolugrás']
    if min_helyboltavol > i['Helyből_Távolugrás']:
        min_helyboltavol = i['Helyből_Távolugrás']
print(f'A legjobb helyből távolugrás: {max_helyboltavol}')
print(f'A legrosszabb helyből távolugrás: {min_helyboltavol}')
print(f'Az összesen helyből távolugrott  táv: {osszeg_helyboltavol}')
print(f'Az ugrott helyből távolugrás átlaga: {osszeg_helyboltavol/len(list)}')
print('\n')

#Súlydobás
max_sulydobas = 0
min_sulydobas = 100
osszeg_sulydobas = 0
for i in list:
    osszeg_sulydobas += i['Súlydobás']
    if max_sulydobas < i['Súlydobás']:
        max_sulydobas = i['Súlydobás']
    if min_sulydobas > i['Súlydobás']:
        min_sulydobas = i['Súlydobás']
print(f'A legjobb súlydobás: {max_sulydobas}')
print(f'A legrosszabb súlydobás: {min_sulydobas}')
print(f'Az összesen dobott táv: {osszeg_sulydobas}')
print(f'Az dobott súlydobások átlaga: {osszeg_sulydobas/len(list)}')
print('\n')


#Futás
max_futas = 0
min_futas = 100
osszeg_futas = 0
for i in list:
    osszeg_futas += i['Futás']
    if max_futas < i['Futás']:
        max_futas = i['Futás']
    if min_futas > i['Futás']:
        min_futas = i['Futás']
print(f'A legjobb futás: {max_futas}')
print(f'A legrosszabb futás: {min_futas}')
print(f'Az összesen futott táv: {osszeg_futas}')
print(f'Az futott távok átlaga: {osszeg_futas/len(list)}')
print('\n')


#Magasugrás
max_magasugras = 0
min_magasugras = 100
osszeg_magasugras = 0
for i in list:
    osszeg_magasugras += i['Magasugrás']
    if max_magasugras < i['Magasugrás']:
        max_magasugras = i['Magasugrás']
    if min_magasugras > i['Magasugrás']:
        min_magasugras = i['Magasugrás']
print(f'A legjobb magasugrás: {max_magasugras}')
print(f'A legrosszabb magasugrás: {min_magasugras}')
print(f'Az összesen ugrott táv: {osszeg_sulydobas}')
print(f'Az ugrott magasugrás átlaga: {osszeg_sulydobas/len(list)}')
print('\n')
