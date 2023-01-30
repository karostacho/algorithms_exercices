
def find_fibonacci_sequence_for(n):
    x = []
    for i in range(2):
        x.append(i)
    while not len(x) == n:
        sum_of_two_last_numbers = x[-1] + x[-2]
        x.append(sum_of_two_last_numbers)
    print(x)
        
    
find_fibonacci_sequence_for(10)
