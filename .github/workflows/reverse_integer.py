def reverse_integer(n):
    sign = -1 if n < 0 else 1
    n *= sign
    reversed_num = 0
    while n != 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10
    return sign * reversed_num

# Example usage
num = int(input("Enter an integer: "))
print("Reversed integer:", reverse_integer(num))