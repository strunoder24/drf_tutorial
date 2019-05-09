array = [1, 2, 3, 4, 5]

new_array = [x*3 for x in array if x > 2]

carrot = ((item, item) for item in array)

print(carrot)
