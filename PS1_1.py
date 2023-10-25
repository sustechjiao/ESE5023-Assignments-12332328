#test1
def compare_and_output(a, b, c):
    if a > b:
        if b > c:
            print((a, b, c))
            return
        elif a > c:
            print((a, c, b))
            return
        else:
            print((c, a, b))
    else:
        if(b>c):
            if (a > c):
                print(b, a, c)
            else:
                print(b, c, a)
        else:
            print(c,b,a)
                