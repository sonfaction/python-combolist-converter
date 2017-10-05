#!c:/Python/python.exe
#-*- coding: utf-8 -*-

###Thx to - bp0s1x - haxstroke - f0rest - pr0s3x - goldb
####Original by SonGoku - Son - GonSoku

#modules
import time 
import os 
import sys
os.system("cls")

#stdin
data  = raw_input("Combolist > ")
delim = raw_input("Delimiter > ")

#fs
parse = open(data, 'r').readlines()
email = open("mail_o.txt", 'w')
senha = open("pass_o.txt", 'w')

#stdout
for linha in parse:
    linha = linha.strip()
    MAIL, PASS = linha.split(delim)
    try:
        email.write("%s\n" % MAIL)
        senha.write("%s\n" % PASS)
        print "+----------------------------------------"
        print "|  Mail: "+MAIL  
        print "|  Pass: "+PASS 
        print "+----------------------------------------"
    except IOError:
        print "Não foi possível salvar o arquivo (I/O err)"