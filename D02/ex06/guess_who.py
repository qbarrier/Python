import requests
import argparse
import sys


"""
Parse Arg 
-C          -H          -T          -t
--color     --habitat   --type1     --type2
"""
def ft_parsearg() :
    parser = argparse.ArgumentParser()
    parser.add_argument('-C', '--color',  help='pokemon color', type=str)
    parser.add_argument('-H', '--habitat',  help='pokemon habitat', type=str)
    parser.add_argument('-T', '--type1',  help='pokemon type', type=str)
    parser.add_argument('-t', '--type2',  help='second pokemon type', type=str)
    args = parser.parse_args()
    return(args)


"""
Request then return list for -C and -H
"""
def ft_makelist(word) :
    req = requests.get("https://pokeapi.co/api/v2/" + word)
    if (req.status_code != 200) :
        print ("Error" , req.status_code, req.reason, "Bad value in", word)
        quit()
    req = req.json()
    list_res = []
    for x in req['pokemon_species'] :
        list_res.append(str(x['name']))
    return(list_res)



"""
Request then return list for -t and -T
"""
def ft_makelist_type(word) :
    req = requests.get("https://pokeapi.co/api/v2/" + word)
    if (req.status_code != 200) :
        print ("Error" , req.status_code, req.reason, "Bad value in", word)
        quit()
    req = req.json()
    list_res = []
    for x in req['pokemon'] :
        list_res.append(str(x['pokemon']['name']))
    return(list_res)


"""
Fusion fonction
"""
def ft_intersection(lst1, lst2): 
    lst3 = [value for value in lst1 if value in lst2] 
    return (lst3)


"""
Display if first Gen
"""
def ft_display(list_start) :
    req = requests.get('https://pokeapi.co/api/v2/pokemon/?limit=150')
    req = req.json()
    list_first_gen = []
    for x in req['results'] :
        list_first_gen.append(x['name'])
    list_final = ft_intersection(list_start, list_first_gen)
    for x in list_final :
        print(x)

"""
FIRST FUNCTION
"""
def ft_guess(argv) :
    if len(sys.argv) < 2 :
        print("Need arguments, try -h")
        quit()
    info = ft_parsearg()

    '''GET DATA'''

    if info.color :
        list_start = list_color = ft_makelist("pokemon-color/" + info.color)
    if info.habitat :
        list_start = list_habitat = ft_makelist("pokemon-habitat/" + info.habitat)
    if info.type1 :
        list_start = list_type1 = ft_makelist_type("type/" + info.type1)
    if info.type2 :
        list_start = list_type2 = ft_makelist_type("type/" + info.type2)

    '''FUSION'''

    if info.type2 :
        list_start = ft_intersection(list_start, list_type2)
    if info.type1 :
        list_start = ft_intersection(list_start, list_type1)
    if info.habitat :
        list_start = ft_intersection(list_start, list_habitat)
    if info.color :
        list_start = ft_intersection(list_start, list_color)

    '''DISPLAY'''

    ft_display(list_start)
    #print(list_start)

if __name__ == '__main__' :
    ft_guess(sys.argv)
