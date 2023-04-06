

def factorial(n):
    if n == 1:
        return 1
    elif n == 0:
        return 1
    return n * factorial(n-1)


def main():
    print(factorial(0),"= 0!")
    print(factorial(2),"= 2!")
    print(factorial(4),"= 4!")
    print(factorial(6),"= 6!")
    print(factorial(8),"= 8!")
    print(factorial(10),"= 10!")
    print(factorial(12),"= 12!")
    print(factorial(14),"= 14!")
    
    

if __name__== "__main__":
    main()
