# WHATS YOUR PET'S NAME?

# CREATED BY: MARIA SCALSKAYA, https://github.com/scalochnaya
# READ MORE INFO IN 'README.md'

############################################################################

import re
import requests
from bs4 import BeautifulSoup

class colors:
        RED = '\033[91m'
        WHITE = '\033[0m'
        GREEN = '\033[92m'

dictionary = []

############################################################################

# TO-DICTIONARY FUNCTIONS
def name_to_dict(n):
    dictionary.append(n.upper())
    dictionary.append(n[0].upper()+n[1:])
    dictionary.append(n[0])
    dictionary.append(n[:2])
    dictionary.append(n[:3])
    dictionary.append(n[:2].upper())
    dictionary.append(n[:3].upper())
    dictionary.append(n[0].upper())
    dictionary.append(n[:-1]+n[-1].upper())

def birth_to_dict(b):
    dictionary.append(b[4:])
    dictionary.append(b[6:])
    dictionary.append(b[:4])
    dictionary.append(b[:4]+b[6:])
    dictionary.append(b[:2])

def combo_to_dict(i, j):
    dictionary.append(dictionary[i]+dictionary[j])
    dictionary.append(dictionary[i]+"+"+dictionary[j])
    dictionary.append(dictionary[i]+"_"+dictionary[j])
    dictionary.append(dictionary[i]+"-"+dictionary[j])
    dictionary.append(dictionary[i]+"*"+dictionary[j])
    dictionary.append(dictionary[i]+"="+dictionary[j])
    dictionary.append(dictionary[i]+"@"+dictionary[j])
    dictionary.append(dictionary[i]+"$"+dictionary[j])

def job_to_dict(j):
    dictionary.append(j[0])
    dictionary.append(j.upper())
    dictionary.append(j[0].upper()+j[1:])
    dictionary.append(j[:-1]+j[-1].upper())

def pop_to_dict_1(name, love_name):
        dictionary.append(name[0]+love_name[0])
        dictionary.append(name[0].upper()+love_name[0])
        dictionary.append(name[0]+love_name[0].upper())
        dictionary.append(name[0].upper()+love_name[0].upper())
        dictionary.append(name[0]+"-"+love_name[0])
        dictionary.append(name[0].upper()+"-"+love_name[0])
        dictionary.append(name[0]+"-"+love_name[0].upper())
        dictionary.append(name[0].upper()+"-"+love_name[0].upper())
        dictionary.append(name[0]+"_"+love_name[0])
        dictionary.append(name[0].upper()+"_"+love_name[0])
        dictionary.append(name[0]+"_"+love_name[0].upper())
        dictionary.append(name[0].upper()+"_"+love_name[0].upper())

def pop_to_dict_2(birth, love_birth):
    dictionary.append(birth+love_birth)
    dictionary.append(birth[6:]+love_birth[6:])
    dictionary.append(birth[:4]+love_birth[:4])
    dictionary.append(birth[:2]+love_birth[:2])
    dictionary.append(birth[4:]+love_birth[4:])
    dictionary.append(birth+"-"+love_birth)
    dictionary.append(birth[6:]+"-"+love_birth[6:])
    dictionary.append(birth[:4]+"-"+love_birth[:4])
    dictionary.append(birth[:2]+"-"+love_birth[:2])
    dictionary.append(birth[4:]+"-"+love_birth[4:])
    dictionary.append(birth+"_"+love_birth)
    dictionary.append(birth[6:]+"_"+love_birth[6:])
    dictionary.append(birth[:4]+"_"+love_birth[:4])
    dictionary.append(birth[:2]+"_"+love_birth[:2])
    dictionary.append(birth[4:]+"_"+love_birth[4:])

def child_to_dict(child_list):
    dictionary.append(child_list[ch][0]+child_list[ch][2])
    dictionary.append(child_list[ch][0][0]+child_list[ch][2])
    dictionary.append(child_list[ch][0][0].upper()+child_list[ch][2])
    dictionary.append(child_list[ch][0]+child_list[ch][2][6:])
    dictionary.append(child_list[ch][0]+child_list[ch][2][:4])
    dictionary.append(child_list[ch][0]+child_list[ch][2][:2])
    dictionary.append(child_list[ch][0]+child_list[ch][2][4:])
    dictionary.append(child_list[ch][0][0]+child_list[ch][2][6:])
    dictionary.append(child_list[ch][0][0]+child_list[ch][2][:4])
    dictionary.append(child_list[ch][0][0]+child_list[ch][2][:2])
    dictionary.append(child_list[ch][0][0]+child_list[ch][2][4:])
    dictionary.append(child_list[ch][0][0].upper()+child_list[ch][2][6:])
    dictionary.append(child_list[ch][0][0].upper()+child_list[ch][2][:4])
    dictionary.append(child_list[ch][0][0].upper()+child_list[ch][2][:2])
    dictionary.append(child_list[ch][0][0].upper()+child_list[ch][2][4:])

