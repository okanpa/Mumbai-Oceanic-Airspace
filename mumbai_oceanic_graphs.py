#Mumbai Oceanic Airspace Graph
#Here a graph is created by manually defining the neighbours of each waypoint
#to efficiently visualise connections and to become familiar with the map

# DATA FROM EAIP INDIA
map = {}
### NON CROSSING ROUTES

#P574
map["TOTOX"]=["BOLIS"]
map["BOLIS"]=["TOTOX","ADPOP"]
map["ADPOP"]=["BOLIS","BISET"]
map["BISET"]=["ADPOP","BBB","DARMI","LEGEN"]#P751
map["DARMI"]=["BISET","BBB","GUNDI","MEPAT"]#G450
map["GUNDI"]=["DARMI","BBB","ERVIS","NINOB"]#B459
map["ERVIS"]=["GUNDI","BBB","OKILA","OPIRA"]#A474
map["OKILA"]=["UDULO"]
map["UDULO"]=["OKILA"]

#N563
map["REXOD"]=["KATBI"]
map["KATBI"]=["REXOD","LEGEN"]
map["LEGEN"]=["KATBI","BISET","MEPAT","LEAMX"]#P751
map["MEPAT"]=["LEGEN","DARMI","NINOB","MESAN"]#G450
map["NINOB"]=["MEPAT","GUNDI","OPIRA","NITIX"]#B459
map["OPIRA"]=["NINOB","ERVIS","KAKIB","OSUPI","OSIRI"]#A474
map["KAKIB"]=["OPIRA","NOBOD"]
map["NOBOD"]=["KAKIB"]

#M300
map["LOTAV"]=["KADOL"]
map["KADOL"]=["LOTAV","LEMAX"]
map["LEMAX"]=["KADOL","LEGEN","MESAN","LADIB"]#P751
map["MESAN"]=["LEMAX","MEPAT","NITIX","METIP"]#G450
map["NITIX"]=["MESAN","NINOB","OSIRI","NIVUD"]#B459
map["OSIRI"]=["NITIX","OPIRA","VASTU","OTABI"]#A474
map["VASTU"]=["OSIRI"]

#P570
map["KITAL"]=["RIGLO","BOLUR","TEGOR"]
map["TEGOR"]=["KITAL","LADIB"]
map["LADIB"]=["TEGOR","LEMAX","METIP","BOLUR"]#P751
map["METIP"]=["LADIB","MESAN","NIVUD","DONSA"]#G450
map["NIVUD"]=["METIP","NITIX","OTABI","APUNA"]#B459
map["OTABI"]=["NIVUD","OSIRI","OLNIK","GOKUM"]#A474
map["OLNIK"]=["OTABI","BEDIL","POMAN","GOKUM"]
map["POMAN"]=["OLNIK"]

#L894

map["RIGLO"] = ["MAMIG","BOLUR","UNRIV","KITAL"]
map["BOLUR"] = ["ASPUX","DONSA","LADIB","KITAL","RIGLO"]

map["MAMIG"] = ["ANGAL","RIGLO","ASPUX","DONSA"]
map["UNRIV"] = ["ORLID","VUTAS","DONSA"]


