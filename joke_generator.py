#RQ : Truc intéréssant avec Git : Dernière fois on avait fait le lien entre un repository Github et le dossier Michou sur le bureau cf fichier 1
#Mtn dans le menu "source et controle" on a accès a l'historique des modifs du fichiers en local (On voit les modifs en local, sur github, les push...)


#Comprendre branches Git, possibilité de travailler en parallèle.

#EXOS 4 ET 5

#EXOS 5BIS


import random
# Initial joke collection
jokes = [
    "Pourquoi les développeurs préfèrent le mode sombre ? Parce que la lumière attire les bugs !",
    "Combien de développeurs faut-il pour changer une ampoule ? Aucun, c'est un problème hardware.",
    "Pourquoi les développeurs Java portent des lunettes ? Parce qu'ils ne peuvent pas C# !"
]

def print_random_joke():
    """Print a random joke from the collection."""
    joke = random.choice(jokes)
    
    print(f"😂 {joke}")

if __name__ == "__main__":
    print("Bienvenue au Générateur de Blagues !")
    print_random_joke()