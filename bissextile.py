annee = input("tape l'année :")
annee = int(annee)
if annee %400 ==0 or (annee % 100 != 0  and annee % 4 == 0):
    print("bissextile")
else:
    print("non bissextile")