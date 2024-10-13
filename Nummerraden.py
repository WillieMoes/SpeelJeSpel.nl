import random

def raden2(): #functie voor het nummerraad spel
    nummer = random.randrange(1, 20)
    max_kansen = 5
    kansen = 0
    while kansen < max_kansen: #Zorgt ervoor dat de kansen werken
        try:
            gok = int(input(f'Kans {kansen + 1}. Raad het nummer van 1 tot 20: '))
            kansen += 1 #na een poging komt er een kans bij
            if gok < nummer:
                print('Helaas :(, je hebt het niet goed, probeer een hoger getal.')
            elif gok > nummer:
                print('Helaas :(, je hebt het niet goed, probeer een lager getal.')
            else:
                print('Yes, je hebt het goed geraden!')
                return
        except ValueError: #Dummyproof
            print('Voer een geldig getal in!')
    print(f'Helaas, je hebt geen kansen meer over. Het juiste getal was {nummer}')
if __name__ == "__main__":
    raden2()