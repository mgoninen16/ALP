# Read the instructions to see what you need to do here!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def caesar_encode(text, n):
  encodedText = []
  for character in text:
    encodedCharacter = alpha[(alpha.index(character) + n) % 26]
    encodedText.append(encodedCharacter)
  return encodedText

def caesar_decode(text, n):
  decodedText = []
  for character in text:
    decodedCharacter = alpha[(alpha.index(character) - n) % 26]
    decodedText.append(decodedCharacter)
  return decodedText


test = "HELLOWORLD"
shift = 5
enc = caesar_encode(test, shift)
dec = caesar_decode(enc, shift)
print(enc)
print(dec)
# If this worked, dec should be the same as test!