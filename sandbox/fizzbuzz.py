def fizzbuzz(i):
    for x in range(i, 100):
            if x % 15 == 0:
                print("Fizzbuzz")
            if x % 5 == 0:
                print("Fizz")
            elif x%10 == 0:
                print("Buzz")
            else:
                print(x)
fizzbuzz(20)
