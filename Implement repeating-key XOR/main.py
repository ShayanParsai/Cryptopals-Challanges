import binascii


def main():
    message = open('TextToEnOrDeCrypt.txt').readlines()
    stringsList = []
    for i in range(len(message)):
        stringsList.append(message[i].strip())

    #Pick a key, keep it secret
    key = 'bra fråga ;)'

    #use this method if you want to encrypt your text, paste the text in the ' TextToEncrypt/Decrypt.txt'
    encrypt(message,key,stringsList)

    #use this method if you want to decrypt that text, make sure to use the key that you used to encrypt the text
    #decrypt(message,key,stringsList)

    #Comment out the method that you arent using with '#'


def encrypt(message, key, stringsList):
    for i in range(len(stringsList)):
        stringsList[i] = binascii.hexlify(encrypt_decrypt(stringsList[i], key))
    for s in stringsList:
        print(s.decode('utf-8'))


def decrypt(message, key, stringsList):
    for i in range(len(stringsList)):
        stringsList[i] = binascii.unhexlify(stringsList[i]).decode('iso-8859-15')
        stringsList[i] = encrypt_decrypt(stringsList[i], key)
    for s in stringsList:
        print(s.decode('iso-8859-15'))


def encrypt_decrypt(message, key):
    encrypted_message = bytearray()
    for i in range(len(message)):
        encrypted_message.append(ord(message[i]) ^ ord(key[i % len(key)]))
    return encrypted_message


if __name__ == '__main__':
    main()
