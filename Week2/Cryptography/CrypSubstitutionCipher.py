# Read the instructions to see what you need to do here!
from random import shuffle

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
cipher_alphabet = [*alpha]
shuffle(cipher_alphabet)
cipher_alphabet = "".join(cipher_alphabet)

test = input("Please Input a Phrase to Encode and Decode: ")

def sub_encode(text, codebet):
  encodedText = []
  for character in text:
    indexedCharacter = alpha.index(character)
    encodedCharacter = cipher_alphabet[indexedCharacter]
    encodedText.append(encodedCharacter)
  return "".join(encodedText)


def sub_decode(text, codebet):
  decodedText = []
  for character in text:
    indexedCharacter = cipher_alphabet.index(character)
    decodedCharacter = alpha[indexedCharacter]
    decodedText.append(decodedCharacter)
  return "".join(decodedText)

enc = sub_encode(test.upper(), cipher_alphabet)
dec = sub_decode(enc.upper(), cipher_alphabet)
print("Encoded Phrase Using Substitution Cipher: " + enc.title())
print("Decoded Phrase Using Substitution Cipher: " + dec.title())
# If this worked, dec should be the same as test!