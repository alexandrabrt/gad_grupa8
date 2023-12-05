# my_dict = {
#     "key_1": 1,
#     "key_2": 2,
#     "key_3": 1,
#     "key_1": 4
# }
my_dict = {
    "key_1": 1,
    "key_2": 2,
    "key_3": 1,
}
# print(my_dict['key_2'])
# print(my_dict['key_4'])
# print(my_dict.get('key_2', "Nu exista"))
# print(my_dict.get('key_4', "Nu exista"))
# my_dict['key_5'] = 5
my_dict.update({"key_5": 5, "key_6": 6, "key_0": 7, "key_1": 100})
# print(my_dict.keys())
# print(my_dict.values())
print(my_dict.items())
my_dict["key_6"] = 10
print(my_dict.items())

# print(type(my_dict))
