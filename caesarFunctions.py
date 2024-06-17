def getAction():
    flag = False
    while flag == False:
        flag = True
        try:
            action = int(input("What do you want to do? (1. Encode, 2. Decode): "))
            if action< 1 or action > 2:
                flag = False
                print(flag)
        except ValueError:
            flag = False
        if flag == False:
            print("Enter 1 or 2.")
    return action

def getDisplacement():
    flag = False
    while flag == False:
        flag = True
        try:
            displacement = int(input("Enter displacement: "))
        except ValueError:
            flag = False
            print("Enter a number.")            
    return displacement

def getMessage():
    return input("Enter Message: ")

def encode(message, displacement, alphabetDict, alphabetList, action):
    newMessage = ""
    messageLenght = len(message)
    for i in range(0, messageLenght):
        upperFlag = False
        if message[i].isalpha(): # si el char es alpha
            if message[i].isupper(): # si el char es mayuscula
                upperFlag = True
                char = message[i].lower() # pasar a minuscula
            # se usa alpabetDict para obtener indice del char actual
                if action == "encode":
                    newChar = alphabetDict[char] + displacement # si es encode sumar displacement
                else: # al hacer decode, la adicion o substraccion del displacement debe ser la inversa al encode
                    newChar = alphabetDict[char] - displacement # si es decode restar displacement
            else:
                if action == "encode":
                    newChar = alphabetDict[message[i]] + displacement
                else:
                    newChar = alphabetDict[message[i]] - displacement
            newChar = getNewChar(newChar)
            # se usa alphabetList para obtener el char mediante el indice (newChar es el indice que se obtiene del dict)
            if upperFlag: # si la flag de upper se activó, el char se debe pasar a upper de nuevo para respetar el mensaje original
                char = alphabetList[newChar].upper()
                newMessage = newMessage + char
            else: # sino se coloca tal cual
                newMessage = newMessage + alphabetList[newChar]
        else: # si el char no es alpha
            newMessage = newMessage + message[i]
    print(newMessage)

def getNewChar(newChar): # se asegura de obtener un char dentro del rango
    while newChar > 25: # El char obtenido {newChar} se pasa del rango
        newChar = newChar - 26
    while newChar < 0: # El char obtenido {newChar} es menor que el rango
        newChar = newChar + 26
    return newChar

def repeat():
    flag = False
    while flag == False:
        flag = True
        repeat = input("Do you want to continue? (yes/no): ")
        repeat = repeat.lower()
        if repeat not in ["yes", "no"]:
            flag = False
            print("Enter yes or no.")            
    return repeat