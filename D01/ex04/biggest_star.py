import json
f = open("rick_and_morty.json", "r")
texte = json.loads(f.read())

Rick = 0
Morty = 0
R_M = 0
index = 0

list_RM = []
list_Morty = []
list_Rick = []


while index < len(texte) :
    if "Rick" in texte[index]['summary'] and "Morty" in texte[index]['summary'] :
        R_M += 1
        list_RM.append(texte[index]['name'])
    elif "Morty" in texte[index]['summary'] :
        Morty += 1
        list_Morty.append(texte[index]['name'])
    elif "Rick" in texte[index]['summary'] :
        Rick += 1
        list_Rick.append(texte[index]['name'])
    index +=1

print("Rick (%d):" % Rick)
for val_rick in list_Rick :
    print(val_rick)

print("\nMorty (%d):" % Morty)
for val_morty in list_Morty :
    print(val_morty)

print("\nRick and Morty (%d):" % R_M)
for val_rm in list_RM :
    print(val_rm)

