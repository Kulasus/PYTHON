import numbers

def invert(x):
    y = ""
    for i in x:
        if i.isupper():
            y += i.lower()
        else:
            y += i.upper()
    return y

def translate(dictionary, word):
    if word in dictionary:
        return dictionary[word]
    else:
        print("This word is not in dictionary!")
        alphabetical_list = []
        for i in dictionary:
            alphabetical_list.append(i)
        alphabetical_list.sort()
        print(alphabetical_list)
        return None

def fu(x):
    return (x*3)+5

def fu_map(seznamHodnot, fu):
    for i in seznamHodnot:
        if isinstance(i,numbers.Number):
            pass
        else:
            seznamHodnot.remove(i)
    result = [fu(i) for i in seznamHodnot]
    return result

def factorial(x):
    result = x
    while x!=1:
        result = result*(x-1)
        x = x-1
    return result

myDicionary = {"Hello":"Ahoj", "World":"Svět", "Pain":"Bolest", "Light":"Světlo", "Blue":"Modrá"}
randomString = "Hello World"
seznamH = ["hELLO", 1.47, 3, 8, "ACAR",  5]
factorialNumber = 4
#print(invert(randomString))
#print(translate(myDicionary,"Banana"))
#print (fu_map(seznamH,fu))
#print(factorial(factorialNumber))
