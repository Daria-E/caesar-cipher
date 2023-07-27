def main():
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    action = input("Do you want to (e)ncrypt or (d)ecrypt? ").lower()
    if (action not in ['e','d']):
        print("Please enter 'e' or 'd'.")
        exit()
    
    key = input("Enter the key (0-25) to use: ")
    try:
        key = int(key)
    except:
        print("Please enter a number between 0 and 25.")
        exit()
    if (key < 0 or key > 25):
        print("Please enter a number between 0 and 25.")
        exit()

    msg = input("Enter your message: ").upper()
    if action == 'e':
        encrypt(key, msg, alphabet)
    else:
        decrypt(key, msg, alphabet)
        

def encrypt(key, msg, alphabet):
    new_msg = ''
    for i in range(len(msg)):
        char=msg[i]
        if char not in alphabet:
            new_msg += char
        elif alphabet.index(char) + key > 25:
            new_msg += alphabet[alphabet.index(char) + key - 26]
        else:
            new_msg += alphabet[alphabet.index(char) + key]
    print(new_msg)

def decrypt(key, msg, alphabet):
    new_msg = ''
    for i in range(len(msg)):
        char=msg[i]
        if char not in alphabet:
            new_msg += char
        elif alphabet.index(char) - key < 0:
            new_msg += alphabet[alphabet.index(char) - key + 26]
        else:
            new_msg += alphabet[alphabet.index(char) - key]
    print(new_msg)


if __name__ == "__main__":
	main()