import TMdataRYAN
import json
import csv


artists=['Post Malone', #'Drake',  'Childish Gambino', 'Imagine Dragons', 'Cardi B',
#'Shinedown', 'Leon Bridges',
'Ed Sheeran', 'Shawn Mendes', #'Luke Combs'
'Camila Cabello', #'Kendrick Lamar', #'The Weeknd', #'Jason Aldean'
#'Lake Street Dive',
#'Bruno Mars', #'Dua Lipa',
'Taylor Swift', #'Maroon',
#'Migos',
#'Keith Urban', 'Kane Brown', #'Ariana Grande','Nicki Minaj',
'Chris Stapleton',
'Charlie Puth', #'Florida Georgia Line',
#'Khalid', #'XXXTENTACION',
#'Kenny Chesney',
#'YoungBoy Never Broke Again',
#'Thomas Rhett', #'Halsey',
#'Bazzi',
#'SZA',
#'Marshmello',
#'P!nk', 'Travis Scott',
'Justin Timberlake', 'Bebe Rexha', 'Rich The Kid', #'Demi Lovato',
'BlocBoy JB',
'Brett Young', #'Luke Bryan',
'Dan + Shay', 'Royce da' , 'Ella Mai', 'Rae Sremmurd',
'Metallica', #'Blake Shelton', #'Rihanna',
#'Eminem',
'Maren Morris'
]

masterlist={}
for i in range(0,1):#len(artists)):
    dict=TMdataRYAN.eventer(artists[i])
    masterlist.update(dict)


with open('dang.csv', 'w') as f:
    writer = csv.writer(f)
    i=0
    for key, value in masterlist.iteritems():
        i=i+1
        ln=[]
        for ik, iv in value.iteritems():
            ln.append(ik)
    writer.writerow(ln)
    for j in range(0,len(masterlist.items())):
        lan=[]
        for i in range(0,len(ln)):
            lalaa= masterlist.items()[j][1].items()[i][1]
            btr=str(lalaa)
            lan.append(btr)
        writer.writerow(lan)

    #writer.writerow(masterlist.get(ln).get(ln))
