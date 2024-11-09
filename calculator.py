a =input("enter the first number:")
c =input("enter an operator:")

if c not in['+','-','*','/']:
    print("error")
else:
    b =input("enter the second number:")
    expression=a + c + b
    result = eval(expression)
    print("answer:",result)