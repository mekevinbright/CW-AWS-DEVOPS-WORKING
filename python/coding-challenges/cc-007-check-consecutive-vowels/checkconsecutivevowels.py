def check_cons_vowels(text):
    vowels = "aeiouöüı"
    for i in range(len(text)):
        if i < len(text)-1 and text[i] in vowels and text[i+1] in vowels:
            is_positive = "Positive"
            break
        else:
            is_positive = "Negative"
    return is_positive


text = input("Please enter a text: ")
print(check_cons_vowels(text.lower()))

