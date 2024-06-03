import json
li=[{'Name':'Demian', 'kor':77, 'eng':90, 'mat':70},
    {'Name':'Catherine', 'kor':87, 'eng':99, 'mat':95},
    {'Name':'Adelia', 'kor':97, 'eng':95, 'mat':99},]

with open("/Users/Demian/Desktop/pythonproject/family_score.json",'w') as f:
    json.dump(li,f)

with open("/Users/Demian/Desktop/pythonproject/family_score.json",'r') as f:
    info=json.load(f)

print(info)

for i in info:
    for k,v in i.items():
        print(k,v)
    print('-'*30)