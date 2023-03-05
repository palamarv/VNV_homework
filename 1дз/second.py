
# 2.* Наповнити список числами з клавіатури,
# знайти мінімальне і максимальне число в списку,
# не використовуючи функції min і max

some_string = input('Enter numbers: ')
check_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

number_list = []

for i in range(len(some_string)):
    if int(some_string[i]) in check_list:
    # перевірка на число
        number_list += some_string[i]
min_elem = sorted(number_list)
max_elem = sorted(number_list)

print("Max number: ", int(max_elem[0]))
print("Min_number: ", int(min_elem[-1]))

