'''

Symmetric Cryptographic Encryption and Decryption in Python (AES)

Repo Owner :- PrajwalCyberGod

''' 

# Imports

from Crypto import Random
from Crypto.Cipher import AES

import os
import os.path
from os import listdir
from os.path import isfile, join

from tqdm import tqdm
from termcolor import colored,cprint

import string
import random

# Defined Functions

class Encryptor:

	def __init__(self, key):

		self.key = key

	def pad(self, s):

		return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

	def encrypt(self, message, key, key_size=256):

		message = self.pad(message)

		iv = Random.new().read(AES.block_size)

		cipher = AES.new(key, AES.MODE_CBC, iv)

		return iv + cipher.encrypt(message)

	def encrypt_file(self, file_name):

		with open(file_name, 'rb') as fo:

			plaintext = fo.read()

		enc = self.encrypt(plaintext, self.key)

		with open(file_name + ".enc", 'wb') as fo:

			fo.write(enc)

		os.remove(file_name)

	def decrypt(self, ciphertext, key):

		iv = ciphertext[:AES.block_size]

		cipher = AES.new(key, AES.MODE_CBC, iv)

		plaintext = cipher.decrypt(ciphertext[AES.block_size:])

		return plaintext.rstrip(b"\0")

	def decrypt_file(self, file_name):

		with open(file_name, 'rb') as fo:

			ciphertext = fo.read()

		dec = self.decrypt(ciphertext, self.key)

		with open(file_name[:-4], 'wb') as fo:

			fo.write(dec)

		os.remove(file_name)

	def getAllFiles(self):

		dir_path = os.path.dirname(os.path.realpath(__file__))
		dirs = []

		for dirName, subdirList, fileList in os.walk(dir_path):

			for fname in fileList:

				if (fname != 'script.py' and fname != 'password.txt.enc'):

					dirs.append(dirName + "\\" + fname)

		return dirs

	def encrypt_all_files(self):

		dirs = self.getAllFiles()

		for file_name in dirs:

			self.encrypt_file(file_name)

	def decrypt_all_files(self):

		dirs = self.getAllFiles()

		for file_name in dirs:

			self.decrypt_file(file_name)

space_count = 60 * ' '

key = b'[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e'

enc = Encryptor(key)

clear = lambda: os.system('cls')

# Main program

if os.path.isfile('password.txt.enc'):

	while True:

# Authentication

		clear()

		cprint('\n{}*** Encryption And Decryption Tool (AES) ***'.format(space_count),'red',attrs=['bold'])

		cprint('\n{}*** Programmed by Prajwal Vijaykumar Mali ***'.format(space_count),'green',attrs=['bold'])

		cprint('\n\tEnter password: ','green', attrs=['bold'])

		cprint('\n\t~CRYPTO : ','blue', attrs=['bold','blink'], on_color='on_white')

		password = str(input('\n\t'))

		enc.decrypt_file("password.txt.enc")

		p = ''

		with open("password.txt", "r") as f:

			p = f.readlines()

		if p[0] == password:

			enc.encrypt_file("password.txt")

			cprint('\n\tAuthentication Completed','green', attrs=['bold'])

			break

		else:

			enc.encrypt_file("password.txt")

			cprint('\n\tINCORRECT PASSWORD.....!','red', attrs=['bold'])

			exit()

	while True:

# Choice Menu

		clear()

		cprint('\n{}*** Encryption And Decryption Tool (AES) ***'.format(space_count),'red',attrs=['bold'])

		cprint('\n{}*** Programmed by Prajwal Vijaykumar Mali ***'.format(space_count),'green',attrs=['bold'])

		cprint('\n\t1. Press 1 to Encrypt a file','cyan', attrs=['bold'])
		
		cprint('\n\t2. Press 2 to Decrypt a file','yellow', attrs=['bold'])
		
		cprint('\n\t3. Press 3 to Encrypt all files in the directory','green', attrs=['bold'])
		
		cprint('\n\t4. Press 4 to Decrypt all files in the directory','magenta', attrs=['bold'])
		
		cprint('\n\t5. Press 5  to Exit','red',attrs=['bold'])
		
		cprint('\n\tEnter your choice (in integer format) :','cyan',attrs=['bold'])

		cprint('\n\t~CRYPTO : ','blue', attrs=['bold','blink'], on_color='on_white')

		choice = int(input('\n\t'))   

		clear() 

# To ENCRYPT the file

		if choice == 1:

			logo = '''
	  ___                       _   _          
	 | __|_ _  __ _ _ _  _ _ __| |_(_)___ _ _  
	 | _|| ' \/ _| '_| || | '_ \  _| / _ \ ' \ 
	 |___|_||_\__|_|  \_, | .__/\__|_\___/_||_|
	                  |__/|_|
                  
                  '''

			cprint(logo,'cyan',attrs=['bold'])

			cprint("\n\tEnter name of file to encrypt : ",'cyan', attrs=['bold'])

			cprint('\n\t~CRYPTO : ','blue', attrs=['bold','blink'], on_color='on_white')

			enc.encrypt_file(str(input('\n\t')))

			cprint('\n\tEncryption done Sucessfully.....!','green',attrs=['bold'])

			cprint('\n\tDo you want to do it again (y/n) : ','red',attrs=['bold'])

			again_choice  = input('\n\t')

			if (again_choice.lower() == 'y'):

				continue

			else:

				break

