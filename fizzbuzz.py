def fizzbuzz(i):
    if i % 3 == 0 or i % 5 == 0:
        if i % 3 == 0 and i % 5 != 0:
            return "Fizz"
        if i % 3 == 0 and i % 5 == 0:
            return "FizzBuzz"
        if i % 3 != 0 and i % 5 == 0:
            return "Buzz"
    else:
        return i

print(fizzbuzz(4))