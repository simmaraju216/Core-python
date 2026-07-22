# # ==========================================
# # Q1. PARAMETERS + LAMBDA
# # ==========================================
#
# def apply_operation(a, b, op):
#     return op(a, b)
#
# print("Q1 Output:")
# print("Addition      :", apply_operation(10, 5, lambda x, y: x + y))
# print("Subtraction   :", apply_operation(10, 5, lambda x, y: x - y))
# print("Multiplication:", apply_operation(10, 5, lambda x, y: x * y))
# print()
#
#
# # ==========================================
# # Q2. *args + RECURSION
# # ==========================================
#
# def recursive_sum(*args):
#     if len(args) == 0:
#         return 0
#     elif len(args) == 1:
#         return args[0]
#     else:
#         return args[0] + recursive_sum(*args[1:])
#
# print(recursive_sum(10, 20, 30, 40, 50))
# print()
#
#
# # ==========================================
# # Q3. DEFAULT + KEYWORD + LAMBDA
# # ==========================================
#
# def make_greeting(name, prefix="Hello", formatter=lambda x: x):
#     message = f"{prefix}, {name}"
#     return formatter(message)
#
# print("Q3 Output:")
# print(make_greeting("Raju"))
# print(make_greeting("Raju", prefix="Welcome"))
# print(make_greeting("Raju", formatter=str.upper))
# print()
#
#
# # ==========================================
# # Q4. map() + filter() + lambda
# # ==========================================
#
# numbers = list(range(1, 21))
#
# result = list(
#     map(
#         lambda x: x ** 2,
#         filter(lambda x: x % 3 == 0, numbers)
#     )
# )
#
# print("Q4 Output:")
# print(result)
#
# # ==========================================
# # Q5. FUNCTION REFERENCE + HIGHER ORDER
# # ==========================================
#
# double = lambda x: x * 2
# triple = lambda x: x * 3
# quadruple = lambda x: x * 4
#
# functions = [double, triple, quadruple]
#
# def apply_all(funcs, value):
#     for func in funcs:
#         value = func(value)
#     return value
#
# print("Q5 Output:")
# print(apply_all(functions, 2))
# print()
#
#
# # ==========================================
# # Q6. RECURSION + DEFAULT PARAMETER
# # ==========================================
#
# def flatten(lst, depth=1):
#     result = []
#
#     for item in lst:
#         if isinstance(item, list) and depth > 0:
#             result.extend(flatten(item, depth - 1))
#         else:
#             result.append(item)
#
#     return result
#
# print("Q6 Output:")
# print(flatten([[1, [2]], 3], depth=2))
# print()
#
#
# # ==========================================
# # Q7. **kwargs + reduce()
# # ==========================================
#
# from functools import reduce
#
# def weighted_average(**scores):
#     values = list(scores.values())
#
#     total = reduce(lambda x, y: x + y, values)
#
#     return total / len(values)
#
# print("Q7 Output:")
# print(weighted_average(Math=90, English=80, Science=85))
# print()
#
#
# ==========================================
# Q8. FULL PIPELINE
# ==========================================

students = [
    {"name": "Raju", "score": 85},
    {"name": "Anil", "score": 45},
    {"name": "Sita", "score": 72},
    {"name": "Kiran", "score": 60}
]

passed = filter(lambda s: s["score"] >= 60, students)

graded = map(
    lambda s: {**s, "grade": "Pass"},
    passed
)

result = sorted(
    graded,
    key=lambda s: s["score"],
    reverse=True
)
for student in result:
    print(student)
print()

# #
# # ==========================================
# # Q9. LAMBDA + sorted() + FUNCTION REFERENCE
# # ==========================================
#
# students = [
#     ("Raju", 85),
#     ("Anil", 45),
#     ("Sita", 72),
#     ("Kiran", 60)
# ]
#
# strategies = {
#     "by_name": lambda x: x[0],
#     "by_score": lambda x: x[1],
#     "by_length": lambda x: len(x[0])
# }
#
# choice = input("Enter strategy (by_name/by_score/by_length): ")
#
# if choice in strategies:
#     sorted_list = sorted(students, key=strategies[choice])
#     print(sorted_list)
# else:
#     print("Invalid Choice")
#
# print()


# ==========================================
# Q10. ALL CONCEPTS
# ==========================================

# from functools import reduce
# def calculator(*args, operation="add", **options):
#     operations = {
#         "add": lambda nums: reduce(lambda x, y: x + y, nums),
#         "multiply": lambda nums: reduce(lambda x, y: x * y, nums),
#         "max": lambda nums: reduce(lambda x, y: x if x > y else y, nums),
#         "min": lambda nums: reduce(lambda x, y: x if x < y else y, nums)
#     }
#     if options.get("show_steps", False):
#         print("Numbers:", args)
#         print("Operation:", operation)
#     return operations[operation](args)
#
# print(calculator(10, 20, 30))
# print(calculator(2, 3, 4, operation="multiply"))
# print(calculator(10, 25, 5, operation="max"))
# print(calculator(10, 25, 5, operation="min"))
# print(calculator(1, 2, 3, 4, operation="add", show_steps=True))