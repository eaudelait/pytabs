notes = {"maths": 11, "francais": 13, "anglais": 16, "histoire":6}

nom = None
note = 0

for m, n in notes.items():
    if n > a:
        nom = m
        note = n

print(str(note) + " " + nom)
