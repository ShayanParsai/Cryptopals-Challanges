import base64

byteArray = bytearray.fromhex('49276d206b696c6c696e6720796f757220627261696e206c6'
                              '96b65206120706f69736f6e6f7573206d757368726f6f6d')
print(byteArray.decode())
print(base64.b64encode(byteArray))
