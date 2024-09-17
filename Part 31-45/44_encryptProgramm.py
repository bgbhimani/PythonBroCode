import random
import string
def main():
    chars = " " + string.ascii_letters + string.punctuation + string.digits
    chars = list(chars)
    key = chars.copy()
    random.shuffle(key)

    # Encryption
    while True:
        plain_text = input("Enter Message to Encrypt (Enter to exit):  ")
        cipher_text = ""

        if plain_text == "":
            break

        for letter in plain_text:
            index = chars.index(letter)
            cipher_text += key[index]
        print(f"The Encrypted Message is: {cipher_text}")
    
    # Decryption
        cipher_text = input("Enter Encrypted Message: ")
        plain_text = ""

        for letter in cipher_text:
            index = key.index(letter)
            plain_text += chars[index]
        print(f"The Decrypted Message is: {plain_text}")



if __name__ == '__main__':
    main()