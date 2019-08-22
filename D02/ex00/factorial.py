import sys

def find_factorial(argv):
    if len (argv) != 2 :
        print("Error need ONE arg")
    elif not argv[1].isdigit() :
        print("Bad arg" , argv[1])
    else :
        nomber = int(argv[1])
        if nomber == 0 :
            print (0)
        else :
            fact = range(1, nomber + 1)
            res = 1
            for x in fact :
                res = res * x
            print(res)

if __name__ == '__main__':
         find_factorial(sys.argv)
