f = open("groceries.txt", "a")

print("Qu'ajouter a la liste de course ?")
add = input()
f.write("%s\n" % add)
add = ""
while (add != "no") :
    print("Anything else ?")
    add = input()
    if (add != "no") :
        f.write("%s\n" % add)
f.close()
