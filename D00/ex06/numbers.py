f = open("numbers.txt", "r")
numbers = f.read().replace("\n", "")

for x in numbers.split(",") :
    print(x)
f.close()
