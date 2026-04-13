def number_pattern(n):
     
    if not isinstance(n,int):
        return  'Argument must be an integer value.'
    if n<1:
        return  'Argument must be an integer greater than 0.'
    result=[]
    for i ,_ in enumerate(range(n)):
        result.append(str(i + 1))
    
    return " ".join(result)
#Example of number_pattern  
n=4
n=12    
print(number_pattern(n))
