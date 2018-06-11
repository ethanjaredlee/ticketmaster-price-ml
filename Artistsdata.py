import TMdataRYAN
import json
import csv


artists=['Post Malone', 'Drake',
'Childish Gambino', 'Imagine Dragons', 'Cardi B',
'Shinedown', 'Leon Bridges',
'Ed Sheeran', 'Shawn Mendes', 'Luke Combs',
'Camila Cabello', 'Kendrick Lamar', 'The Weeknd', 'Jason Aldean',
#'Lake Street Dive',
'Bruno Mars', 'Dua Lipa','Taylor Swift', 'Maroon','Migos','Keith Urban',
'Kane Brown', #'Ariana Grande',
'Nicki Minaj','Chris Stapleton','Charlie Puth', 'Florida Georgia Line',
'Khalid','Kenny Chesney','YoungBoy Never Broke Again','Thomas Rhett', 'Halsey',
'Bazzi','SZA','Marshmello','P!nk', 'Travis Scott','Justin Timberlake',
'Bebe Rexha','Rich The Kid', 'Demi Lovato','BlocBoy JB','Brett Young',
'Luke Bryan','Dan + Shay', #'Royce da' ,
'Ella Mai', 'Rae Sremmurd', 'Metallica', #'Blake Shelton', #'Rihanna',
'Eminem','Maren Morris','J Balvin', 'Portugal. The Man', 'Meghan Trainor',
'Zedd','Ty Dolla $ign', 'Parkway Drive', 'Carrie Underwood', 'G-Eazy',
'Daddy Yankee', 'Lil Dicky', 'Chris Brown', 'Kanye West',
'Ozuna', 'Bad Bunny', 'NF', 'Adele', 'Kelly Clarkson',
'Janelle Monae', 'Darius Rucker', 'Godsmack', 'Grey',
'Bad Wolves', 'Foster The People', 'The Chainsmokers', 'MercyMe', 'Anne-Marie',
'Sam Smith', 'Lil Pump','Logic','Niall Horan', 'Bon Jovi', 'Lil Uzi Vert',
'Lynyrd Skynyrd', 'Dustin Lynch', 'Savage', 'Jordan Davis', 'Sam Hunt', 'Panic! At The Disco',
'Famous Dex', 'Maluma'

]

masterlist={}
for i in range(0,1):
    dict=TMdataRYAN.eventer(artists[i])
    masterlist.update(dict)


with open('dang2.csv', 'w') as f:
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
            #btr=str(lalaa)
            a=u'unicode'
            b='string'
            c=15
            if type(lalaa)==type(a):
                lan.append(lalaa.encode("utf-8"))
            elif type(lalaa)==type(b) or type(lalaa)==type(c):
                lan.append(str(lalaa))
            else:
                lan.append(str(lalaa))
        writer.writerow(lan)

    #writer.writerow(masterlist.get(ln).get(ln))
