f = open("ten_thousand.txt", "w")
for index in range(10000) :
    f.write("%d," % index)
f.write("10000")
