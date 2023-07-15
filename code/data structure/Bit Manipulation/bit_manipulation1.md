---
Crafted by [Genie](https://marketplace.visualstudio.com/items?itemName=genieai.chatgpt-vscode)

---

## You

Input: nums = [1,2,1,3,2,5]
Output: [3,5]
Explanation:  [5, 3] is also a valid answer.


## Genie

To get the output [3,5] (or [5,3]), we first need to find the numbers that appear only once in the given list. We can do this by iterating over the list and keeping track of the count of each number using a dictionary or a Counter object from the collections module.

Then, we can create a new list containing only those numbers that appear once and return it sorted in descending order to get the desired output.

Here's the code that implements this approach:

```python
from collections import Counter

def find_unique_nums(nums):
    count = Counter(nums)
    unique_nums = [num for num in count if count[num] == 1]
    return sorted(unique_nums, reverse=True)

nums = [1,2,1,3,2,5]
print(find_unique_nums(nums))  # Output: [5, 3] or [3, 5]
```

In this code, we first import the Counter class from the collections module. We then define a function named `find_unique_nums` that takes a list of integers as input and returns a list of unique integers sorted in descending order.

We create a `count` dictionary that maps each number to its count in the input list using the Counter class. We then filter the dictionary to only keep the numbers that occur exactly once and store them in the `unique_nums` list using a list comprehension.

Finally, we sort the `unique_nums` list in descending order using the sorted function with the `reverse=True` argument and return it as the result.

Note that since there are multiple valid outputs for this problem, this code will produce one of the possible outputs.

## You

Input: nums = [1,2,1,3,2,5]
Output: [3,5]
Explanation:  [5, 3] is also a valid answer.
using bit manipulation

## Genie

We can also solve this problem using bit manipulation, which is more efficient than the previous approach.

To do so, we use the XOR operator to cancel out all the pairs of the same numbers in the list. The result of this operation will be a number that represents the XOR of the two unique numbers in the list.

We can then use the bitwise AND operator with the two's complement of this XOR result to get the rightmost set bit (i.e., the bit that is 1 in one of the unique numbers and 0 in the other).

Using this bit, we can group all the numbers in the input list into two groups: one that has this bit set and the other that doesn't. We can then take the XOR of each group separately to get the two unique numbers.

Here's the code that implements this approach:

```python
def find_unique_nums(nums):
    # XOR of all nums gives XOR of two unique nubers
    xor_result = nums[0]
    for num in nums[1:]:
        xor_result ^= num

    # Get rightmost set bit
    rightmost_set_bit = xor_result & -xor_result

    # Group numbers based on rightmost set bit
    group_1, group_2 = 0, 0
    for num in nums:
        if num & rightmost_set_bit:
            group_1 ^= num
        else:
            group_2 ^= num

    return [group_1, group_2]

nums = [1,2,1,3,2,5]
print(find_unique_nums(nums))  # Output: [3, 5] or [5, 3]
```

In this code, we first define a function named `find_unique_nums` that takes a list of integers as input and returns a list of unique integers sorted in descending order.

We then calculate the XOR of all the numbers in the input list using a loop and store the result in `xor_result`.

Next, we use the bitwise AND operator with `-xor_result` (which is the two's complement of `xor_result`) to get the rightmost set bit. We store this value in `rightmost_set_bit`.

We then iterate over the input list again and group the numbers into two groups: one that has `rightmost_set_bit` set (i.e., its value is 1 in binary representation) and the other that doesn't. We use the XOR operator to calculate the unique number in each group and store them in `group_1` and `group_2`, respectively.

Finally, we return the two numbers as a list. Note that the order of the output may be different from the previous approach, but both outputs are valid.

## You

can u dry run with examples

## Genie

Sure! Let's use the input `nums = [1, 2, 1, 3, 2, 5]` to demonstrate how this bit manipulation approach works.

First, we calculate the XOR of all the numbers in the list:

```
1 ^ 2 ^ 1 ^ 3 ^ 2 ^ 5 = 6
```

The result is `6`, which is the XOR of the two unique numbers in the input list. We can represent `6` in binary as `110`.

Next, we get the rightmost set bit of the XOR result by taking its two's complement and performing a bitwise AND with the original result:

```
6 & -6 = 2
```

The two's complement of `6` is `-6`, which in binary is represented as `...11111010`. The bitwise AND of `6` and `(-6)` gives us `2`, which is the rightmost set bit of the XOR result. We can represent `2` in binary as `010`.

We then group the numbers in the input list based on whether their `010` bit (i.e., the second bit from the right) is set:

```
group_1: 2 (010), 3 (011), 5 (101)
group_2: 1 (001), 1 (001), 2 (010)
```

We can see that the two unique numbers must be in different groups, since they have different values for the `010` bit. We can then calculate the unique number in each group using the XOR operator:

```
group_1_result = 2 ^ 3 ^ 5 = 6
group_2_result = 1 ^ 1 ^ 2 = 2
```

Finally, we return `[6, 2]`. Note that the order of the output is different from the previous approach, but both outputs are valid.

## You

bit flip

## Genie

In computer science, the term "bit flip" refers to the operation of changing a single bit in a binary number from 0 to 1 or from 1 to 0. This operation can be performed using bitwise operators.

For example, let's say we have the binary number `0101` (which represents the decimal number 5), and we want to flip its second bit from the right (i.e., change the `0` to `1`):

```
0101 (original)
   ^
0111 (result)
```

We can perform this operation by doing a bitwise OR with the number `0010`, which has a `1` in its second bit:

```python
num = 0b0101     # binary representation of decimal 5
bit_mask = 0b0010  # binary number with a 1 in the second bit
result = num | bit_mask
print(bin(result))  # Output: 0b111 (binary representation of decimal 7)
```

In this code, we define the variable `num` to be equal to the binary representation of the decimal number `5`. We also define the `bit_mask` variable to be equal to a binary number with a `1` in the second bit. We then perform a bitwise OR of `num` and `bit_mask` to get the result. The output will be the binary representation of decimal `7`, which has the second bit flipped from `0` to `1`.

Likewise, if we want to flip the second bit from `1` to `0`, we can use a bitwise AND with a number that has a `0` in the second bit:

```python
num = 0b0111     # binary representation of decimal 7
bit_mask = 0b1101  # binary number with a 0 in the second bit
result = num & bit_mask
print(bin(result))  # Output: 0b0101 (binary representation of decimal 5)
```

In this code, we define the variable `num` to be equal to the binary representation of the decimal number `7`. We also define the `bit_mask` variable to be equal to a binary number with a `0` in the second bit. We then perform a bitwise AND of `num` and `bit_mask` to get the result. The output will be the binary representation of decimal `5`, which has the second bit flipped from `1` to `0`.