import binascii

x = binascii.unhexlify('1c0111001f010100061a024b53535009181c')
y = binascii.unhexlify('686974207468652062756c6c277320657965')

result = bytearray()
for i in range(len(x)):
    result.append((x[i] ^ y[i]))

print(result.decode())
print(binascii.hexlify(result))