# To DECRYPT the file

		elif choice == 2:

			logo = '''
	  ___                       _   _          
	 |   \ ___ __ _ _ _  _ _ __| |_(_)___ _ _  
	 | |) / -_) _| '_| || | '_ \  _| / _ \ ' \ 
	 |___/\___\__|_|  \_, | .__/\__|_\___/_||_|
	                  |__/|_|                  
                                        
                  '''

			cprint(logo,'yellow',attrs=['bold'])

			cprint("\n\tEnter name of file to decrypt : ",'yellow', attrs=['bold'])

			cprint('\n\t~CRYPTO : ','blue', attrs=['bold','blink'], on_color='on_white')

			enc.decrypt_file(str(input('\n\t')))

			cprint('\n\tDecryption done Sucessfully.....!','green',attrs=['bold'])

			cprint('\n\tDo you want to do it again (y/n) : ','red',attrs=['bold'])

			again_choice  = input('\n\t')

			if (again_choice.lower() == 'y'):

				continue

			else:

				break

# To ENCRYPT the directory

		elif choice == 3:

			logo = '''
	  ___                       _   _          
	 | __|_ _  __ _ _ _  _ _ __| |_(_)___ _ _  
	 | _|| ' \/ _| '_| || | '_ \  _| / _ \ ' \ 
	 |___|_||_\__|_|  \_, | .__/\__|_\___/_||_|
	                  |__/|_|
                  
                  '''

			cprint(logo,'green',attrs=['bold'])

			enc.encrypt_all_files()

			cprint('\n\tEncryption done Sucessfully.....!','green',attrs=['bold'])

			cprint('\n\tDo you want to do it again (y/n) : ','red',attrs=['bold'])

			again_choice  = input('\n\t')

			if (again_choice.lower() == 'y'):

				continue

			else:

				break

# To DECRYPT the directory

		elif choice == 4:

			logo = '''
	  ___                       _   _          
	 |   \ ___ __ _ _ _  _ _ __| |_(_)___ _ _  
	 | |) / -_) _| '_| || | '_ \  _| / _ \ ' \ 
	 |___/\___\__|_|  \_, | .__/\__|_\___/_||_|
	                  |__/|_|                  
                                        
                  '''

			cprint(logo,'magenta',attrs=['bold'])

			enc.decrypt_all_files()

			cprint('\n\tDecryption done Sucessfully.....!','green',attrs=['bold'])

			cprint('\n\tDo you want to do it again (y/n) : ','red',attrs=['bold'])

			again_choice  = input('\n\t')

			if (again_choice.lower() == 'y'):

				continue

			else:

				break

# To close the program

		elif choice == 5:

			exit()

# When user input has an error			

		else:

			cprint('\n\tPlease select a valid option.....!','red',attrs=['bold'])

			break

# Password setup

else:

	while True:

		cprint('\n{}*** Encryption And Decryption Tool (AES) ***'.format(space_count),'red',attrs=['bold'])

		cprint('\n{}*** Programmed by Prajwal Vijaykumar Mali ***'.format(space_count),'green',attrs=['bold'])

		cprint("\n\tSetting up stuff.....",'yellow',attrs=['bold'])

		cprint("\n\tDo you want to generate a random password (y/n) : ",'red',attrs=['bold'])

		cprint('\n\t~CRYPTO : ','blue', attrs=['bold'], on_color='on_white')

		random_pass  = input('\n\t')

		if (random_pass.lower() == 'y'):

# For random password generator			

			s1 = string.ascii_lowercase
			s2 = string.ascii_uppercase
			s3 = string.digits
			s4 = string.punctuation

			cprint("\n\tEnter password length: ",'yellow', attrs=['bold'])

			cprint('\n\t~CRYPTO : ','blue', attrs=['bold'], on_color='on_white')

			plen = int(input('\n\t'))

			s = []

			s.extend(list(s1))
			s.extend(list(s2))
			s.extend(list(s3))
			s.extend(list(s4))

			password = "".join(random.sample(s, plen))		

			cprint('\n\tPassword is saved Sucessfully.....!','green',attrs=['bold'])

			cprint('\n\tYour password is :','magenta',attrs=['bold'])

			cprint('\n\t'+password,'green',attrs=['bold'])

			cprint('\n\tPlease save it SECURELY.....!','cyan',attrs=['bold'])

			cprint("\n\tPlease restart the program to complete the setup.....",'yellow',attrs=['bold'])

			break

		else:

# For manual password setup			

			cprint("\n\tEnter a password that will be used for decryption : ",'cyan',attrs=['bold',])

			cprint('\n\t~CRYPTO : ','blue', attrs=['bold'], on_color='on_white')

			password = str(input('\n\t'))

			cprint("\n\tConfirm password: ",'magenta',attrs=['bold'])  

			cprint('\n\t~CRYPTO :','blue', attrs=['bold'], on_color='on_white') 

			repassword = str(input('\n\t'))

			if password == repassword:				

				cprint('\n\tPassword is saved Sucessfully.....!','green',attrs=['bold'])

				cprint("\n\tPlease restart the program to complete the setup.....",'yellow',attrs=['bold'])

				break

			else:

				cprint("\n\tPasswords Mismatched.....!",'red', attrs=['bold'])

				exit()

	f = open("password.txt", "w+")

	f.write(password)

	f.close()

	enc.encrypt_file("password.txt")	