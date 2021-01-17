import binascii

x = '1c0111001f010100061a024b53535009181c'
y = '686974207468652062756c6c277320657965'
deHexedX = binascii.unhexlify(x)
deHexedY = binascii.unhexlify(y)

result = bytearray()
for i in range(len(deHexedX)):
    result.append((deHexedX[i] ^ deHexedY[i]))

print(result)
print(binascii.hexlify(result))
