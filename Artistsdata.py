import TMdataRYAN
import json

artists=['Post Malone', 'Drake',  'Childish Gambino', 'Imagine Dragons', 'Cardi B',
'Shinedown', 'Leon Bridges','Ed Sheeran', 'Shawn Mendes', #'Luke Combs'
'Camila Cabello', 'Kendrick Lamar', #'The Weeknd', #'Jason Aldean'
'Lake Street Dive', 'Bruno Mars', 'Dua Lipa', 'Taylor Swift', 'Maroon',
'Migos', 'Keith Urban', 'Kane Brown', #'Ariana Grande','Nicki Minaj',
'Chris Stapleton',
'Charlie Puth', 'Florida Georgia Line', 'Khalid', #'XXXTENTACION',
'Kenny Chesney',
#'YoungBoy Never Broke Again',
'Thomas Rhett', 'Halsey', 'Bazzi', 'SZA', 'Marshmello', 'P!nk', 'Travis Scott',
'Justin Timberlake', 'Bebe Rexha', 'Rich The Kid', 'Demi Lovato', 'BlocBoy JB',
'Brett Young', 'Luke Bryan', 'Dan + Shay', 'Royce da' , 'Ella Mai', 'Rae Sremmurd',
'Metallica', 'Blake Shelton', #'Rihanna',
'Eminem', 'Maren Morris'
]

masterlist={}
for i in range(0,len(artists)):
    dict=TMdataRYAN.eventer(artists[i])
    masterlist.update(dict)

with open('result.json', 'w') as fp:
    json.dump(masterlist, fp)
