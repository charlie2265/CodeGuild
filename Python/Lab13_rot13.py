english = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
rot13 = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def encrypt(string):
    rotated = ''
    for i in range(len(string)):
        english_idx = english.index(string[i])
        rotated += rot13[english_idx]
    return rotated

def decrypt (string):
    unrotate =''
    for i in range(len(string)):
        rot_idx = rot13.index(string[i])
        unrotate += english[rot_idx]
    return unrotate

def rotn_encrypt(string, n):
        rotated = ''
    for i in range(len(string)):
        english_idx = alpha.index(string[i])
        rotated += rot13[english_idx]
    return rotated

def repl():
	while True:
		while True:
			operation = input(
			    'Would you like to (e)ncrypt or (d)ecrypt a message? ').lower().strip()
			if operation in ['e', 'encrypt', 'd', 'decrypt']:
				break

		if operation.startswith('e'):
			user_input = input('Enter a message you would like to encrypt:\n')
			print(encrypt(user_input))
		else:
			user_input = input('Enter a message you would like to decrypt:\n')
			print(decrypt(user_input))

		while True:
			play_again = input('Would you like to play again? ').lower().strip()
			if play_again in ['y', 'yes', 'n', 'no']:
				break

		if play_again.startswith('n'):
			break
        


repl()