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
---
## References

- [LeetCode Two Sum](https://leetcode.com/problems/two-sum/)
- [Array Data Structure](https://en.wikipedia.org/wiki/Array_data_structure)
