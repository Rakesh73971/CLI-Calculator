def get_number(prompt='Enter a number'):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print('Invalid Input.Enter a valid number')

def arithmetic_operation(a,b):
    operations = {
        "+":lambda x,y : x+y,
        "add":lambda x,y: x+y,
        "-":lambda x,y:x-y,
        "subtract":lambda x,y:x-y,
        "*":lambda x,y:x*y,
        "multiply":lambda x,y:x*y,
        "/":lambda x,y:x/y if y != 0 else "Error:Division by zero",
        "division":lambda x,y: x/y if y != 0 else "Error:Division by zero"
    }

    print('Available operations: + , -, *, / or add, subtract, multiply, division ')

    while True:
        op = input('Enter your operation: ')
        if op in operations:
            if (op == "/" or op == "division") and b == 0:
                print("Error: Division by zero. Enter a different number.")
                return None
            return operations[op](a,b)
        else:
            print('Invalid operation')
    
def main():
    result = None
    continue_cal = True
    while continue_cal:
        first = result if result is not None else get_number('Enter a first Number: ')
        second = get_number('Enter a second Number: ')
        result = arithmetic_operation(first,second)
        print('Result:',result)
        while True:
            choice = input('continue with result(C),new calculation (N) or exit (E): ').upper()
            if choice in ['C','N','E']:
                break
            else:
                print('Invalid choice.Enter C,N or E')
        if choice == 'E':
            continue_cal = False
        if choice == 'N':
            result = None
if __name__ == "__main__":
    main()

            