#Given Code :

numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
    if i % 2 == 0:
        numbers.remove(i)
print(numbers)

#1. What’s wrong with the code?

#The remove() method removes a value, not an index.
#→ The code is trying to remove the index number (i), but numbers.remove(i) looks for the actual value equal to i.
#So, when i = 0, Python tries to remove the value 0 (which doesn’t exist).
#Modifying a list (numbers) while looping over it causes index shifting, leading to skipped elements or incorrect removals.

#2. What will it output?

#Output: [1, 3, 5]
#it accidentally works because of the index shifting, but it’s not the intended behavior. (It accidentally works for this case, but for the wrong reason.)


#3. How to fix it?

#Solution 1: Iterate over a copy of the list
numbers = [1, 2, 3, 4, 5]
numbers = [i for i in numbers if i % 2 != 0]
print(numbers)  # Output: [1, 3, 5]

#Solution 2: Use list comprehension to create a new list
numbers = [1, 2, 3, 4, 5]
result = [num for num in numbers if num % 2 != 0]
print(result)  # Output: [1, 3, 5]
#Solution 3: Iterate backwards
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers) - 1, -1, -1):
    if numbers[i] % 2 == 0:
        numbers.remove(numbers[i])
print(numbers)  # Output: [1, 3, 5]

#Explanation
#The code iterates through the list of numbers and removes even numbers.
#The original code had a bug because it tried to remove elements while iterating over the same
#list, causing index shifting issues.
#The fixed versions either create a new list with only odd numbers or iterate backwards to avoid index
#shifting problems. The final output is a list containing only the odd numbers: [1, 3, 5].


