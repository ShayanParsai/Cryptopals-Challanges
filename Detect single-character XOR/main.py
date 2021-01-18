import binascii

keys_list = ['30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '41', '42', '43', '44', '45',
             '46', '47', '48','49', '4A', '4B', '4C', '4D', '4E', '4F', '50', '51', '52', '53', '54',
             '55', '56', '57', '58', '59', '5A', '61', '62', '63', '64', '65', '66', '67', '68', '69',
             '6A', '6B', '6C', '6D', '6E', '6F', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '7A']

stringsTxt = open('StringList.txt').readlines()
stringsList = []
for i in range(len(stringsTxt)):
    stringsList.append(stringsTxt[i].strip())
result = bytearray()

for i in range(len(stringsList)):
    hexEncodedString = binascii.unhexlify(stringsList[i])

    for j in range(len(keys_list)):
        key = binascii.unhexlify(keys_list[j])

        for n in range(len(hexEncodedString)):
            result.append((hexEncodedString[n] ^ key[0]))
        decodedResult = result.decode("iso-8859-15")
        theRightResult = decodedResult.replace(" ", "").strip()

        if theRightResult.isalpha():
            print('\n',result.decode("iso-8859-15"))
            print(binascii.hexlify(result))
            print('The key for this attempt was : ', key.decode())
        result.clear()
