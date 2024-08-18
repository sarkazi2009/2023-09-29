my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
list1 = 0
while list1 < len(my_list):
    if my_list[list1] > 0:
        print(my_list[list1])
    list1 += 1
    if my_list[list1] < 0:
        break
