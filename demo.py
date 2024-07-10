# name = input('Enter your name: ')
# print(f'Hello {name}!')

list = ['aadvi', 'preethi', 'raavan', 'chinna']

reversed_list =  [name[::-1] for name in list]
print(reversed_list)

res = reversed_list[::-1]
print(res)

reversed_list2 =  [name[::-1] for name in res]
print(reversed_list2)
sorted_list = sorted(reversed_list2)
final_list = (n.title() for n in sorted_list)
print(type(final_list))
