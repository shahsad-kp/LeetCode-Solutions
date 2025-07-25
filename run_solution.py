import importlib.util
import inspect
import ast
import os


def load_solution_class(file_number):
    file_name = f"{file_number}.py"
    if not os.path.exists(file_name):
        raise FileNotFoundError(f"{file_name} not found.")

    spec = importlib.util.spec_from_file_location("solution_module", file_name)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    if not hasattr(module, "Solution"):
        raise AttributeError(f"{file_name} must define a class named 'Solution'.")

    return module.Solution()


def get_method(solution):
    for name, method in inspect.getmembers(solution, predicate=inspect.ismethod):
        if not name.startswith("__") and name != '__init__':
            return name, method
    raise Exception("No valid method found in Solution class.")


def get_arguments(method):
    sig = inspect.signature(method)
    return [param for param in sig.parameters.values() if param.name != 'self']


def get_input_for_param(param):
    while True:
        try:
            raw = input(f"Enter value for '{param.name}' ({param.annotation}): ")
            value = ast.literal_eval(raw)
            return value
        except Exception as e:
            print(f"Invalid input: {e}. Please try again.")


def run_manual(method, params):
    args = [get_input_for_param(p) for p in params]
    result = method(*args)
    print(f"\nResult: {result}")


def run_automatic(method, test_cases):
    print(f"\nRunning {len(test_cases)} test case(s)...")
    passed = 0
    for idx, case in enumerate(test_cases, 1):
        args = case.get("input", [])
        expected = case.get("output")
        try:
            result = method(*args)
            if result == expected:
                print(f"✅ Test {idx}: Passed")
                passed += 1
            else:
                print(f"❌ Test {idx}: Failed. Input: {args}, Expected: {expected}, Got: {result}")
        except Exception as e:
            print(f"💥 Test {idx}: Exception occurred: {e}")
    print(f"\n{passed}/{len(test_cases)} test cases passed.")


def main():
    file_number = input("Enter question number: ").strip()
    solution = load_solution_class(file_number)

    print(f"\nQuestion: {getattr(solution, '__question__', 'No question description found.')}\n")

    method_name, method = get_method(solution)
    params = get_arguments(method)

    test_cases = getattr(solution, "__test_cases__", [])

    mode = input("Run in (A)utomatic or (M)anual mode? ").strip().lower()

    if mode == "a":
        if not test_cases:
            print("⚠️  No test cases found for automatic mode.")
        else:
            run_automatic(method, test_cases)
    elif mode == "m":
        run_manual(method, params)
    else:
        print("Invalid mode. Choose 'A' or 'M'.")


if __name__ == "__main__":
    main()
