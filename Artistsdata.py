import TMdataRYAN

artists=['Post Malone', 'Drake',  'Childish Gambino', 'Imagine Dragons', 'Cardi B',
'Shinedown', 'Leon Bridges']

masterlist={}
for i in range(0,len(artists)):
    dict=TMdataRYAN.eventer(artists[i])
    print type(masterlist)
    masterlist.update(dict)
