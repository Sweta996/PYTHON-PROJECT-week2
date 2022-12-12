# looping in tuples,tuples with one element , tuple without parenthesis, tuple unpacking, list inside tuple, some funtions to use with tuples
mixed = (1,2,3,4.0)

# for loop and tuple
for i in mixed:
    print(i)
# Note - You can use while loop too

# tuple with one element
nums = (1,)
words = ('word1')
# print(type(nums))
# print(type(words))

# tuple without parenthesis
guitars = 'Yamaha', 'baton rouge', 'taylor'
# print(type(guitars))

# tuple packing
guitarists = ('Manali Jamal', 'Eddie Van Der Meer', 'Andrew Foy')
guatarist1, guitarist2, guitarist2 = (guitarists)
# print(guitarist1)


# list inside tuples
favourites = ('southern mangolia' , ['Tokyo Ghoul Theme', 'landscape'])
favouites[1].pop()
favourites[1].append("we made it")
# print(favourites)

# min(), max, sum
print(max(mixed))
