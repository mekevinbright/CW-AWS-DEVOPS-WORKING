def control(entry):
    global check, a
    for i in range(len(entry)):
        if (entry[i] not in check["ac"] ) and (entry[i] not in check["kapa"] ):
            return print("Not valid input!")
    
    if len(entry) % 2 != 0:
        return print("false")
    
    if entry[0] in check["kapa"]:
        return print("false")
    
    a = 0

def evaluation(entry):
    global check, kapa
    if entry == []:
        return print("true")
    if entry[len(kapa)] in check["ac"]:
        for i in range(3):
            if entry[len(kapa)] == check["ac"][i]:
                kapa.append(check["kapa"][i])
        if entry[len(kapa)] in check["kapa"]:
            if entry[len(kapa)] == kapa[-1]:
                entry.pop(len(kapa) - 1)
                entry.pop(len(kapa) - 1)
                kapa = []
                evaluation(entry)
            else:
                return print("false")
        else:
            evaluation(entry)
        
check = {"ac" : ["(", "[", "{"], "kapa" : [")", "]", "}"]}    
kapa = []    
a = 1
while a:
    entry = list(input("Enter a string containing just the characters `(`, `)`, `{`, `}`, `[` and `]`: "))
    control(entry)
    
evaluation(entry)