####### Control Flow #######
print('####### Control Flow #######');
num = float(input('Enter a Number ... '));

if num >= 0:
    if num==0:
        print('you Entered Zero');
    elif num > 2:
        print('you entered a positive number greater than 2');
    else:
        print("you entered a number less than 2");
elif num < 0:
    print('you entered a negative number');

print('###### While Loop ######')
num = int(input("Enter a number to calculate factorial ..."))
i = 1;
fact = 1;
while i < num+1:
    fact = fact*i;
    i=i+1;
print("Factorial of your number", num);
print(fact);
nums = [6,5,4,3,2,1];
total = 0;
for val in nums:
    total = total+val;
print('The sum of nums 6 to 1 is ' , total);
print('Traversing the word "statment" using for loop');
for val in "statment":
    if val == 'e':
        break;
    print(val);
print('End of for loop');
print('Traversing the word "python" using for loop');
for val in "python":
    if val == 'h':
        continue;
    print(val);
print('End of for loop');


print('######  Python Functions ######')

def addValues(x,y):
    return x+y;
print("Sum of 9 and 5 ..." ,addValues(5,9));

def calc_factorial(x):
    if x == 1:
        return 1
    else:
        return(x * calc_factorial(x-1))

num = 6
print("The factorial of", num, "is", calc_factorial(num)) 

    
