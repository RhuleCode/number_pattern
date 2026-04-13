# number_pattern
A Python utility function that generates a space-separated string of integers from 1 to n with robust input validation.
## Number Pattern Generator

A simple Python function that returns a sequence of numbers as a formatted string.

### Functionality
The `number_pattern(n)` function takes a positive integer `n` and returns a string of numbers from `1` up to `n`, separated by spaces.

### Input Validation
The function includes error handling for:
* **Non-integer types:** Returns `"Argument must be an integer value."`
* **Values less than 1:** Returns `"Argument must be an integer greater than 0."`

### Usage
```python
print(number_pattern(4)) 
# Output: "1 2 3 4"

print(number_pattern("hello")) 
# Output: "Argument must be an integer value."
