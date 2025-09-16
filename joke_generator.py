#RQ : Truc intéréssant avec Git : Dernière fois on avait fait le lien entre un repository Github et le dossier Michou sur le bureau cf fichier 1
#Mtn dans le menu "source et controle" on a accès a l'historique des modifs du fichiers en local (On voit les modifs en local, sur github, les push...)


#Comprendre branches Git, possibilité de travailler en parallèle.
#RQ : POSSIBLE DE FAIRE LE PULL ET PUSH DIRECTEMENT DEPUIS VS CODE APRES AVOIR CLONE VIA GIT :
#CF ICONES DANS SOURCE ET CONTROLE PETIT ROND AVEC FLECHES
#RQ IMPORTANT : SI ON TRAVAILLE EN LOCAL LAUTRE A PAS ACCCES A NOS MODIFS (OU IL LES A SUR GITHUB SI ON A PULL ET PUSH)
#POUR AVOIR ACCES AUX FICHIERS MODIFIES PAR L'AUTRE EN LOCAL, EXECUTER "git pull" DANS TERMINAL, PUIS "ls" CA MET TT A JOUR

#EXOS 4 ET 5

#EXOS 5BIS


import random

# Programming jokes collection
programming_jokes = [
    "Pourquoi les développeurs préfèrent le mode sombre ? Parce que la lumière attire les bugs !",
    "Combien de développeurs faut-il pour changer une ampoule ? Aucun, c'est un problème hardware.",
    "Pourquoi les développeurs Java portent des lunettes ? Parce qu'ils ne peuvent pas C# !"
]

# Dad jokes collection (blagues de papa)
dad_jokes = [
    "Que dit un escargot quand il croise une limace ? Regarde le nudiste !",
    "Comment appelle-t-on un chat tombé dans un pot de peinture le jour de Noël ? Un chat-mallow !",
    "Que dit un crocodile qui surveille la pharmacie ? Lacoste garde !",
    "Pourquoi les poissons n'aiment pas jouer au tennis ? Parce qu'ils ont peur du filet !",
    "Comment appelle-t-on un boomerang qui ne revient pas ? Un bâton !",
    "Que dit un pingouin quand ça ne va pas ? J'ai le cafard !",
    "Pourquoi les plongeurs plongent-ils toujours en arrière ? Parce que sinon, ils tombent dans le bateau !"
]

def print_random_joke(category="MIXTE"):
    """Print a random joke from the selected category."""
    if category == "PROGRAMMATION":
        jokes = programming_jokes
    elif category == "PAPA":
        jokes = dad_jokes
    else:  # MIXTE ou autre
        jokes = programming_jokes + dad_jokes
    
    joke = random.choice(jokes)
    print(f"[{category}] 😂 {joke}")

if __name__ == "__main__":
    print("Bienvenue au Générateur de Blagues !")
    print("🖥️ Blagues de programmation ET 👨 Blagues de papa !")
    print("\nExemples des différentes catégories :")
    print_random_joke("PROGRAMMATION")
    print_random_joke("PAPA")
    print_random_joke("MIXTE")

#ETAPE 1
#1 Commit and push to GitHub
#2 JUSTE FAIRE UN PULL ET PUSH DANS LES ICONES

#Share repo URL with Person B
#SIMPLE

#ETAPE 2 
#1 Juste se mettre dans le bon dossier via terminal et executer git switch -c add-dad-jokes
#2 On modifie le code : On ajoute après les blagues de progra des blagues de Papa et on modifie la fonction print_random_joke():
#joke = random.choice(jokes)  devient joke = random.choice(jokes)

#3 ET 4 : ON SAUVEGARDE ET EXECUTE git add joke_generator.py
#git commit -m "Add dad jokes collection and combine with programming jokes"
#git push origin add-dad-jokes

#JEXECUTE git switch main
#git merge add-dad-jokes
#git push origin main
#LE CONFLIT APPARAIT : EXPLICATION 

#Pourquoi Git est confus ? 🤔

#Ligne identique modifiée : La signature de la fonction (def print_random_joke() vs def print_random_joke(category=...))
#Contenu complètement différent : Une version combine des listes, l'autre ajoute des catégories
#Git dit : "Je ne sais pas laquelle des deux versions tu veux garder !"


#ETAPE 3
#1 executer git switch main
#git merge add-dad-jokes
#git push origin main

#ALLER VOIR PULL REQUEST GITHUB ET RESOUDRE VIA SOLUTION CLAUDE QUI RETIRE LE CONFLIT EN CLIQUANT SUR RESOLVE CONFLICT ET MODIFIER SUR VS CODE