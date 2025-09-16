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