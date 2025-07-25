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
    # Get non-dunder, non-init methods
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


def main():
    file_number = input("Enter question number: ").strip()
    solution = load_solution_class(file_number)

    print(f"\nQuestion: {getattr(solution, '__question__', 'No question description found.')}\n")

    method_name, method = get_method(solution)
    params = get_arguments(method)
    args = [get_input_for_param(p) for p in params]

    print(f"\nRunning {method_name} with arguments {args}...")
    result = method(*args)
    print(f"Result: {result}")


if __name__ == "__main__":
    main()
