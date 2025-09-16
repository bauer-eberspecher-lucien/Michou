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
# Initial joke collection
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
    "Comment appelle-t-on un boomerang qui ne revient pas ? Un bâton !"
]

def print_random_joke():
    """Print a random joke from the collection."""
    all_jokes = programming_jokes + dad_jokes
    joke = random.choice(all_jokes)
    print(f"😂 {joke}")

if __name__ == "__main__":
    print("Bienvenue au Générateur de Blagues !")
    print_random_joke()

#ETAPE 1
#1 Commit and push to GitHub
#2 JUSTE FAIRE UN PULL ET PUSH DANS LES ICONES

#Share repo URL with Person B
#SIMPLE

#ETAPE 2 
#1 Juste se mettre dans le bon dossier via terminal et executer git switch -c add-dad-jokes
#2 On modifie le code : On ajoute après les blagues de progra des blagues de Papa et on modifie la fonction print_random_joke():
#joke = random.choice(jokes)  devient joke = random.choice(jokes)

