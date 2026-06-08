#######################
#   関数を変数に代入   #
#    Func-let3.py     #
#######################

def calc_5_3(func):
    return func(5, 3)

result = calc_5_3(lambda a, b: a * b)
print(result)

# The calc_5_3 function takes another function as an argument and applies it to the numbers 5 and 3.
# In this case, the passed function is a lambda function that multiplies its two arguments.
# Therefore, the final result is the product of 5 and 3, which is 15.