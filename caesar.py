import caesarFunctions

alphabetDict = {"a": 0,"b": 1,"c": 2,"d": 3,"e": 4,"f": 5,"g": 6,"h": 7,"i": 8,"j": 9,"k": 10,"l": 11,"m": 12,"n": 13,
            "o": 14,"p": 15,"q": 16,"r": 17,"s": 18,"t": 19,"u": 20,"v": 21,"w": 22,"x": 23,"y": 24,"z": 25}
alphabetList = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

repeat = "yes"
while repeat == "yes":
    action = caesarFunctions.getAction() # obtener accion "encode" "decode"
    displacement = caesarFunctions.getDisplacement() # obtener desplazamiento
    message = caesarFunctions.getMessage() # obtener mensaje
    if action == 1:
        caesarFunctions.encode(message, displacement, alphabetDict, alphabetList, "encode")
    else:
        caesarFunctions.encode(message, displacement, alphabetDict, alphabetList, "decode")
    repeat = caesarFunctions.repeat() # obtener "yes" o "no" que indica si se repite el prompt
