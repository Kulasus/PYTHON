def maskify(cc):
    if len(cc) > 4:
        result = ""
        for letter in cc[:len(cc)-4]:
            result += "#"
        result+=cc[len(cc)-4:]
        return result
    else:
        return cc
