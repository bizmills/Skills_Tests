# Things you should be able to do.

# DONE Write a function that takes a list and returns a new list with only the odd numbers.
def all_odd(some_list):
    odd_numbers = []
    for numbers in range(len(some_list)):
        if numbers % 2 != 0:
            odd_numbers.append(numbers)
    return odd_numbers

# DONE Write a function that takes a list and returns a new list with only the even numbers.
def all_even(some_list):
    even_numbers=[]
    for numbers in range(len(some_list)):
        if numbers % 2 == 0:
            even_numbers.append(numbers)
    return numbers


#DONE Write a function that takes a list of strings and a new list with all strings of length 4 or greater.
def long_words(word_list):
    new_list = []
    words = word_list[0]
    for words in word_list:
        if (len(words)) >= 4:
            new_list.append(words)
    words += 1 
    return new_list

# Write a function that finds the smallest element in a list of integers and returns it.
def smallest(some_list):
    smallest_num = min(some_list)
    return smallest_num

# Write a function that finds the largest element in a list of integers and returns it.
def largest(some_list):
    largest_num = max(some_list)
    return largest_num

# DONE Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(some_list):
    div_num = 2
    new_list = [num/div_num for num in some_list]
    return new_list

# DONE Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lengths(word_list):
    count = [0]
    for words in range(len(word_list)):
        count[word_list[words]-1]+=1

    return word_list

# DONE Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(numbers):
    sums = 0
    for num in numbers:
        sums += num
    return sums

# DONE Write a function that multiplies all the numbers in a list together.
def mult_numbers(numbers):
    mults = 1
    for i in range(len(numbers)):
        mults *= i
    return mults

#DONE Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
def join_strings(string_list):
    list_of_strings = ""
    for str in string_list:
        list_of_strings = list_of_strings + str
    return list_of_strings

# DONE Write a function that takes a list of integers and returns the average (without using the avg method)
def average(numbers):
    average = (float(sum(numbers) / len(numbers)))
    return average
