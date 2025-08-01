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

| # | Title | LeetCode Link | Solutions |
|---|-------|--------------|-----------|
| 100 | Same Tree | [Link](https://leetcode.com/problems/same-tree) | [Solutions](questions/100.py) |
| 101 | Symmetric Tree | [Link](https://leetcode.com/problems/symmetric-tree) | [Solutions](questions/101.py) |
| 104 | Maximum Depth of Binary Tree | [Link](https://leetcode.com/problems/maximum-depth-of-binary-tree) | [Solutions](questions/104.py) |
| 112 | Path Sum | [Link](https://leetcode.com/problems/path-sum) | [Solutions](questions/112.py) |
| 118 | Pascal's Triangle | [Link](https://leetcode.com/problems/pascals-triangle) | [Solutions](questions/118.py) |
| 2 | Add Two Numbers | [Link](https://leetcode.com/problems/add-two-numbers) | [Solutions](questions/2.py) |
| 3487 | Maximum Unique Subarray Sum After Deletions | [Link](https://leetcode.com/problems/maximum-unique-subarray-sum-after-deletion) | [Solutions](questions/3487.py) |
| 88 | Merge Sorted Array | [Link](https://leetcode.com/problems/merge-sorted-array) | [Solutions](questions/88.py) |
| 9 | Palindrome Number | [Link](https://leetcode.com/problems/palindrome-number) | [Solutions](questions/9.py) |

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