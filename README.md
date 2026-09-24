# Second Largest Number

## Explanation

This program finds the second largest unique number in a list.

## Problem Statement

Write a Python program to find the second largest distinct element from a list of numbers.

## Features

* Accepts a list of numbers
* Removes duplicate values
* Finds the largest values
* Displays the second largest number

## How It Works

The list is converted to a set to remove duplicates. The unique values are sorted in descending order, and the second value is selected.

## Technologies Used

* Python 3

## Data Structure Used

* List
* Set

## Methods Used

* `input()`
* `split()`
* `set()`
* `sorted()`

## Program Flow

1. Read numbers
2. Remove duplicates
3. Check whether at least two unique numbers exist
4. Sort the unique values
5. Display the second largest value

## Sample Input

```text
10 25 30 45 20
```

## Sample Output

```text
Second largest number: 30
```

## Time Complexity

O(n log n)

## Space Complexity

O(n)

## Key Learning

* Sets
* Lists
* Sorting
* Duplicate handling

## File Location

`second_largest.py`

## Repository Structure

```text
python-second-largest-number/
├── second_largest.py
└── README.md
```

## Author

V.Harini
