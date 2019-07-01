def buggy_function1(vector, multiplier):
    output = {'max': max(vector*multiplier)}
    return output

def buggy_function2():
    calculation = buggy_function1(vector=[3,4,5], multiplier=3) # should return 15, right?
    output = calculation['maximum']
    return output

output = buggy_function2()
print(output)