from utils import hc_util,rsa_util,histogram_util,frequency_util
from utils.rsa_util import RSAHelper
from collections import Counter
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
				hc_util.enkripsi("sources/loremm.txt") #hasil disimpan di file enkripsi.txt
				
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
			hc_util.dekripsi('results/rsa_dekripsi.txt')
		elif option == 3:
			# Original Text Histogram and Frequency Analysis
			# Read the original text
			with open('sources/loremm.txt', 'r') as file:
				original = file.read()
			
			histogram_util.plot_histogram(original)

			# Menghitung frekuensi bigram
			bigram_counts = Counter([original[i:i+2] for i in range(len(original)-1)])

			# Visualisasi frekuensi bigram
			frequency_util.plot_ngram_frequency(bigram_counts, 'Bigram')

			# Menghitung frekuensi trigram
			trigram_counts = Counter([original[i:i+3] for i in range(len(original)-2)])

			# Visualisasi frekuensi trigram
			frequency_util.plot_ngram_frequency(trigram_counts, 'Trigram')
		elif option == 4:
			# Encrypted Text Histogram and Frequency Analysis
			# Read the encrypted text
			with open('results/enkripsi.txt', 'r') as file:
				encrypted = file.read()
			
			histogram_util.plot_histogram(encrypted)

			# Menghitung frekuensi bigram
			bigram_counts = Counter([encrypted[i:i+2] for i in range(len(encrypted)-1)])

			# Visualisasi frekuensi bigram
			frequency_util.plot_ngram_frequency(bigram_counts, 'Bigram')

			# Menghitung frekuensi trigram
			trigram_counts = Counter([encrypted[i:i+3] for i in range(len(encrypted)-2)])

			# Visualisasi frekuensi trigram
			frequency_util.plot_ngram_frequency(trigram_counts, 'Trigram')

		elif option == 5:
			print('Thank you for using this program. Please press enter')
			exit()
		else:
			print('Invalid option. Please enter a number between 1 and 5.')



