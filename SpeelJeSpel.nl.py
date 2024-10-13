from Nummerraden import raden2 #Spel nummerraden
from Galgje import galgje #Spel galgje
import random

def main_menu(): #Dt zorgt ervpoor dat je na een spel weer terug komt in het keuzemenu
    print('===== Welkom bij SpeelJeSpel.nl ======')
    naam = input('Wat is uw gebruikersnaam?\n-  ')
    while True:
        try:
            leeftijd = int(input(f'Hallo {naam}, wat is uw leeftijd?\n-  '))
            if leeftijd < 12 or leeftijd > 99:
                print('Helaas, u voldoet niet aan de leeftijdsgrens voor deze games.\nU kunt wel verder spelen, maar het wordt niet aangeraden. ')
            else:
                print('U bent oud genoeg om dit te spelen! ')
            break #Zorgt ervoor dat je niet in de leeftijdsloop blijft zitten en je gaat nu verder naar het keuzemenu
        except ValueError: #Dummyproof
            print("Ongeldige invoer. Voer een getal in.")

    while True:
        game = input('Welke game wilt u spelen?\nU kunt kiezen uit Nummerraden & Galgje:\n-  ').lower() #Invullen van het gekozen spel

        if game == 'nummerraden':
            print('Welkom bij het nummerraad spel!\n=== Lees hier voor de uitleg van het spel. ===\n- Onder deze uitleg staat "Raad het nummer van 1 tot 20". Achter deze zin kunt u een nummer invullen.\n- Wanneer het nummer goed is geraden, dan heeft u gewonnen. Anders kunt u opnieuw proberen het getal te raden.')
            raden2()

        elif game == 'galgje':
            print('Welkom bij Galgje!\n=== Lees hier voor de uitleg van het spel. ===\n- Onder deze uitleg staat "Welkom bij galgje" en dan het woord in _.\n- Vul elke keer 1 letter in, als de letter in het woord zit, komt die op de lijn te staan. Zo niet, dan gaat er 1 poging weg.')
            galgje()

        else:
            print("Ongeldige keuze. Probeer het opnieuw.")

        opnieuw = input("Wilt u opnieuw spelen? (ja/nee)\n-  ").lower() #Na het einde van een spel is dit de keuze voor een nieuw spel ja of nee
        if opnieuw != 'ja':
            print("Bedankt voor het spelen op SpeelJeSpel.nl en tot ziens!")
            break


if __name__ == "__main__":
    main_menu()