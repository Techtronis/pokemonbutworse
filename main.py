import random

#Déclaration de variables tels que les pokemons, vies, attaques etc...
defaultPokemons = ["Pikachu", "Salamèche", "Carapuce"]
otherPokemons = ["Chenipan", "Aspicot", "Piafabec", "Rondoudou", "Rattata", "Bulbizarre"]
otherAttacks = ["Morsure", "Claque", "Griffure"]
noms = ["Joan", "Diego", "Arianit", "Thomas", "Hugo", "André", "Antonin"]
enemyHP = 60
hp = 60
potions = 1
attacks = []
attackDamage = [20, 10, 15]

#Route
def road():
    enemyUser = noms[random.randint(0, len(noms)-1)]
    enemyPokemon = otherPokemons[random.randint(0, len(otherPokemons)-1)]
    global hp
    global enemyHP
    enemyHP = 60
    global potions
    print(f"Tu rencontres {enemyUser} et il utilise {enemyPokemon}")
    print(f"{enemyPokemon} à {enemyHP}HP, Tu as {hp}HP")
    battleOn = True
    #Rencontre avec l'enemy
    while(battleOn and hp > 0):
        #Choix de combat -> choix d'attaques
        battleChoice = int(input(f"Que veux-tu faire? (1) Attaquer | (2) Objets | (3) Fuir "))
        enemyChoice = int(attackDamage[random.randint(0, len(attackDamage)-1)])
        if enemyHP > 0 or hp > 0:
            if battleChoice == 1:
                attackChoice = int(input(f"Quelle attaque ? (1) {attacks[0]} | (2) {attacks[1]} | (3) {attacks[2]} "))-1
                enemyHP -= attackDamage[attackChoice]
                print(f"Tu lances {attacks[attackChoice]}. Il reste {enemyHP}HP au {enemyPokemon} enemy.")
                hp -= enemyChoice
                print(f"{enemyPokemon} lance {otherAttacks[attackChoice]}. Il reste {hp} à ton {mainPokemon}")
            elif battleChoice == 2:
                if potions > 0:
                    hp = 60
                    print("Tu as bu une potion, tu es maintenant guérit.")
                    potions = potions - 1
                else:
                    print("Tu n'as plus de potions. Tu peux en acheter au magasin après ce combat.")
            else:
                print("Tu ne peux pas t'enfuir quand tu combats un entraineur.")
        #décés du pokemon
        if hp <= 0 or enemyHP <= 0:
            if hp <= 0:
                print("Tu es mort. Ton pokémon va étre envoyé à l'hopital.")
                hp = 60
            else:
                print(f"Le {enemyPokemon} enemy est mort.")
                enemyHP = 60
            battleOn = False
            location()
#Hautes herbes
def grass():
    enemyPokemon = otherPokemons[random.randint(0, len(otherPokemons)-1)]
    global hp
    global enemyHP
    global potions
    print(f"Tu rencontres {enemyPokemon}")
    print(f"{enemyPokemon} à {enemyHP}HP, Tu as {hp}HP")
    battleOn = True

    while(battleOn and hp > 0):
        #Choix de combats
        battleChoice = int(input(f"Que veux-tu faire? (1) Attaquer | (2) Objets | (3) Fuir "))
        enemyChoice = int(attackDamage[random.randint(0, len(attackDamage)-1)])
        if enemyHP > 0 or hp > 0:
            if battleChoice == 1:
                attackChoice = int(input(f"Quelle attaque ? (1) {attacks[0]} | (2) {attacks[1]} | (3) {attacks[2]} "))-1
                enemyHP -= attackDamage[attackChoice]
                print(f"Tu lances {attacks[attackChoice]}. Il reste {enemyHP}HP au {enemyPokemon} enemy.")
                hp -= enemyChoice
                print(f"{enemyPokemon} lance {otherAttacks[attackChoice]}. Il reste {hp} à ton {mainPokemon}")
            #Potions
            elif battleChoice == 2:
                if potions > 0:
                    hp = 60
                    print("Tu as bu une potion, tu es maintenant guérit.")
                    potions = potions - 1
                else:
                    print("Tu n'as plus de potions. Tu peux en acheter au magasin après ce combat.")
            else:
                print("Tu t'enfuis.")
                location()
            #Décés du pokémon
        if hp <= 0 or enemyHP <= 0:
            if hp <= 0:
                print("Tu es mort. Ton pokémon va étre envoyé à l'hopital.")
                hp = 60
            else:
                print(f"Le {enemyPokemon} enemy est mort.")
                enemyHP = 60
            battleOn = False
            location()
#Ville
def city():
    global potions
    global hp
    #Choix de lieu
    locChoice = int(input("Où veux tu aller? (1) Hôpital | (2) Le magasin | (3) Quitter la ville "))
    #hopital
    if locChoice == 1:
        print("Tu vas à l'hôpital, ton pokémon est guérit.")
        hp = 60
        location()
        #magasin pour potions
    elif locChoice == 2:
        answer = int(input("Tu vas au magasin, combien de potions veux-tu? (max 2) "))
        if answer <= 2:
            potions += answer
            print(f"Tu as reçu {answer} potions")
            city()
        else:
            print("Tu peux en prendre 2 au max")
            city()
    #retour au choix de lieu
    elif locChoice == 3:
        location()
#choix des lieux
def location():
    locChoice = int(input("Où veux tu aller? (1) La route | (2) Les hautes herbes | (3) La ville "))
    if locChoice == 1:
        road()
    elif locChoice ==2:
        grass()
    elif locChoice == 3:
        city()

#Début du jeu
pokemonChoice = int(input("Quel Pokémon veux-tu? (1) Pikachu | (2) Salamèche | (3) Carapuce " )) - 1
mainPokemon = defaultPokemons[pokemonChoice]
playerPokemons.append(mainPokemon)
print(f"Tu as choisi {mainPokemon}")

if mainPokemon == "Pikachu":
    attacks.extend(["éclair", "Griffure", "Electrocution"])
elif mainPokemon == "Salameche":
    attacks.extend(["Flamme", "Griffure", "Brulure"])
elif mainPokemon == "Carapuce":
    attacks.extend(["Noyade", "Griffure", "Jet d'eau"])

print(f"Les attaques sont {attacks[0]}, {attacks[1]} et {attacks[2]}")
location()