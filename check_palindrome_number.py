# Check Palindrome Number

def is_palindrome(num):
    return str(num) == str(num)[::-1]

num = 121
if is_palindrome(num):
    print(f"Original number {num}\nYes. Given number is a palindrome number")
else:
    print(f"Original number {num}\nNo. Given number is not a palindrome number")

num = 125
if is_palindrome(num):
    print(f"Original number {num}\nYes. Given number is a palindrome number")
else:
    print(f"Original number {num}\nNo. Given number is not a palindrome number")
