# What's Your Pet's Name? [WYPN]

"What's Your Per's Name", or WYPN is a little python3 script intended to generate a wordlist for brute-force attack using basic
information about person. WYPN generates combinations formed from basic words you give the program 
and associations to keywords. Made with Python 3.10.

WYPN is now available on Linux systems. Recommended use systems with 2+ GB RAM.
#

How to get a program?
 - Write to Linux console 'git clone https://github.com/scalochnaya/WYPN' command. It will 
   download from GitHub repository all files that you need. 
   After installation run 'python3 WYPN_demo.py' or 'python WYPN_demo.py' (if you don't have installed packages, run in terminal 'sudo apt install python3-pip' and then 'pip install BeautifulSoup4' and 'pip install lxml')
#

How the program works?
 - 1. You write to WYPN console basic information about user, such as: name, last name, birth, nickname, information about user's lover and children and keywords (if you don't know some facts that WYPN requests, use 'ENTER' to skip a question)
   2. WYPN generates a wordlist, using given information. Also WYPN uses scraping methods: it searches associating nouns to keywords which are taken from "https://wordassociations.net". Standart length of the wordlist is about 3000000 - 12000000 potential passwords.
   3. After the program finished the process, potential passwords had been written into "wypn_wordlist.txt" (WYPN creates this file in a such directory as WYPN.py file)
   4. Well done! Now you can use generated wordlist for brute-force attack!

! Remember that we use brute-force just for checking our own passwords !
! Program created exclusively for educational purposes. I don't call for and condemn illegal actions !
#

Dear user,

 If you have some suggestions to make program better, or you have problems with it, please contact me: scalochnaya@gmail.com
#

by Maria Scalskaya

P.S. I'm still waiting for you. In our 'special' place: https://github.com/scalochnaya
