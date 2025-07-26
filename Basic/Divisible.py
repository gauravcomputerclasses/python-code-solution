# Input a number and print whether it's a multiple of both 7 and 11 without using conditions

num = int(input("Enter a number: "))
is_multiple = (num % 7 == 0) and (num % 11 == 0)

print(f"The number {num} is a multiple of both 7 and 11: {is_multiple}")