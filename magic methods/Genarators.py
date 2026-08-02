def count_up(start, stop):
    current = start
    while current <= stop:
        yield current
        current += 1
gen = count_up(1, 5)
print(type(gen))       # resume here next time             # <class 'generator'>
for n in gen:
    print(n, end=' ')

