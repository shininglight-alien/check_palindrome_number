# Check Palindrome Number

def is_palindrome():
    num = int(input("Enter a number: "))
    return str(num) == str(num)[ ::-1]

if is_palindrome():
    print("Yes. The given is a palindrome number.")
else:
    print("No. The given is not a palindrome number.")

