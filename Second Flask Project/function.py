def allfruits():
    all_fruit = ['apple', 'banana', 'orange']
    print(all_fruit)

def Mathoperation(a,b,operater):
    a = input(float('Enter the first number:'))
    b = input(float('Enter the second number:'))
    c = input(str("Enter the operater:'+','-','*','/':"))
    if c == '+':
        return a+b
    elif c == '-':
        return a-b
    elif c == '*':
        return a*b
    elif c == '/':
        return a/b
