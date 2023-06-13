def divide(a, b):
    try:
        result = int(a) / int(b)
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")
a=input('Enter a number: ')
b=input('Enter a number: ')
divide(a,b)