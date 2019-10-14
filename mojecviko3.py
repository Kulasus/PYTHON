def my_avg(*params):
    summary = 0; count = 0
    for param in params:
        if type(param) != int and type(param) != float:
            print("Neplatne parametry!")
            return False
        else:
            summary += param
            count += 1
    return summary/count


def divide(number,collection):
    result = map(lambda x: x // number, collection)
    return list(result)

def addTwo(number):
    return number+2
    
    
def my_map(function,collection):
    result = [function(n) for n in collection]
    return result


def file_handler():
    listOfLines = []
    f = open(r'C:\Users\lukas\OneDrive\Plocha\Python\calls.txt')
    try:
        for line in f:
            listOfLines.append(line)

        print(listOfLines)
    except:
        print ("Fatal error")
    finally:
        f.close()






a1 = 6
a2 = 5
a3 = 10
collection = [15,6,8,22]
print(my_avg(a1,a2))
print(divide(a1,collection))
print(my_map(addTwo,collection))
file_handler()