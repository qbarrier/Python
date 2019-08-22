import requests
import json

def ft_first_gen() :
    req = requests.get('https://pokeapi.co/api/v2/pokemon/?limit=150')
    req = req.json()
    dict_pk = {}
    list_pk = []
    index = 1
    for x in req['results'] :
        dict_pk = {index : x['name']}
        list_pk.append(dict_pk)
        index += 1

    f = open("the_only_true_pokemons.json", "w")
    f.write("%s\n" % json.dumps(list_pk))
    f.close()

if __name__ == '__main__':
    ft_first_gen()
