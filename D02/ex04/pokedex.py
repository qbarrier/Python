import sys
import requests

def ft_pokedex(argv) :
    """
    Error Tests
    """
    if len (argv) != 2 :
        print("Error need ONE arg")
        quit()
    pokemon = requests.get('https://pokeapi.co/api/v2/pokemon/' + argv[1])
    if (pokemon.status_code != 200) :
        print("Error :" , pokemon.status_code , pokemon.reason)
        quit()
    '''
    Types
    '''
    pokemon = pokemon.json()
    print(argv[1])
    print("\nType(s) :")
    for x in pokemon['types']:
        print("\t", x['type']['name'])
    '''
    Abilities
    '''
    print("\n" , len(pokemon['abilities']), " Abilities :", sep='')
    for x in pokemon['abilities']:
        print("\t", x['ability']['name'])
    '''
    Moves
    '''
    print("\n" , len(pokemon['moves']), " Moves :", sep='')

    list_moves = []
    for x in pokemon['moves']:
        list_moves.append(x['move']['name'])
   #     print("\t", x['move']['name'])
    list_moves = sorted(list_moves)
    for x in range(5) :
        print("\t" + list_moves[x])
    print("\t...")


if __name__ == '__main__':
    ft_pokedex(sys.argv)
