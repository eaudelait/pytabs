mon_tableau = ["a", "b", "c", "d"]
print(len(mon_tableau))
del mon_tableau[4]
print(mon_tableau)

# On peut confirmer que le programme ne fonctionne pas en l'essayant.
#out:
# Traceback (most recent call last):
#   File "<string>", line 3, in <module>
# ERROR!
# IndexError: list assignment index out of range
