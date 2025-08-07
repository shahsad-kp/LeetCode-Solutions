import os
import importlib.util
import inspect
import re

QUESTIONS_DIR = "questions"
README_FILE = "README.md"

def validate_question_file(filepath):
    spec = importlib.util.spec_from_file_location("module", filepath)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    if not hasattr(module, "Solution"):
        return False, "Missing Solution class"

    sol = module.Solution()

    if not hasattr(sol, "__question__"):
        return False, "Missing __question__ attribute"
    if not hasattr(sol, "__leetcode__"):
        return False, "Missing __leetcode__ attribute"
    if not hasattr(sol, "__test_cases__"):
        return False, "Missing __test_cases__ attribute"
    if not isinstance(sol.__test_cases__, list):
        return False, "__test_cases__ must be a list"

    method_count = sum(
        1 for name, _ in inspect.getmembers(sol, predicate=inspect.ismethod)
        if not name.startswith("__")
    )
    if method_count == 0:
        return False, "No solution method found"

    return True, None

def update_readme():
    files = sorted([f for f in os.listdir(QUESTIONS_DIR) if f.endswith(".py")])
    table_lines = []
    for i, f in enumerate(files, 1):
        qnum = f.replace(".py", "")
        spec = importlib.util.spec_from_file_location("module", os.path.join(QUESTIONS_DIR, f))
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        sol = module.Solution()

        title = sol.__question__
        link = sol.__leetcode__
        table_lines.append(f"| {i} | {qnum} | {title} | [Link]({link}) | [Solutions](questions/{f}) |")

    with open(README_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    new_table = "\n".join([
        "| # | LeetCode Number | Title | LeetCode Link | Solutions |",
        "|---|-----------------|-------|---------------|-----------|",
        *table_lines
    ])

    updated = re.sub(
        r"(## 📂 Questions\n\n)([\s\S]*?)(\n\n##|\Z)",
        f"\\1{new_table}\\3",
        content,
    )

    with open(README_FILE, "w", encoding="utf-8") as f:
        f.write(updated)

if __name__ == "__main__":
    all_valid = True
    for file in os.listdir(QUESTIONS_DIR):
        if file.endswith(".py"):
            valid, msg = validate_question_file(os.path.join(QUESTIONS_DIR, file))
            if not valid:
                print(f"❌ {file}: {msg}")
                all_valid = False
    if not all_valid:
        exit(1)

    print("✅ All questions valid.")
    update_readme()
    print("✅ README updated.")
