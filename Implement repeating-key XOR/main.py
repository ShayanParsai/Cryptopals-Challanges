import binascii


def main():
    message = open('TextToEncrypt.txt').readlines()
    key = 'ICE'
    stringsList = []
    for i in range(len(message)):
        stringsList.append(message[i].strip())

    #DeCrypted > Crypted
    for i in range(len(stringsList)):
        stringsList[i] = binascii.hexlify(encrypt_decrypt(stringsList[i], key))
    for s in stringsList:
        print(s.decode('utf-8'))

    #Crypted > DeCrypted
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
