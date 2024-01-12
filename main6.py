def find_and_return_odd_repeating_number(input_list):
    odd_repeating_number = None
    counts = {}
    index = 0

    while index < len(input_list):
        current_number = input_list[index]
        if current_number in counts:
            counts[current_number] += 1
        else:
            counts[current_number] = 1
        index += 1

    for number, count in counts.items():
        if count % 2 != 0:
            odd_repeating_number = number
    print(odd_repeating_number)

my_list = [1, 2, 3, 4, 5, 3, 2, 7, 7, 8, 9, 1]

result = find_and_return_odd_repeating_number(my_list)
print("Qaytalanib kelayotgan toq son:", result)