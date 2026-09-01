def count_up(start, stop):
    current = start
    while current <= stop:
        yield current
        current += 1
gen = count_up(1, 5)
print(type(gen))       # resume here next time             # <class 'generator'>
for n in gen:
    print(n, end=' ')

"""Write a generator function prime_generator() that yields prime numbers infinitely.
Use it to print the first 10 primes.
 Explain why this would be impossible with a regular
  function returning a list for a truly infinite sequence.
 """
def prime_generator():
    num = 2

    while True:  # Infinite loop
        is_prime = True

        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            yield num

        num += 1


# Print the first 10 prime numbers
gen = prime_generator()

for j in range(10):
    print(next(gen))


