def voyelles(chaine):
    voyelles = "aeiou"
    p = [i for i in chaine if i.casefold() in voyelles]
    return "".join(p)

print(voyelles("Bonjour le monde !"))

#out: ooueoe
