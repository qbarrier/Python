import sys
if len (sys.argv) < 2 :
    print ("Hey, give me at least one argument!")
else :
    arguments = sys.argv
    del arguments[0]
    for index, val in enumerate(arguments, 1) :
        print ("Argument", index, "is :", val)
    print("I have", len(arguments), "arguments")
