def total(a=5, *numbers, **phonebook):
    print('a', a)
    for single_item in numbers:
        print('single_item', single_item)
    for first_part, second_part in phonebook.items():
        print(first_part, second_part)

print(total(10, 1, 2, 3, Jack=1123, John=2231, Inge=1560))




#When we declare a starred parameter such as  *param , then all the positional arguments from that point till the end are collected as a tuple called 'param'. Similarly, when we declare a double-starred parameter such as  **param , then all the keyword arguments from that point till the end are collected as a dictionary called 'param'.

#Swaroop C H. A Byte of Python (Kindle 位置 1797-1801). GitBook. Kindle 版本.
