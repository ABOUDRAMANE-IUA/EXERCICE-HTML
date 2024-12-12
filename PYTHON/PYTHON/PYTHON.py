import random

# Base des questions (nom de la région et son chef-lieu)
questions = {
    "Abidjan": "Abidjan",
    "Bélier": "Yamoussoukro",
    "Haut-Sassandra": "Daloa",
    "Lagunes": "Abidjan",
    "Marahoué": "Bouaflé",
    "Montagnes": "Man",
    "Sassandra": "San Pedro",
    "Vallée du Bandama": "Bouaké",
    "Woroba": "Séguéla",
    "Zanzan": "Bondoukou"
}

# Fonction pour poser une question
def poser_question(region, reponse_correcte):
    print(f"Quel est le chef-lieu de la région {region}?")
    reponse_joueur = input("Réponse: ").strip()
    
    if reponse_joueur.lower() == reponse_correcte.lower():
        print("Bonne réponse!")
        return True
    else:
        print(f"Mauvaise réponse. La bonne réponse est {reponse_correcte}.")
        return False

# Fonction principale du jeu
def jouer_partie():
    print("Bienvenue dans le jeu du découpage administratif de la Côte d'Ivoire!")
    
    # Mélanger les régions pour poser des questions différentes
    regions = list(questions.keys())
    random.shuffle(regions)
    
    score = 0
    for i in range(5):  # On pose 5 questions
        region = regions[i]
        reponse_correcte = questions[region]
        
        if poser_question(region, reponse_correcte):
            score += 10  # 10 points par bonne réponse
    
    # Affichage du score final
    print(f"\nVotre score final est {score} points.")

# Lancer une partie du jeu
if __name__ == "__main__":
    jouer_partie()

