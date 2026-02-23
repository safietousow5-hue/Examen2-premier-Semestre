phrase = input("entrez une phrase : ")
phrase_minuscule = phrase.lower()
list_mots = phrase_minuscule.split()

## =======Affichage========##
    # Nombre total de mots 
nbr_mots = len(list_mots)
print("le nombre total de mots est de :", nbr_mots)

# le mot le plus long
motLong = ""
for mot in list_mots:
    if len(mot) > len(motLong):
        motLong = mot
print("le mot le plus long est : ", motLong)

# Nombre de voyelles 
voyelle = "ioeauy"
nbrVoyelle = 0
for lettre in phrase_minuscule:
    if lettre in voyelle:
        nbrVoyelle = nbrVoyelle + 1
print("Le nombre total de voyelles dans la phrase est :", nbrVoyelle)

#construire une nouvelle phrase :
    #Convertir les mots de longueur paire en majuscule
newPhrase = input("Entrez une nouvelle phrase : ")
for mot in list_mots:
    if len(mot) % 2 == 0:
        motMaj = mot.upper()
        newPhrase = newPhrase + motMaj + " "
    else:
        newPhrase = newPhrase + mot + " "
print("Nouvelle phrase :", newPhrase)