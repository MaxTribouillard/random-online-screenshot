import random
from colorama import Style, Fore, Back
import string

print(Fore.GREEN + "Bienvenue dans le chercheur de screenshots aléatoire en ligne ! ")
print(Fore.GREEN + "Welcome in the random screenshots searcher online ! ")

lancement = input("Voulez vous vraiment lancer le générateur de screenshot ? (Oui/Non) : ")

while lancement == str("Oui"):
    char_list = string.ascii_letters
    second_char_list = string.ascii_letters
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for num in range(6):
        Random_Char = random.choice(char_list)
        Random_Num = random.choice(num_list)
        print(f"https://prnt.sc/{Random_Char}{Random_Char}{Random_Num}{Random_Num}{Random_Num}")
