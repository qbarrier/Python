dates = [
        ('Alan Turing' , '1912'),
        ('Ada Lovelace' , '1815'),
        ('Tim Berners-Lee' , '1955'),
        ('Grace Hopper' , '1906'),
        ('Denis Ritchie' , '1941'),
        ('Richard Stallman' , '1953'),
        ('Guido van Rossum' , '1956'),
        ('Radia Perlman' , '1951'),
        ('Larry Page' , '1973'),
        ('Mary Kenneth Keller' , '1913'),
        ('Dorothy Vaughan' , '1910'),
        ('Annie Easley' , '1933'),
        ('Ian Murdock' , '1973'),
        ('Carol Shaw' , '1955'),
        ('Aaron Swartz' , '1986'),
        ('Hedy Lamarr' , '1914'),
        ('Katherine Johnson' , '1918'),
        ('Jimmy Wales' , '1966'),
        ('Jean E. Sammet' , '1928'),
        ('Charles Babbage' , '1791'),
        ('Margaret Hamilton', '1936'),
        ('Vint Cerf' , '1943'),
]

print("Bonjour, Vous cherchez la date de naissance d'une personnalite ? Laquelle ?")
name = input().lower()
index = 0

for x in dates :
    if x[0].lower() == name :
        print(x[0], "est ne(e) en", x[1])
        index += 1
if index == 0 :
    print ("Personnalite inconnue")