############################################################################
    
# PROLOGUE
print(f"{colors.RED}\n\n\n  ????????????????????????????????       ?     WHAT'S YOUR PET'S NAME      ")
print("                                         ?             (WYPN)              ")
print("       ????     ??????????               ??????????????????????????????????")
print("      ?    ?????          ?              ?                                 ")
print("     ?                     ?             ?  WYPN - a little python3 script ")
print("    ?              ?        ?            ? intended to generate a wordlist ")
print("    ?   ?      ?    ?       ?            ? for brute-force attack using    ")
print("    ? ? ??    ??     ?     ??            ? basic information about person. ")
print("    ? ?                ????  ?           ? WYPN generates combinations     ")
print("     ??                       ?          ? formed from basic words you give")
print("     ? ???                     ?         ? the program and the most popular")
print("      ?        ??               ?        ? associations to keywords.       ")
print("       ????????  ?              ?        ? Enjoy it!                       ")
print("                                         ?                                 ")
print("     ?  ?  ?  ?   ?  ????   ?  ?         ??????????????????????????????????")
print("     ?  ?  ?   ? ?   ?   ?  ?? ?         ?                                 ")
print("     ?  ?  ?    ?    ????   ? ??         ? AUTHOR: Maria Scalskaya         ")
print("      ?? ??     ?    ?      ?  ?         ? (https://github.com/scalochnaya)")
print("                                         ?                                 ")
print(f"  ????????????????????????????????       ?         READ MORE IN 'README.md'{colors.WHITE}")

print(f"\n\n\nIT SMELLS LIKE SOMEBODY WANTS TO BRR..{colors.RED} BRUTE {colors.WHITE}SOMEONE.. I'M IN!")
print(f"{colors.GREEN}[USE 'ENTER' TO SKIP A QUESTION]{colors.WHITE}\n\n")

############################################################################

# INPUT INFO
pet = str(input("THE FIRST QUESTION IS...\nWHAT'S HIS/HER PET'S NAME?\nPET: "))
print("===================\nOK, NOW WE'RE READY TO PLAY\n===================")

name = str(input("NAME: "))
lname = str(input("LAST NAME: "))
birth = str(input(f"BIRTH{colors.GREEN}[DDMMYYYY]:{colors.WHITE} "))
nickname = str(input("NICKNAME: "))

love_init = str(input(f"===================\nMAYBE HE/SHE HAS A LOVER?{colors.GREEN}[y/n]:{colors.WHITE} "))
print("===================")
if love_init == "y":
    love_name = str(input("NAME: "))
    love_lname = str(input("LAST NAME: "))
    love_birth = str(input(f"BIRTH{colors.GREEN}[DDMMYYYY]: {colors.WHITE}"))
    love_nickname = str(input("NICKNAME: "))
else:
    print(":'( SUCH A BAD NEWS")
    love_name = love_lname = love_birth = love_nickname = ""

child_num = int(input(f"===================\nHAS HE GOT CHILDREN? HOW MANY?{colors.GREEN}[0, 1, 2, ...]: {colors.WHITE}"))
child_list = []
ch_num = child_num
while ch_num > 0:
    child_list.append(str(input(f"GIVE ME INFO {colors.GREEN}[NAME/NICKNAME/BIRTH[DDMMYYYY]]: {colors.WHITE}")).split("/"))
    ch_num -= 1

job = str(input(f"===================\nMAYBE A WORK PLACE?{colors.GREEN}[y/n]:{colors.WHITE} "))
if job == "y":
    job = str(input("WORK PLACE: "))
else:
    job = ""

dop_info = str(input(f"===================\nHEY, IT'S A GREAT INFO FOR ME!\nWANNA CONTINUE AND USE SOME KEYWORDS?{colors.GREEN}[y/n]: {colors.WHITE}"))
associations_dict = []
lim = 0
if dop_info == "y":
    print(f"WRITE DOWN KEYWORDS, THAT HE/SHE CAN USE IN HIS PASSWORD: {colors.GREEN}['ENTER' TO ESCAPE]{colors.WHITE}")
    while lim < 5:
        num_counter = str(lim+1)
        dop_word = input("KEYWORD "+num_counter+": ")
        if dop_word == "":
            break
        else:
            associations_dict.append(dop_word)
            dictionary.append(dop_word.lower())
            lim += 1

