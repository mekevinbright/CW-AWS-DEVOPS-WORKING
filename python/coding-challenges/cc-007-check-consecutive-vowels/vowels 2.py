word = input("Please enter a string: ")
word = word.lower()

vowels = ["a", "e", "i", "o", "u"]
exist = False

for i in range(len(word)-1):
  if word[i] in vowels:
    if word[i+1] in vowels:
      exist = True
      break

if exist:
  print("Positive")
else:
  print("Negative")



def checkvowels(text):
    vowel = False 
    for i in text:
        if i in set('aeiou'):
            if vowel:
                return 'Positive'
            else:
                vowel = True
        else:
            vowel = False
    return 'Negative'

def checkvowels2(text):   
    return 'Positive' if len([1 for i in range(len(text)-1) if set(text[i:i+2]) - set('aeiou') == set()]) > 0 else 'Negative'

def checkvowels3(text):   
    for i in range(len(text)-1): 
        if set(text[i:i+2]) - set('aeiou') == set():
            return 'Positive'
    return 'Negative'



x = "zafeer"
xlist = list(x)
vowels = ["a", "e", "i", "o", "u"]
result = 1
res = 0
for i in range(len(xlist) - 1):
    if xlist[i] in vowels and xlist[i + 1] in vowels:
        result = 0
        res = 1
print("negative" * result or "positive" * res)