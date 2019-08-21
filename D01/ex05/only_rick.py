import json
f = open("rick_and_morty.json", "r")
f_OR = open("only_rick.json", "w")
texte = json.loads(f.read())
index = 0
list_Rick = []
new_json = (dict)

while index < len(texte) :
    if "Rick" in texte[index]['summary'] and not "Morty" in texte[index]['summary'] :
        index += 1
    elif "Rick" in texte[index]['name'] and not "Morty" in texte[index]['name'] :
        index += 1
    else :
        list_Rick.append(index)
        index +=1
"""
y = ""
for x in list_Rick :
    if y == "" :
        y = json.dumps(x)
    else :
        y = y + json.dumps(x)
"""
list_Rick.reverse()

index = 0
for x in list_Rick :
    del(texte[x])

f_OR.write("%s\n" % json.dumps(texte))

