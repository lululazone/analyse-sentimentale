from thefuzz import fuzz


def create_word_list(filename):
    # Ouvrez le fichier en lecture
    with open(filename, 'r') as f:
        # Lisez le contenu du fichier
        text = f.read()

    # Divisez le contenu du fichier en mots individuels
    words = text.split()

    # Renvoyez la liste de mots
    return words



def percentage_match(word1, word_list,path):
    # Initialiser un compteur à 0
    count = 0
    score = 0

    # Parcourir chaque mot de la liste
    for word2 in word_list:
      match_percentage = fuzz.ratio(word1, word2)

      if match_percentage >= 90:
        # Ouvrir le fichier en mode ajout
        if match_percentage < 100 and word_list.count(word1) == 0:
            with open(path, 'a') as f:
              # Écrire le mot dans le fichier
              print("Ajout du mot " + word1 + " dans le fichier "+path+" car il correspond à "+str(match_percentage)+"% à "+word2)
              f.write(word1+'\n')
              score =1 
        return score
    return 0















# Testez la fonction en créant une liste de mots à partir d'un fichier texte




list_input = open("input.txt", "r")

# Ouvrez le fichier en lecture

with open("input.txt", "r") as f:
    # Lisez le contenu du fichier
    text = f.read()

# Divisez le contenu du fichier en mots individuels
words = text.split()
#supprimer les caractères spéciaux et les chiffres
words = [word for word in words if word.isalpha()]





for word in words:
    good_list = create_word_list('EmotionDictionnary/good.txt')
    love_list = create_word_list('EmotionDictionnary/love.txt')
    open_list = create_word_list('EmotionDictionnary/open.txt')
    alive_list = create_word_list('EmotionDictionnary/alive.txt')
    angry_list = create_word_list('EmotionDictionnary/angry.txt')
    depressed_list = create_word_list('EmotionDictionnary/depressed.txt')
    inspired_list = create_word_list('EmotionDictionnary/inspired.txt')
    positive_list = create_word_list('EmotionDictionnary/positive.txt')
    open_list = create_word_list('EmotionDictionnary/open.txt')
    interested_list = create_word_list('EmotionDictionnary/interested.txt')
    scoreGood = percentage_match(word, good_list, 'EmotionDictionnary/good.txt')
    scoreLove = percentage_match(word, love_list, 'EmotionDictionnary/love.txt')
    scoreOpen = percentage_match(word, open_list, 'EmotionDictionnary/open.txt')
    scoreAlive = percentage_match(word, alive_list, 'EmotionDictionnary/alive.txt')
    scoreAngry = percentage_match(word, angry_list, 'EmotionDictionnary/angry.txt')
    scoreDepressed = percentage_match(word, depressed_list, 'EmotionDictionnary/depressed.txt')
    scoreInspired = percentage_match(word, inspired_list, 'EmotionDictionnary/inspired.txt')
    scorePositive = percentage_match(word, positive_list, 'EmotionDictionnary/positive.txt')
    scoreOpen = percentage_match(word, open_list, 'EmotionDictionnary/open.txt')
    scoreInterested = percentage_match(word, interested_list, 'EmotionDictionnary/interested.txt')
positiveScore = scoreGood+scoreLove+scoreOpen+scoreAlive+scoreInspired+scorePositive+scoreOpen+scoreInterested
negativeScore = scoreAngry+scoreDepressed
globalScore = positiveScore-negativeScore

print("Good: ",scoreGood )
print("Love: ",scoreLove )
print("Open: ",scoreOpen )
print("Alive: ",scoreAlive )
print("Angry: ",scoreAngry )
print("Depressed: ",scoreDepressed )
print("Inspired: ",scoreInspired )
print("Positive: ",scorePositive )
print("Open: ",scoreOpen )
print("Interested: ",scoreInterested )
print("Positive Score: ",positiveScore )
print("Negative Score: ",negativeScore )
print("Global Score: ",globalScore )

if globalScore > 0:
    print("The paragraph is positive")

elif globalScore < 0:

    print("The paragraph is negative")

else:
    print("The paragraph is neutral")



