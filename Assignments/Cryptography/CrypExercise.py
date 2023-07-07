# Write code to accomplish each question as written in instructions.md.  Replace the empty string in each return statement with the correct return.

def question01(s):
  return s[2]

def question02(s):
  return s[4]

def question03(s):
  return len(s)

def question04(s):
  return s[0]

def question05(s):
  return s[-1]

def question06(s):
  return s[-2]

def question07(s):
  return s[3:8]

def question08(s):
  return s[-5:]

def question09(s):
  return s[3:]

def question10(s):
  return s.lower()

def question11(s):
  return s.upper()

def question12(s):
  return list(s)

def question13(s):
  return s[0:len(s) -1]

def question14(s):
  return s[1: len(s)]

def question15(s):
  return s.count("e")

def question16(s):
  return str(s.count("e") + s.count("E"))

def question17(s):
  voTi = s.lower()
  return str(voTi.count("a") + voTi.count("e") + voTi.count("i") + voTi.count("o") + voTi.count("u"))

def question18(s):
  vowel = []
  for i in s:
    if i.lower() == "a" or i.lower() == "e" or i.lower() == "i" or i.lower() == "o" or i.lower() == "u":
      vowel.append(i)
  return vowel

def question19(s):
  everyother = []
  for i in range(len(s)):
  	if i % 2 == 0:
  		everyother.append(s[i])
  return everyother

def question20(s):
  everyother = []
  for i in range(len(s)):
  	if i % 2 != 0:
  		everyother.append(s[i])
  return everyother

def question21(s):
  substrings = []
  for i in range(len(s) - 1):
    substrings.append(s[i:i+2])
  return substrings

def question22(s):
  result = ""
  for i in range(len(s)):
      if i % 3 == 0:
        result += "!"
      else:
        result += s[i]
  return result

def question23(s):
  result = ""
  for i in range(len(s)):
    if (i - 2) % 3 == 0:
      result += "!"
    else:
      result += s[i]
  return result

#CHANGE THIS to do other tests!
st = "ExampleString"  

print("#1:", question01(st))
print("#2:", question02(st))
print("#3:", question03(st))
print("#4:", question04(st))
print("#5:", question05(st))
print("#6:", question06(st))
print("#7:", question07(st))
print("#8:", question08(st))
print("#9:", question09(st))
print("#10:", question10(st))
print("#11:", question11(st))
print("#12:", question12(st))
print("#13:", question13(st))
print("#14:", question14(st))
print("#15:", question15(st))
print("#16:", question16(st))
print("#17:", question17(st))
print("#18:", question18(st))
print("#19:", question19(st))
print("#20:", question20(st))
print("#21:", question21(st))
print("#22:", question22(st))
print("#23:", question23(st))