pet = pet.lower()
name = name.lower()
lname = lname.lower()
love_name = love_name.lower()
love_lname = love_lname.lower()
job = job.lower()
print(f"\n\n\n{colors.GREEN}I'M WORKING. DON'T DISTURB ME.\n...{colors.WHITE}")

############################################################################

# 1ST WAVE
dictionary.append(pet)
dictionary.append(name)
dictionary.append(lname)
dictionary.append(birth)
dictionary.append(love_name)
dictionary.append(love_lname)
dictionary.append(love_birth)
dictionary.append(job)

# 2ND WAVE
if birth != "":
    birth_to_dict(birth)

if love_birth != "":
    birth_to_dict(love_birth)

if name != "":
    name_to_dict(name)

if love_name != "":
    name_to_dict(love_name)

if lname != "":
    name_to_dict(lname)

if love_lname != "":
    name_to_dict(love_lname)

if nickname != "":
    name_to_dict(nickname)

if love_nickname != "":
    name_to_dict(love_nickname)

if job != "":
    job_to_dict(job)

if pet != "":
    name_to_dict(pet)
    dictionary.append(pet[:3]+"ie")
    dictionary.append(pet[:4]+"ie")
    dictionary.append(pet[:4]+"y")
    dictionary.append(pet[0]+pet[1:3]+"ie")
    dictionary.append(pet[0]+pet[1:4]+"ie")
    dictionary.append(pet[0]+pet[1:4]+"y")
    dictionary.append(pet[0]+pet[1:3]+"y")

# CHILDREN TO DICTIONARY
for ch in range(0, child_num):
    if child_list[ch][0] != "":
        name_to_dict(child_list[ch][0].lower())
    if child_list[ch][1] != "":
        name_to_dict(child_list[ch][1].lower())
    if child_list[ch][2] != "":
        birth_to_dict(child_list[ch][2])
    child_to_dict(child_list)

# ASSOCIATIONS TO DICTIONARY
for ation in range(lim):
    source = associations_dict[ation]
    url = "https://wordassociations.net/en/words-associated-with/{0}".format(source.rstrip())

    headers = {
        "accept": "*/*",
        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.3"
    }

    req = requests.get(url, headers = headers)
    src = req.text

    soup = BeautifulSoup(src, "lxml")

    associations = soup.find("div", class_ = "section NOUN-SECTION")
    if associations is None:
        continue
    associations = associations.text.strip()
    associations_list = re.findall('[A-Z][^A-Z]*', associations)
    associations_list.pop(0)
    associations_list = associations_list[:10]
    for a in range(len(associations_list)):
        dictionary.append(associations_list[a].lower())
        name_to_dict(associations_list[a])

############################################################################

# POPULAR BASIC COMBINATIONS TO OPERATE WITH
if name != '':
    if love_name != '':
        pop_to_dict_1(name, love_name)
    if lname != '':
        pop_to_dict_1(name, lname)
    if nickname != '':
        pop_to_dict_1(name, nickname)

if love_name != '':
    if love_lname != '':
        pop_to_dict_1(love_name, love_lname)
    if love_nickname != '':
        pop_to_dict_1(love_name, love_nickname)


if birth != '' and love_birth != '':
    pop_to_dict_2(birth, love_birth)

############################################################################

# TO-DICTIONARY COMBINATIONS
ldict0 = len(dictionary)
for reverse in range(ldict0):
    dictionary.append(str(dictionary[reverse])[::-1])

ldict1 = len(dictionary)
for i1 in range(ldict1):
    for j1 in range(ldict1):
        combo_to_dict(i1, j1)

############################################################################

# DICTIONARY TO .TXT FILE
dictionary = set(dictionary)
with open("wypn_wordlist.txt", "w+") as wordlist:
    for item in dictionary:
        wordlist.write("%s\n" % item)

############################################################################

# EPILOGUE
print(f"\n\n\n{colors.GREEN}CONGRATULATIONS! YOU CREATED A WORDLIST WHICH INCLUDES " + str(len(dictionary)) + " POTENTIAL PASSWORDS!\nWELL, NOW YOU CAN USE IT\n===================\n['wypn_wordlist.txt' file had been created in such directory as this .py file]{colors.WHITE}")
