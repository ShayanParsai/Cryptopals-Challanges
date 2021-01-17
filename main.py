import base64

hexString = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
byteArray = bytearray.fromhex(hexString)
print("This is the hexString in bytearray format : ", byteArray)
base64Value = base64.b64encode(byteArray)
print("This is the base 64 value : ", base64Value)
