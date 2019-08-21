def find_factorial(nomber):
    if nomber == 0 :
        return(0)
    fact = range(1, nomber + 1)
    res = 1
    for x in fact :
        res = res * x
    return (res)


if __name__ == '__main__':
    import sys
    if len (sys.argv) != 2 :
        print("Error need ONE arg")
    elif not sys.argv[1].isdigit() :
        print("Bad arg" , sys.argv[1])
    else :
        res = find_factorial(int(sys.argv[1]))
        print(res)
