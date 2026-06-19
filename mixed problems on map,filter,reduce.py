# def mystery(*args, **kwargs):
#     print(sum(args), list(kwargs.values()))
# mystery(1, 2, 3, a=4, b=5)
#
# def f(n):
#     if n == 0: return 0
#     return n + f(n - 1)
# print(f(4))
#
# from functools import reduce
# data=[2,3,4]
# r=reduce(lambda a,b:a*b,list(map(lambda x: x + 1, data)))
# print(r)
#
def Trees(fruit_type, fruit_count):

    d = {
        "mangoes": 2,
        "apple": 3,
        "orange": 1.5,
        "banana": 1,
        "grapes": 2
    }

    def time_taken(monkey_count):
        total_time = (fruit_count * d[fruit_type]) / monkey_count
        print("Time taken =", total_time)

    return time_taken


T1 = Trees("mangoes", 20)
T1(20)

T2 = Trees("apple", 5)
T2(3)