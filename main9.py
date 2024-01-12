def process_list(input_list):
    input_number = int(input("Istalgan sonni kiriting: "))
    if input_number in input_list:
        input_list.remove(input_number)
        input_list.append(input_number)
        input_list.append(input_number)
        print(my_list)
    else:
        print("fatalnaya oshibka !!!!")

# Test qilish
my_list = [3, 6, 9, 12]
process_list(my_list)