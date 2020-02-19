print('##### Taking input from keyboard ######');
userName = input('What is your name ... ');
print('Hello ', userName);
# Output: <class>
print('type of 5 ',type(5))

# Output: <class>
print('type of 5.0 ',type(5.0))

# <class>
c = 5 + 3j
print('type of c = 5 + 3j ',type(c));
print(' ######### Python Data Structures ######### ');
my_list = ['1', 'one', '22', 'two'];
my_list2 = [11,12,10,4.2,7];
print(my_list[1]);
print('List is mutable and tuple is imutable');
my_list[1] = '1';
print(my_list[1]);
print(my_list2);

language = ("French", "German", "English", "Polish");
print(language);
print('Length is ' , len(language));

del language;
#print('Length is ' , len(language));
# NameError: name 'language' is not defined
#if language:  print(language);

# set of integers
my_set = {1, 2, 3}
print(my_set)

# set of mixed datatypes
my_set = {1.0, "Hello", (1, 2, 3)}

print(my_set)


numbers = range(1, 6)

print(list(numbers)) # Output: [1, 2, 3, 4, 5]
print(tuple(numbers)) # Output: (1, 2, 3, 4, 5)
print(set(numbers)) # Output: {1, 2, 3, 4, 5}

# Output: {1: 99, 2: 99, 3: 99, 4: 99, 5: 99} 
print(dict.fromkeys(numbers, 99))
