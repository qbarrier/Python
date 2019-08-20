import json
f = open("rick_and_morty.json","r")
texte_json = f.read()
texte = json.loads(texte_json)
print(json.dumps(texte, indent=4))
f.close()
