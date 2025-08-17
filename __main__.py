import argparse
import ast
import sys

from run_leetcode_solutions.base_solution import BaseSolution
from run_leetcode_solutions.run_solutions import load_solution_class


def parse_args():
    parser = argparse.ArgumentParser(description="Run solution interactively or with test cases.")
    parser.add_argument("--question", type=str, help="Question number (e.g., 1 for 1.py)")
    parser.add_argument("--mode", type=str, choices=["a", "m"], help="Run mode: a (auto) or m (manual)")
    parser.add_argument("--inputs", type=str, help="Manual inputs as Python list string (e.g., \"[1, 2]\")")
    return parser.parse_args()


def run_solutions(questions_folder: str = 'questions'):
    args = parse_args()

    question_number = args.question or input("Enter question number: ").strip()
    mode = args.mode or input("Run in (A)utomatic or (M)anual mode? ").strip().lower()
    inputs_from_cli = None

    if args.inputs:
        try:
            inputs_from_cli = ast.literal_eval(args.inputs)
            if not isinstance(inputs_from_cli, list):
                raise ValueError("Inputs must be a list.")
        except Exception as e:
            print(f"Error parsing inputs: {e}")
            sys.exit(1)

    solution: BaseSolution = load_solution_class(question_number, questions_folder)
    print(f"\nQuestion: {getattr(solution, 'title', 'No question description found.')}\n")

    if mode == "a":
        solution.run_automatic()
    elif mode == "m":
        solution.run_manual(inputs_from_cli)
    else:
        print("Invalid mode. Choose 'a' or 'm'.")

if __name__ == "__main__":
    run_solutions()
