# 🎯 Two Sum

<div align="center">

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen)
![Topics](https://img.shields.io/badge/Topics-Array%20|%20Hash%20Table%20|%20Brute%20Force-blue)
![LeetCode](https://img.shields.io/badge/LeetCode-Problem-orange)

</div>

## 📋 Problem Description

Given an array of integers `nums` and an integer `target`, return **indices of the two numbers** such that they add up to `target`.

**Key Points:**
- You may assume that each input would have **exactly one solution**
- You **may not use the same element twice**
- You can return the answer in **any order**

---

## 💡 Examples

### Example 1
```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]
```

### Example 2
```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

### Example 3
```
Input: nums = [3,3], target = 6
Output: [0,1]
```

---

## 🚀 Approaches

### Approach 1: Brute Force

**Strategy:**
- Check every pair of numbers
- Nested loop approach

**Complexity Analysis:**
- **Time Complexity:** O(n²)
- **Space Complexity:** O(1)

**Implementation:**
```python
def twoSum(nums, target):
    """
    Brute force approach: Check all pairs
    """
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []  # No solution found
```

**Pros:**
- Simple to understand and implement
- No extra space required

**Cons:**
- Inefficient for large arrays
- Time complexity is quadratic

---

### Approach 2: Hash Map (Optimal) ⭐

**Strategy:**
- Use a hash map to store numbers and their indices
- For each number, check if `target - num` exists in the map
- Single pass solution

**Complexity Analysis:**
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

**Implementation:**
```python
def twoSum(nums, target):
    """
    Hash map approach: One-pass solution
    """
    value_to_index = {}
    
    for current_index, current_value in enumerate(nums):
        required_value = target - current_value
        
        if required_value in value_to_index:
            return [value_to_index[required_value], current_index]
        
        value_to_index[current_value] = current_index
    
    return []  # No solution found
```

**Pros:**
- Highly efficient - linear time
- Single pass through the array

**Cons:**
- Requires extra space for hash map

---

## 📊 Algorithm Visualization

```
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
```

---

## 🔍 Step-by-Step Walkthrough

**Example: nums = [2, 7, 11, 15], target = 9**

| Iteration | Index | Value | Required Value | Hash Map | Action |
|-----------|-------|-------|----------------|----------|---------|
| 1 | 0 | 2 | 9 - 2 = 7 | {} | 7 not found, add {2: 0} |
| 2 | 1 | 7 | 9 - 7 = 2 | {2: 0} | 2 found! Return [0, 1] |

**Result:** [0, 1] ✅

---

## 🎓 Key Takeaways

- **Hash maps** provide O(1) average lookup time
- **Trade-off:** Exchange space for time efficiency
- **Pattern recognition:** Complement-searching is a common technique in array problems
- **One-pass optimization:** Sometimes you can solve in a single iteration

---

## 🧪 Test Cases

```python
# Test Case 1: Normal case
assert twoSum([2, 7, 11, 15], 9) == [0, 1]

# Test Case 2: Different positions
assert twoSum([3, 2, 4], 6) == [1, 2]

# Test Case 3: Duplicate numbers
assert twoSum([3, 3], 6) == [0, 1]

# Test Case 4: Negative numbers
assert twoSum([-1, -2, -3, -4, -5], -8) == [2, 4]

# Test Case 5: Large target
assert twoSum([0, 4, 3, 0], 0) == [0, 3]
```

---

## 🔗 Related Problems

- **3Sum** (Medium) - Find triplets that sum to target
- **4Sum** (Medium) - Find quadruplets that sum to target
- **Two Sum II - Input Array Is Sorted** (Medium) - Two-pointer approach
- **Two Sum III - Data Structure Design** (Easy) - Design data structure
- **Subarray Sum Equals K** (Medium) - Continuous subarray sum

---

## 📚 References

- [LeetCode: Two Sum](https://leetcode.com/problems/two-sum/)
- [Array Data Structure](https://en.wikipedia.org/wiki/Array_data_structure)
- [Hash Table Fundamentals](https://en.wikipedia.org/wiki/Hash_table)
- [Time Complexity Analysis](https://en.wikipedia.org/wiki/Time_complexity)

---

## ⚙️ Running the Solution

```bash
# Save the code to a file
# two_sum.py

# Run with Python
python two_sum.py

# Or run tests
pytest test_two_sum.py -v
```

---

## 🌟 Comparison Table

| Approach | Time Complexity | Space Complexity | Best For |
|----------|----------------|------------------|----------|
| Brute Force | O(n²) | O(1) | Small arrays, learning |
| Hash Map | O(n) | O(n) | Production, large datasets |
| Two Pointers* | O(n log n) | O(1) | Sorted arrays |

*Two Pointers requires sorting first, applicable for "Two Sum II"

---

<div align="center">

**Happy Coding!** 💻

[![LeetCode](https://img.shields.io/badge/LeetCode-Profile-yellow?logo=leetcode)](https://leetcode.com/yourusername)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-black?logo=github)](https://github.com/yourusername)

</div>

---

## 📝 Notes

- This is one of the most frequently asked interview questions
- Master this pattern as it applies to many similar problems
- Practice both approaches to understand the trade-offs
- Consider edge cases: empty arrays, single element, duplicates
