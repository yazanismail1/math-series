def fibonacci_series(nth):
    '''
Is a numeric series starting with the integers 0 and 1. In this series, the next integer is determined by summing the previous two. This function takes one required argument.

nth (int): fibonacci series up to the nth position starting from 0.

return (int): the fibonacci number to the nth position.
    '''
    if type(nth) != int:
        return "Please enter a positive integer"
    if nth < 0:
        return "Please enter a positive integer"
    if nth == 0:
      return 0
    elif nth == 1:
      return 1
    else:
        return (fibonacci_series(nth-2) + fibonacci_series(nth-1))

def lucas_series(nth):
    '''
Is a numeric series starting with the integers 2 and 1. In this series, the next integer is determined by summing the previous two. This function takes one required argument.

nth (int): lucas series up to the nth position starting from 0.

return (int): the lucas number to the nth position.
    '''
    if type(nth) != int:
        return "Please enter a positive integer"
    if nth < 0:
        return "Please enter a positive integer"
    if nth == 0:
      return 2
    elif nth == 1:
      return 1
    else:
        return (lucas_series(nth-2) + lucas_series(nth-1))
    
def sum_series(nth, first_num=0, second_num=1):
    '''
Is a numeric series starting with the integers 0 and 1 by default if not spicified. In this series, the next integer is determined by summing the previous two.

This function takes three arguments.

*required nth (int): series up to the nth position starting from 0.

**optional first_num (int): starting number in the series, if not provided will be 0.

**optional fsecond_num (int): second number in the series, if not provided will be 1.

return (int): the number to the nth position.
    '''
    if type(nth) != int:
        return "Please enter a positive integer"
    if nth < 0:
        return "Please enter a positive integer"
    if first_num == 0 and second_num == 1:
      return fibonacci_series(nth)
    elif first_num == 2 and second_num == 1:
      return lucas_series(nth)
    else:
      if nth == 0:
        return first_num
      elif nth == 1:
        return second_num
      else:
        return (sum_series(nth-2, first_num=first_num, second_num=second_num) + sum_series(nth-1, first_num=first_num, second_num=second_num))
    
if __name__ == "__main__":
    print("-------------------")
    print("Fibonacci Series - 10th position: ",fibonacci_series(10))
    print("-------------------")
    print("Lucas Series - 10th position: ",lucas_series(10))
    print("-------------------")
    print("Sum Series --> Fibonacci Series | without the optional args - 10th position: ",sum_series(10))
    print("-------------------")
    print("Sum Series --> Fibonacci Series | with the optional args - 10th position: ",sum_series(10,first_num=0,second_num=1))
    print("-------------------")
    print("Sum Series --> Lucas Series | with the optional args - 10th position: ",sum_series(10,first_num=2,second_num=1))
    print("-------------------")
    print("Sum Series --> Random Series | with the optional args - 10th position: ",sum_series(10,first_num=5,second_num=8))
    print("-------------------")
