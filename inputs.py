def accept_value():
    while True:
        try:
            first_value = int(input("Enter first number:\n"))
        except:
            print("Error occoured")
            continue
        else:
            if (first_value < 0 or first_value > 255):
                print("Please, enter value between 0 and 255")
                continue
            break
            
    while True:
        try:
            second_value = int(input("Enter second number:\n"))
        except:
            print("Error occoured")
            continue
        else:
            if (second_value < 0 or second_value > 255):
                print("Please, enter value between 0 and 255")
                continue
            break
    return first_value, second_value

def convert_binary():
    first_value, second_value = accept_value()

    first_binary = []
    second_binary = []

    while first_value > 0:
        if first_value % 2 == 0:
            first_binary.insert(0, 0)
            first_value = first_value // 2
        elif first_value % 2 == 1:
            first_binary.insert(0, 1)
            first_value = first_value // 2
    
    while second_value > 0:
        if second_value % 2 == 0:
            second_binary.insert(0, 0)
            second_value = second_value // 2
        elif second_value % 2 == 1:
            second_binary.insert(0, 1)
            second_value = second_value // 2
    
    while len(first_binary) != 8:
        first_binary.insert(0, 0)

    while len(second_binary) != 8:
        second_binary.insert(0, 0)
    
    print(first_binary)
    print(second_binary)
    return first_binary, second_binary
