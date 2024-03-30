---
title: The Quicksort Algorithm
date: "2024-03-30T11:42:00.000Z"
description: "Understanding partition and recursion of the ubiquitously used sorting algorithm"
featuredAnimation: "quickSort"
user: "jdev9487"
---

## Background
A sorting algorithm is simply a set of steps taken to organise a collection of elements based on certain criteria. This could be ordering stories on social media sites so newer stories appear at the top. It could be ordering journeys in by their travel time. So long as there is a sense in which any element of the collection is *comparable* to any other then sorting can take place. The most obvious example of this would be a collection of integers. The "quicksort" algorithm is used frequently as the default choice for ordering. This post aims to explain how the algorithm works by understanding two of its key features: **partition** and **recursion**.

## Outline
`quicksort()` works by first partitioning the sequence of numbers into three groups:

1. one sorted element (pivot)
2. elements *smaller* than the pivot
3. elements *greater* than the pivot

Once the pivot has been sorted (placed in the correct place), the smaller elements get sorted by the same process, then the larger elements as well. This is a **recursive** process explained later.

## Procedure

### Partition
This is where actual sorting takes place. The recursive step, on the other hand, is just a demand that more partitioning occurs. The goal of the partition is to move one element to its correct position and ensure that all elements to the left are lower than it, and elements to the right are higher than it. So how does it work? Let's take an example: the numbers
$$
[2, 4, 1, 3]\,.
$$
The pivot is chosen to be the right-most element: $3$. Our goal is to place $3$ in the third position, have $1$ and $2$ to its left and have $4$ to its right.

This is done by using two markers - let's call them "upper" and "lower". The upper will move from the left all the way to the right (where the pivot is). The lower marker starts at the left and moves one place to the right only if the upper marker encounters an element less than or equal to the pivot (re-read this sentence as many times as necessary for it to make sense). If the upper marker visits just one element that greater than the pivot, then when the upper marker has traversed all elements, the lower marker will be one place behind it. This is the first reason for the lower marker; at the end it will show where the pivot should be:
$$
\begin{align*}
&\textrm{1 element greater than the pivot} \\
\implies 
&\textrm{lower marker 1 place behind upper marker} \\
\implies
&\textrm{lower marker now indicates where pivot should move}
\end{align*}
$$

The next purpose of the lower marker is to swap elements along the way. When the upper and lower markers are not at the same position, we swap the elements at their positions. This will be explained but may become obvious by seeing it in action using our example:

```
   u           p
  [2] [4] [1] [3]
l
```
Is upper less than or equal to pivot?... No. So lower catches up one spot.
```
   u           p
  [2] [4] [1] [3]
   l
```
Upper and lower at same position so no swapping. Let's increment upper again:
```
       u       p
  [2] [4] [1] [3]
   l
```
This time, the element at the upper marker position *is* greater than the pivot value (3). Now we do nothing with the lower marker; we have introduced the gap of one which will be needed at the end. Let's increment the top again:
```
           u   p
  [2] [1] [4] [3]
       l
```
Two things happened here. The element at the upper marker position (1) was less than the pivot so we caught the lower marker up one to the right. Now, since the upper and lower are out of sync, we swapped the elements at their positions (1 and 4). Note we still have a gap of 1 between lower and upper as required. Let's increment the top again, moving slowly for clarity:
```
               u/p
  [2] [1] [4] [3]
       l
```
Only the top marker was incremented. It is now at the pivot value so it guaranteed to be less than *or* equal to the pivot so we need to bring the lower marker one to the right:
```
               u/p
  [2] [1] [4] [3]
           l
```
Once a gap has been introduced between upper and lower, it cannot be eliminated. We know swap elements at upper and lower positions and the markers are removed:
```
           F
  [2] [1] [3] [4]
```
The pivot value of 3 is now in it's correct place (hence the F for "Fixed"). All elements to its left are less than it (2 and 1) and all elements to its right are greater than it (just 4 in this case).

The partition procedure can be summarized with pseudocode:
```
Place upper marker at start of collection;
Place lower marker one index before start of collection;

while upper index <= pivot index:
    if element at upper <= pivot value:
        increment lower index
        if upper index != lower index:
            swap element as upper and lower indexes
    increment upper index
```

Take a pen and paper, use the collection [2, 4, 1, 5, 3] with the algorithm above and ensure that two swaps are made along the way giving first [2, 1, 4, 5, 3] and then [2, 1, 3, 5, 4].

### Recursion
The partition step definitely involves a fair few processes but if you've never encountered recursion before it can be hard to get your head around. Pseudocode for `quicksort()` looks something like this:
```
quicksort(elements):
    pivot, smaller_elements, larger_elements = partition(elements)
    sorted_smaller = quicksort(smaller_elements)
    sorted_larger = quicksort(larger_elements)
    return sorted_smaller + [pivot] + sorted_larger
```
If we called `quicksort([2, 4, 1, 5, 3])`, we would find:

* `pivot = 3`
* `smaller_elements = [2, 1]`
* `larger_elements = [5, 4]`

In general, the pivot will always be correctly sorted in the sense that we could concatenate the smaller elements, the pivot and the larger elements together and it will always be in the correct position. `smaller_elements` and `larger_elements` will in general not be sorted however. The way we sort them is by *recursively* calling `quicksort()` on them.

At each stage in the recursion we correctly sort just one element; the pivot. Each further call to `quicksort()` sorts just one more element. When we arrive at calling `quicksort()` on a collection of just one element, we do nothing to it - it is already sorted. This should be reflected in the code so one amendment is necessary:
```
quicksort(elements):
    if length of elements is 1:
        return elements
    pivot, smaller_elements, larger_elements = partition(elements)
    sorted_smaller = quicksort(smaller_elements)
    sorted_larger = quicksort(larger_elements)
    return sorted_smaller + [pivot] + sorted_larger
```

## Conclusion
The quicksort algorithm falls into the "Divide and Conquer" approach. Split up the collection and repeat the process on the smaller collections. I best understand this sort by thinking about the recursion first. I assume there is a magic way to sort a collection into [lower elements], pivot and [higher elements]. Recursion ensures the sub collections will be sorted accordingly. I then turn my attention to the partitioning process which actually swaps elements and does sorting.
