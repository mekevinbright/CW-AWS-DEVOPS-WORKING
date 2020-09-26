def checkform2(text):
    while any(i for i in ["()","{}","[]"] if i in text):
        text = text.replace("()","")
        text = text.replace("{}","")
        text = text.replace("[]","")
    return not bool(text) 


    x = "(){((([])))}"

for i in x:

    x = x.replace("()","")

    x = x.replace("[]","")

    x = x.replace("{}","")

print(not bool(x))