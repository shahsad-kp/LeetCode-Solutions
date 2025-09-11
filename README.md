# LeetCode Runner

> ⚠️ **This project is built purely for personal use** — to test and run LeetCode-style problems locally with both manual and automatic test inputs.

---

## 📌 Overview

This CLI utility allows you to:
- Store all LeetCode-style Python problems inside a `questions/` directory.
- Run solutions either manually (with your own input) or automatically (with test cases).
- Quickly test methods via the terminal without needing any web interface.

---

## 🏃 Usage

### 🔧 Manual Input Mode

```bash
python run_solution.py --question 1 --mode m
# You will be prompted for input Or pass inputs directly:
python run_solution.py --question 1 --mode m --inputs "[10, 20]"
```

### 🤖 Automatic Test Case Mode
```bash
python run_solution.py --question 1 --mode a
```

### 🧪 No Flags? No Problem
You can also run without flags, and the script will interactively ask for inputs:
```bash
python run_solution.py
```
---

## 🧠 Question File Format

All problem files go inside the questions/ folder and must define a Solution class with:

* `__question__`: a short string description of the problem.

* `__test_cases__`: a list of test cases with input and output.

* One method that solves the problem.

### Example: questions/1.py
```python
class Solution:
    __question__ = "Add two numbers"
    __test_cases__ = [
        {"input": [1, 2], "output": 3},
        {"input": [5, 10], "output": 15},
    ]

    def add(self, a: int, b: int) -> int:
        return a + b
```
---

## 📂 Questions

| # | LeetCode Number | Title | LeetCode Link | Solutions | Is Passed |
|---|-----------------|-------|---------------|-----------|-----------|
| 1 | 100 | Same Tree | [Link](https://leetcode.com/problems/same-tree) | [Solutions](questions/100.py) | ✅ |
| 2 | 101 | Symmetric Tree | [Link](https://leetcode.com/problems/symmetric-tree) | [Solutions](questions/101.py) | ✅ |
| 3 | 104 | Maximum Depth of Binary Tree | [Link](https://leetcode.com/problems/maximum-depth-of-binary-tree) | [Solutions](questions/104.py) | ❌ |
| 4 | 108 | Convert Sorted Array to Binary Search Tree | [Link](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree) | [Solutions](questions/108.py) | ✅ |
| 5 | 111 | Minimum Depth of Binary Tree | [Link](https://leetcode.com/problems/minimum-depth-of-binary-tree) | [Solutions](questions/111.py) | ✅ |
| 6 | 112 | Path Sum | [Link](https://leetcode.com/problems/path-sum) | [Solutions](questions/112.py) | ✅ |
| 7 | 118 | Pascal's Triangle | [Link](https://leetcode.com/problems/pascals-triangle) | [Solutions](questions/118.py) | ✅ |
| 8 | 121 | Best Time to Buy and Sell Stock | [Link](https://leetcode.com/problems/best-time-to-buy-and-sell-stock) | [Solutions](questions/121.py) | ✅ |
| 9 | 125 | Valid Palindrome | [Link](https://leetcode.com/problems/valid-palindrome) | [Solutions](questions/125.py) | ✅ |
| 10 | 136 | Single Number | [Link](https://leetcode.com/problems/single-number) | [Solutions](questions/136.py) | ✅ |
| 11 | 141 | Linked List Cycle | [Link](https://leetcode.com/problems/linked-list-cycle) | [Solutions](questions/141.py) | ❌ |
| 12 | 144 | Binary Tree Preorder Traversal | [Link](https://leetcode.com/problems/binary-tree-preorder-traversal) | [Solutions](questions/144.py) | ✅ |
| 13 | 145 | Binary Tree Postorder Traversal | [Link](https://leetcode.com/problems/binary-tree-postorder-traversal) | [Solutions](questions/145.py) | ✅ |
| 14 | 160 | Intersection of Two Linked Lists | [Link](https://leetcode.com/problems/intersection-of-two-linked-lists) | [Solutions](questions/160.py) | ✅ |
| 15 | 168 | Excel Sheet Column Title | [Link](https://leetcode.com/problems/excel-sheet-column-title) | [Solutions](questions/168.py) | ✅ |
| 16 | 169 | Majority Element | [Link](https://leetcode.com/problems/majority-element) | [Solutions](questions/169.py) | ✅ |
| 17 | 171 | Excel Sheet Column Number | [Link](https://leetcode.com/problems/excel-sheet-column-number) | [Solutions](questions/171.py) | ✅ |
| 18 | 2 | Add Two Numbers | [Link](https://leetcode.com/problems/add-two-numbers) | [Solutions](questions/2.py) | ✅ |
| 19 | 205 | Isomorphic Strings | [Link](https://leetcode.com/problems/isomorphic-strings) | [Solutions](questions/205.py) | ✅ |
| 20 | 217 | Contains Duplicate | [Link](https://leetcode.com/problems/contains-duplicate) | [Solutions](questions/217.py) | ✅ |
| 21 | 226 | Invert Binary Tree | [Link](https://leetcode.com/problems/invert-binary-tree) | [Solutions](questions/226.py) | ✅ |
| 22 | 228 | Summary Ranges | [Link](https://leetcode.com/problems/summary-ranges) | [Solutions](questions/228.py) | ✅ |
| 23 | 242 | Valid Anagram | [Link](https://leetcode.com/problems/valid-anagram) | [Solutions](questions/242.py) | ✅ |
| 24 | 257 | Binary Tree Paths | [Link](https://leetcode.com/problems/binary-tree-paths) | [Solutions](questions/257.py) | ✅ |
| 25 | 258 | Add Digits | [Link](https://leetcode.com/problems/add-digits) | [Solutions](questions/258.py) | ❌ |
| 26 | 263 | Ugly Number | [Link](https://leetcode.com/problems/ugly-number) | [Solutions](questions/263.py) | ✅ |
| 27 | 268 | Missing Numbers | [Link](https://leetcode.com/problems/missing-number) | [Solutions](questions/268.py) | ✅ |
| 28 | 283 | Move Zeroes | [Link](https://leetcode.com/problems/move-zeroes) | [Solutions](questions/283.py) | ✅ |
| 29 | 290 | Word Pattern | [Link](https://leetcode.com/problems/word-pattern) | [Solutions](questions/290.py) | ✅ |
| 30 | 3487 | Maximum Unique Subarray Sum After Deletions | [Link](https://leetcode.com/problems/maximum-unique-subarray-sum-after-deletion) | [Solutions](questions/3487.py) | ✅ |
| 31 | 61 | Rotate List | [Link](https://leetcode.com/problems/rotate-list/) | [Solutions](questions/61.py) | ✅ |
| 32 | 88 | Merge Sorted Array | [Link](https://leetcode.com/problems/merge-sorted-array) | [Solutions](questions/88.py) | ✅ |
| 33 | 9 | Palindrome Number | [Link](https://leetcode.com/problems/palindrome-number) | [Solutions](questions/9.py) | ✅ |

## 🧪 Test Case Format
Each test case should be a dict like:
```python
{
    "input": [args_as_list],
    "output": expected_result
}
```
Arguments will be unpacked as *args when calling the solution method.

---
## 📦 Requirements
Python 3.8 or higher\
No external dependencies — pure standard library

---
## 💡 Why I Made This
I prefer running problems locally in a fast, keyboard-only dev flow.\
This tool mimics the LeetCode experience but fully offline.\
It lets me write, test, and refine solutions quickly without leaving my editor or terminal.

---
## 📜 License
MIT License\
But again — this is a personal project, not intended as a library, SDK, or public package.