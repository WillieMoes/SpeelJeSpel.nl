import random


def kies_woord(bestand): #Functie voor de woordenlijst
    with open(bestand, 'r') as f:
        woordenlijst = [woord.strip() for woord in f.readlines() if woord.strip()]
    return random.choice(woordenlijst)


def galgje(): #Functie voor het spel zelf
    woord = kies_woord('woorden.txt')
    geraden_letters = []
    foute_letters = []
    max_fouten = 6
    pogingen = 0

    print("Welkom bij Galgje!")

    while pogingen < max_fouten:
        voortgang = ''.join([letter if letter in geraden_letters else '_' for letter in woord]) #Dit is voor de streepjes per letter
        print(f"Woord: {voortgang}")
        print(f"Foute letters: {' '.join(foute_letters)}")
        print(f"Overige pogingen: {max_fouten - pogingen}")

        gok = input("Raad een letter: ").lower()

        if len(gok) != 1 or not gok.isalpha(): #Dummyproof
            print("Voer alstublieft één geldige letter in.")
            continue

        if gok in geraden_letters or gok in foute_letters: #Foute letters
            print("Je hebt deze letter al geraden. Probeer een andere letter.")
            continue

        if gok in woord: #Goede letter
            geraden_letters.append(gok)
            print(f"Goed! De letter '{gok}' zit in het woord.")
        else:
            foute_letters.append(gok)
            pogingen += 1 #Een poging minder bij een verkeerde letter
            print(f"Helaas, de letter '{gok}' zit niet in het woord.")

        if all(letter in geraden_letters for letter in woord): #Als het woord is geraden
            print(f"Gefeliciteerd! Je hebt het woord '{woord}' geraden!")
            break
    else:
        print(f"Helaas, je hebt verloren! Het juiste woord was '{woord}'.") #Bij te veel fouten


if __name__ == "__main__":
    galgje()