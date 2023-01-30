def find_integers_not_greater_than_n():
    n = input("Please enter an integer <= 0 \n")
    if not n.isdigit():
        return find_integers_not_greater_than_n()
    n = int(n)
    list_of_integers = []
    for i in range(n):
        list_of_integers.append(i+1)
    return list_of_integers

def return_factorial():   
    list_of_integers = find_integers_not_greater_than_n()
    factorial = 1
    for i in list_of_integers:
        factorial = factorial*i
    print(factorial)
    
return_factorial()   
