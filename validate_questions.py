import os
import importlib.util
import inspect
import re

from run_leetcode_solutions.base_solution import BaseSolution

QUESTIONS_DIR = "questions"
README_FILE = "README.md"

def validate_question_file(filepath):
    spec = importlib.util.spec_from_file_location("module", filepath)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    if not hasattr(module, "Solution"):
        return False, "Missing Solution class"

    sol: BaseSolution = module.Solution()
    return sol.run_automatic()

    return True, None

def update_readme():
    files = sorted([f for f in os.listdir(QUESTIONS_DIR) if f.endswith(".py")])
    table_lines = []
    for i, f in enumerate(files, 1):
        qnum = f.replace(".py", "")
        spec = importlib.util.spec_from_file_location("module", os.path.join(QUESTIONS_DIR, f))
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        sol: BaseSolution = module.Solution()

        title = sol.title
        link = sol.leetcode_link
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
