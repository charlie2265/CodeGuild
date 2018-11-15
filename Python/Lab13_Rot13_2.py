english = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'



def encrypt(string, n):
    coded = ''
    for i in range(len(string)):
        idx = english.find(string[i].upper())
        if idx > -1:
            rotate_idx = (idx + n) % 26
            # if rotate_idx > 25:
            #     rotate_idx -= len(english) 
            # print(idx, rotate_idx)
            coded += english[rotate_idx]
        else:
            coded += string[i]
    return coded



def decrypt(string):
    pass




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
