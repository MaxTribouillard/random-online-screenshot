import random
from colorama import Style, Fore, Back
import string
import os

# SOON : YOU WILL BE ABLE TO SAVE THE LINK GENERATED !
# Bientôt : Vous pourrez

print(Fore.GREEN + "Bienvenue dans le chercheur de screenshots aléatoire en ligne ! ")
print(Fore.GREEN + "Welcome in the random screenshots searcher online ! ")

# stock = input(Fore.LIGHTBLUE_EX + "Voulez-vous enregistrer les liens générés dans un fichier texte? (Oui/Non) ")
# name_Stock = input('Comment voulez vous appeler le fichier de stockage ? ')
lancement = input(Fore.YELLOW + "Voulez-vous vraiment lancer le générateur de screenshots ? (Oui/Non) : ")


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
        link = Random_Char + Second_Random_Char + Random_Num + Second_Random_Num + Third_Random_Num
        print(f"https://prnt.sc/{Random_Char}{Second_Random_Char}{Random_Num}{Second_Random_Num}{Third_Random_Num}")
