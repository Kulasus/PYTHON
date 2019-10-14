import math



#-------------------------------------------
def spherical_sector(r,h):
    if type(r) and type(h) in (int,float):
        pass
    else:
        print("Neplatne parametry")
        return False
    #-------------------------------------------
    return ((2*math.pi)*(r**2)*h)/3





#-------------------------------------------
def sqr(numberOrCollection,number):
    if type(numberOrCollection) in (int,list):
        if type(numberOrCollection) is list:
            for i in numberOrCollection:
                if i is int:
                    pass
                else:
                    print("Neplatne parametry")
                    return False
    else:
        print("Neplatne parametry")
        return False
    if type(number) is int:
        pass
    else:
        print("Neplatne parametry")
        return False
    #-------------------------------------------
    result = []
    if type(numberOrCollection) is int:
        result.append(numberOrCollection**number)
        print(result)
    else:
        for i in numberOrCollection:
            result.append(i**number)
        print(result)





#-------------------------------------------
def shuffle(string1, string2):
    if type(string1) is str and type(string2) is str:
        pass
    else:
        print("Neplatne parametry")
        return False
    #-------------------------------------------
    result = ""
    if(len(string1) == len(string2)):
        x = 0
        while(x != len(string1)):
            result += string1[x] + string2[x]
            x += 1
    #-------------------------------------
    elif(len(string1) > len(string2)):
        x = 0
        while(x != len(string2)):
            result += string1[x] + string2[x]
            x += 1
        while(x != len(string1)):
            result += string1[x]
            x+=1
    #-------------------------------------
    elif(len(string1) < len(string2)):
        x = 0
        while(x != len(string1)):
            result += string1[x] + string2[x]
            x += 1
        while(x != len(string2)):
            result += string2[x]
            x+=1
    #-------------------------------------
    return result






r = 5; h = 2
x = [3, "ahoj", 2]; y = 3
str1 = "Hellooooooo"; str2= "World"

print(spherical_sector(r,h))
sqr(x,y)
print(shuffle(str1,str2))


 
