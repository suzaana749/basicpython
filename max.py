def max(x):
    result = 0
    for a in x:
        if result<a:
            result = a
    return result
x=[2,5,16,35,9,1]
print("maximum is",max(x))