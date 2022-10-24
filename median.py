"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

def findMedian(numbers):
    position = (len(numbers) - 1) / 2
    if (position % 1 != 0):
        position = int(position)
        median = (numbers[position] + numbers[position + 1]) / 2
    else:
        position = int(position)
        median = (numbers[position])
    return median
    
while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
        median = findMedian(numbers)
        print(f'The median is {median}')
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(numbers)
