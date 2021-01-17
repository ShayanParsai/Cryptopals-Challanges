import binascii


keys_list = ['41','42','43','44','45','46','47','48','49','4A','4B','4C','4D','4E','4F','50','51','52','53','54',
             '55','56','57','58','59','5A','61','62','63','64','65','66','67','68','69',
             '6A','6B','6C','6D','6E','6F','70','71','72','73','74','75','76','77','78','79','7A']

hexEncodedString = binascii.unhexlify('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')


result = bytearray()
for j in range(len(keys_list)):
    key = binascii.unhexlify(keys_list[j])
    for i in range(len(hexEncodedString)):
        result.append((hexEncodedString[i] ^ key[0]))
    print('\n',result.decode())
    print(binascii.hexlify(result))
    print('The key for this attempt was : ',key)
    result.clear()







