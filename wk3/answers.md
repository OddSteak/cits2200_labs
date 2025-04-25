# CITS2200 Lab 1: Sorting and Searching

Name: Baasil Siddiqui

Student Number: 23895849


## Question 1 (1 mark)
Write a short paragraph explaining the relationship between this problem and more abstract computer science topics we have covered in class.

We can use sorting algorithm to sort the initial data in ascending order of (time, name) pairs
We can use searching algorithms to find ranks of new data

## Question 2 (1 mark)
What data do you need to store in the `Leaderboard` class?
What algorithm do you intend to use for each method?

a list of the (time, name) pairs need to be stored in sorted order
__init__ - merge sort
get_runs - return the stored data (constant time)
submit_run - binary search
get_rank_time - return the time of the runner with the given rank from the stored data (constant time)
get_possible_rank - binary search
count_time - binary search


## Question 3 (5 marks)
Implement your design by filling out the method stubs in `speedrunning.py`.
Your implementation must pass the tests given in `test_speedrunning.py`, which can be invoked by running `python -m unittest`.

See `speedrunning.py`.


## Question 4 (1 mark)
Give an argument for the correctness and complexity of your `__init__()` function.

I am using merge sorrt to sort the data
the time complexity is O(n * log n) because I am splitting the list recursively and merging them at every level, there are log n levels and the algorithm to merge two sorted lists has order of n1 + n2 complexity

## Question 5 (1 mark)
Give an argument for the correctness and complexity of your `submit_run()` function.

I am using binary search to find the correct rank to insert the runner at
time complexity of binary search is O(log n)
I am inserting the element at a position such that the next element is greater or equal to the given element and the previous element is lower than the given element.
in the worst case, to insert at the beginning of the list the time complexity would be O(n) since all the elements would have to be shifted to the right

complexity of the function is O(n)


## Question 6 (1 mark)
Give an argument for the correctness and complexity of your `count_time()` function.

I am using binary search to find a runner with the given time and then using two loops to look ahead an behind to count the number of runners with same time since the list is sorted

the complexity of binary saerch is O(log n) and the complexity of the finding the runners with equal times before and after the element is O(n)

so the complexity of the whole function is O(n).
