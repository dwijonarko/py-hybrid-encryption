from utils.RSAHelper import RSAHelper
from utils.HCHelper import HCHelper
from utils.CharHelper import CharHelper
from base64 import b64decode, b64encode

menu_options = {
	1: 'Encryption',
	2: 'Decryption',
	3: 'Origintal Text Histogram and Frequency Analysis',
	4: 'Encrypted Text Histogram and Frequency Analysis',
	5: 'Exit'
}
print("="*70)
print("Text Encryption Algorithm Trough Unimodular Matrix and Logistic Map")
print("-"*70)
def print_menu():
	for key in menu_options.keys():
		print (key, '--', menu_options[key] )

if __name__ == '__main__':
	while (True):
		print_menu()
		option = ''
		try:
			option = int(input('Enter your choice: '))
		except:
			print('Wrong input. Please enter a number ...')
		# Check what choice was entered and act accordingly
		if option == 1:
				HCHelper.enkripsi("sources/loremm.txt") #hasil disimpan di file enkripsi.txt
				
				key_size = 1024

				RSAHelper.new_keys(key_size)
				public_key = "certificate/public.pem"
				
				with open('results/enkripsi.txt', 'r') as file:
					msg1 = file.read()
					msg1 = msg1.encode()
				encrypted = b64encode(RSAHelper.encrypt(msg1, public_key))
				
				f = open ('results/rsa_enkripsi.txt', 'w',encoding='utf-8')
				f.write(str(encrypted.decode()))
				f.close()
			
		elif option == 2:
			private_key = "certificate/private.pem"

			#dekripsi RSA
			with open('results/rsa_enkripsi.txt', 'r') as file:
				encrypted = file.read()
				encrypted = encrypted.encode()
			
			decrypted = RSAHelper.decrypt(b64decode(encrypted), private_key)
			f = open ('results/rsa_dekripsi.txt', 'w',encoding='utf-8')
			f.write(str(decrypted.decode()))
			f.close()

			#decrypt hillcipher
			HCHelper.dekripsi('results/rsa_dekripsi.txt')
		elif option == 3:
			CharHelper.main('sources/loremm.txt')
		elif option == 4:
			CharHelper.main('results/rsa_enkripsi.txt')
		elif option == 5:
			print('Thank you for using this program. Please press enter')
			exit()
		else:
			print('Invalid option. Please enter a number between 1 and 5.')



