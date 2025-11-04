# Two Sum

**Difficulty:** Easy

**Topics:** Arrays, Hash Table, Brute Force

---

## Problem Description

Given an array of integers `nums` and an integer `target`, return **indices of the two numbers** such that they add up to `target`.

- You may assume that each input would have **exactly one solution**, and you **may not use the same element twice**.
- You can return the answer in **any order**.

---

## Examples

**Example 1:**

Input: nums = [2,7,11,15], target = 9

Output: [0,1]


**Example 2:**

Input: nums = [3,2,4], target = 6

Output: [1,2]


**Example 3:**

Input: nums = [3,3], target = 6

Output: [0,1]


---



---
## Approaches

### 1. Brute Force
- Check every pair of numbers.
- **Time Complexity:** O(n²)
- **Space Complexity:** O(1)

### 2. Hash Map (Optimal)
- Use a hash map to store numbers and their indices.
- For each number, check if `target - num` exists in the map.
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

TWO SUM PROBLEM (HASH MAP METHOD)
│
├── Input:
│     ├── numbers = [2, 7, 11, 15]
│     └── target_sum = 9
│
├── Step 1: Initialize empty hash map
│     └── value_to_index = {}
│
├── Step 2: Iterate over list using enumerate()
│
│   ┌────────────────────────────────────────────┐
│   │ For each (current_index, current_value):   │
│   └────────────────────────────────────────────┘
│
│     ├── Compute required_value = target_sum - current_value
│     │
│     ├── Check if required_value exists in hash map:
│     │       ├── YES → return [value_to_index[required_value], current_index]
│     │       └── NO  → store current_value in hash map:
│     │                value_to_index[current_value] = current_index
│     │
│     └── Continue loop
│
├── Step 3: If no pair found (edge case) → return None or raise exception
│
└── Output:
      ├── Pair of indices [i, j]
      └── Where numbers[i] + numbers[j] = target_sum

---
## References

- [LeetCode Two Sum](https://leetcode.com/problems/two-sum/)
- [Array Data Structure](https://en.wikipedia.org/wiki/Array_data_structure)
