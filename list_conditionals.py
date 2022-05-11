# numbers = range(1, 11)
# print(numbers)
# evens_squared = []
# for number in numbers:
#     if number % 2 == 0:
#         evens_squared.append(number * number)

# print(evens_squared)

#evens_squared = [expression for item in list if condition]

# evens_squared = [number * number for number in range(1, 11) if number % 2 == 0]
# print(evens_squared)


# chicken_names = ["Hen Solo", "Cluck Norris", "Hennifer Lopez", "ChewPekka", "Feather Locklear"] 

# found_over_10 = [name for name in chicken_names if len(name) > 10]
# print(found_over_10)

# found_letter_h = [name for name in chicken_names if name[0] == 'H']
# print(found_letter_h)

words = ["The", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]
first_letters = [word[0] for word in words]
print(first_letters)