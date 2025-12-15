def number_pattern_generator():
    n=int(input("Enter a number: "))
    if not isinstance(n, int):
        return "Argument must be an integer."
    if n<=0:
        return "Argument must be greater than 0."
    result=[]
    for i in range(1, n+1):
        result.append(str(i))
    return  " ".join(result)

print(number_pattern_generator())