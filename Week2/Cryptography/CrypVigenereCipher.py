# Read the instructions to see what you need to do here!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def vig_encode(text, keyword):
  encodedText = []
  for counter in range(len(text)):
    mNumber = alpha.index(text[counter])
    kExp = counter % len(keyword)
    kNumber = alpha.index(keyword[kExp])
    eNumber = (mNumber + kNumber) % 26
    encodedText.append(alpha[eNumber])
  return "".join(encodedText)


def vig_decode(text, keyword):
  encodedText = []
  for counter in range(len(text)):
    mNumber = alpha.index(text[counter])
    kExp = counter % len(keyword)
    kNumber = alpha.index(keyword[kExp])
    eNumber = (mNumber - kNumber) % 26
    encodedText.append(alpha[eNumber])
  return "".join(encodedText)


test = "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG"
vig_key = "TEST"
enc = vig_encode(test, vig_key)
dec = vig_decode(enc, vig_key)
print("The Encoded Vigenere Cipher is: " + enc)
print("The Decoded Vigenere Cipher is: " + dec)
# If this worked, dec should be the same as test!
