# LAB - Class 02

## Project: math-series

### Author: Yazan Alfarra

**How to initialize/run the application**

- You must install the requirements in the requirements.txt file
- python test_series.py -- To run the tests

**What does this repo includes**

This repo contains three functions:

1. **fibonacci_series**

Is a numeric series starting with the integers 0 and 1. In this series, the next integer is determined by summing the previous two. This function takes one required argument.

nth (int): fibonacci series up to the nth position starting from 0.

return (int): the fibonacci number to the nth position.

2. **lucas_series**

Is a numeric series starting with the integers 2 and 1. In this series, the next integer is determined by summing the previous two. This function takes one required argument.

nth (int): lucas series up to the nth position starting from 0.

return (int): the lucas number to the nth position.

3. **sum_series**

Is a numeric series starting with the integers 0 and 1 by default if not spicified. In this series, the next integer is determined by summing the previous two.

This function takes three arguments.

*required nth (int): series up to the nth position starting from 0.

**optional first_num (int): starting number in the series, if not provided will be 0.

**optional fsecond_num (int): second number in the series, if not provided will be 1.

return (int): the number to the nth position.