import sys
if len (sys.argv) != 2 :
        print ("Error, need ONE argument")
        quit()
arguments = sys.argv[1]
if not arguments.lower().endswith('.txt') :
    print("need a '.txt' file")
else :
    count = 0
    f = open(arguments, "r")
    texte = f.read()
    for x in texte :
        if x.lower() == "e" :
            count += 1
    print(count)
