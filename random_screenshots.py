import random
from colorama import Fore
import string
import os

# SOON : YOU WILL BE ABLE TO SAVE THE LINK GENERATED !
# Bientôt : Vous pourrez enregistrer les liens dans un fichier texte
print(Fore.GREEN + "Bienvenue dans le chercheur de screenshots aléatoire en ligne ! ")
print(Fore.GREEN + "Welcome in the random screenshots searcher online ! ")
lancement = input(Fore.YELLOW + "Voulez-vous vraiment lancer le générateur de screenshots ? (Oui/Non) : ")
stock = input(Fore.LIGHTBLUE_EX + "Voulez-vous enregistrer les liens générés dans un fichier texte? (Oui/Non) ")
name_Stock = input('Comment voulez vous appeler le fichier de stockage ? ')
if lancement == str("Non"):
    exit()
while lancement == str("Oui"):
    char_list = string.ascii_letters
    second_char_list = string.ascii_letters
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for num in range(6):
        Random_Char = random.choice(char_list)
        Second_Random_Char = random.choice(char_list)
        Random_Num = random.choice(num_list)
        Second_Random_Num = random.choice(num_list)
        Third_Random_Num = random.choice(num_list)
        link = str("https://prnt.sc/")
        print(f"{link}{Random_Char}{Second_Random_Char}{Random_Num}{Second_Random_Num}{Third_Random_Num}")
        # full_Link = str(link) + Random_Char + Second_Random_Char + int(Random_Num) + int(Second_Random_Num) + int(Third_Random_Num)
        if stock == str("Oui"):
            file = open(name_Stock+".txt", "w+")
            file.write(f'Lien : {link+Random_Char+Second_Random_Char+str(Random_Num)+str(Second_Random_Num)+str(Third_Random_Num)}')
            file.close()

