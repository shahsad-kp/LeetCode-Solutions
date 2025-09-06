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
| 1 | 100 | Same Tree | [Link](https://leetcode.com/problems/same-tree) | [Solutions](questions/100.py) | True |
| 2 | 101 | Symmetric Tree | [Link](https://leetcode.com/problems/symmetric-tree) | [Solutions](questions/101.py) | True |
| 3 | 104 | Maximum Depth of Binary Tree | [Link](https://leetcode.com/problems/maximum-depth-of-binary-tree) | [Solutions](questions/104.py) | False |
| 4 | 108 | Convert Sorted Array to Binary Search Tree | [Link](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree) | [Solutions](questions/108.py) | True |
| 5 | 111 | Minimum Depth of Binary Tree | [Link](https://leetcode.com/problems/minimum-depth-of-binary-tree) | [Solutions](questions/111.py) | True |
| 6 | 112 | Path Sum | [Link](https://leetcode.com/problems/path-sum) | [Solutions](questions/112.py) | True |
| 7 | 118 | Pascal's Triangle | [Link](https://leetcode.com/problems/pascals-triangle) | [Solutions](questions/118.py) | True |
| 8 | 121 | Best Time to Buy and Sell Stock | [Link](https://leetcode.com/problems/best-time-to-buy-and-sell-stock) | [Solutions](questions/121.py) | True |
| 9 | 125 | Valid Palindrome | [Link](https://leetcode.com/problems/valid-palindrome) | [Solutions](questions/125.py) | True |
| 10 | 136 | Single Number | [Link](https://leetcode.com/problems/single-number) | [Solutions](questions/136.py) | True |
| 11 | 141 | Linked List Cycle | [Link](https://leetcode.com/problems/linked-list-cycle) | [Solutions](questions/141.py) | False |
| 12 | 144 | Binary Tree Preorder Traversal | [Link](https://leetcode.com/problems/binary-tree-preorder-traversal) | [Solutions](questions/144.py) | True |
| 13 | 145 | Binary Tree Postorder Traversal | [Link](https://leetcode.com/problems/binary-tree-postorder-traversal) | [Solutions](questions/145.py) | True |
| 14 | 160 | Intersection of Two Linked Lists | [Link](https://leetcode.com/problems/intersection-of-two-linked-lists) | [Solutions](questions/160.py) | True |
| 15 | 168 | Excel Sheet Column Title | [Link](https://leetcode.com/problems/excel-sheet-column-title) | [Solutions](questions/168.py) | True |
| 16 | 169 | Majority Element | [Link](https://leetcode.com/problems/majority-element) | [Solutions](questions/169.py) | True |
| 17 | 171 | Excel Sheet Column Number | [Link](https://leetcode.com/problems/excel-sheet-column-number) | [Solutions](questions/171.py) | True |
| 18 | 2 | Add Two Numbers | [Link](https://leetcode.com/problems/add-two-numbers) | [Solutions](questions/2.py) | True |
| 19 | 258 | Add Digits | [Link](https://leetcode.com/problems/add-digits) | [Solutions](questions/258.py) | False |
| 20 | 263 | Ugly Number | [Link](https://leetcode.com/problems/ugly-number) | [Solutions](questions/263.py) | True |
| 21 | 3487 | Maximum Unique Subarray Sum After Deletions | [Link](https://leetcode.com/problems/maximum-unique-subarray-sum-after-deletion) | [Solutions](questions/3487.py) | True |
| 22 | 88 | Merge Sorted Array | [Link](https://leetcode.com/problems/merge-sorted-array) | [Solutions](questions/88.py) | True |
| 23 | 9 | Palindrome Number | [Link](https://leetcode.com/problems/palindrome-number) | [Solutions](questions/9.py) | True |

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