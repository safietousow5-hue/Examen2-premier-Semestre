students = [
    ("Ali", 12),
    ("Fatou", 17),
    ("Moussa", 9),
    ("Awa", 14),
    ("Ibrahima", 7)
]

# affiche les etudiants avec leur note
print("===== Liste des Etudiants =====")
for nom, note in students:
    print(nom, ":", note)
print()
# La moyenne de la classe
somNote = 0
for nom, note in students:
    somNote =somNote + 1
moy = somNote / len(students)
print("La moyenne de la classe est : ", moy)

# La note maximale
MaxNote = 0
for nom, note in students:
    if note > MaxNote:
        MaxNote = note
print("La note maximale est :", MaxNote)

# La note minimale 
MinNote = 0
for nom, note in students:
    if note < MinNote:
        MinNote = note
print("La note minimale est :", MinNote)

print()

# liste etudiants admis
print("la liste des etudiants admis est :")
for nom, note in students:
    if note >= 10:
        print(nom, ":", note)
print()

# liste etudiants ajournes
print("la liste des etudiants ajournes est :")
for nom, note in students:
    if note < 10:
        print(nom, ":", note)
print()

# une liste contenant unkiquement les noms des etudiants admis triee par ordre aplphabetique
nomsAdmis = []
for nom, note in students:
    note >= 10
    nomsAdmis.append(nom)

nomsAdmis.sort()

print("le nom des etudiants admis par ordre alphabetique")
for nom in nomsAdmis:
    print(nom)

