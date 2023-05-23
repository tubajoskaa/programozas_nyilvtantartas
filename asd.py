with open('Nyilvantartaspy.txt','r', encoding='utf-8') as forrasfajl:
    for row in forrasfajl:
        print(row.strip().split(';'))
