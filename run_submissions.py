import glob
import os
import ast
from sympy import isprime  # Import isprime here


def run_gcd_test(gcd_func, a, b, expected):
    """
    Runs a test case for the gcd function.
    """
    result = gcd_func(a, b)
    if result == expected:
        print(f"PASS: gcd({a}, {b}) = {result}")
    else:
        print(f"FAIL: gcd({a}, {b}) = {result}, expected {expected}")


def load_and_run():
    """
    Detect and run all student submissions from the students_submissions directory.
    Each student's submission is expected to be in a file named gcd_<GitHubUsername>.py.
    """
    # Find all the files in the students_submissions directory matching the pattern gcd_*.py
    student_files = glob.glob("students_submissions/gcd_*.py")

    for file in student_files:

        if file in [
            "students_submissions/gcd_dt393.py",  # NameError: name 'math' is not defined. Did you forget to import 'math'?
            "students_submissions/gcd_zlk.py",  # ZeroDivisionError: integer modulo by zero
        ]:
            continue

        # Extract the student's GitHub username or identifier from the filename
        module_name = os.path.splitext(os.path.basename(file))[0]

        # Read the student's code
        with open(file, "r") as f:
            student_code = f.read()

        # Parse the student's code to extract all function definitions
        parsed_code = ast.parse(student_code)
        functions = {}
        for node in parsed_code.body:
            if isinstance(node, ast.FunctionDef):
                func_code = compile(
                    ast.Module(body=[node], type_ignores=[]),
                    filename="<ast>",
                    mode="exec",
                )
                func_namespace = {}
                exec(func_code, func_namespace)
                functions[node.name] = func_namespace[node.name]

        # Check if the gcd function was found and run the test cases
        if "gcd" in functions:
            gcd_func = functions["gcd"]
            # Ensure all necessary functions are available in the namespace
            gcd_func.__globals__.update(functions)
            gcd_func.__globals__["isprime"] = (
                isprime  # Add isprime to the global namespace
            )
            print(f"Running {module_name}'s submission...")
            # run_gcd_test(gcd_func, 54, 24, 6)
            # run_gcd_test(gcd_func, 48, 18, 6)
            # run_gcd_test(gcd_func, 101, 10, 1)
            # run_gcd_test(gcd_func, 270, 192, 6)
            # Edge case test cases
            run_gcd_test(gcd_func, 0, 0, None)  # Both numbers are zero
            run_gcd_test(gcd_func, -54, 24, 6)  # One negative number
            run_gcd_test(gcd_func, 54, -24, 6)  # One negative number
            run_gcd_test(gcd_func, -54, -24, 6)  # Both numbers are negative
            run_gcd_test(gcd_func, 0, 24, 24)  # One number is zero
            run_gcd_test(gcd_func, 24, 0, 24)  # One number is zero
            run_gcd_test(gcd_func, 17, 13, 1)  # Both numbers are prime
            run_gcd_test(gcd_func, 1000000000, 2, 2)  # Large number and small number
            run_gcd_test(gcd_func, 123456789, 987654321, 9)  # Large numbers
            run_gcd_test(gcd_func, 1, 1, 1)  # Both numbers are one
            print()
        else:
            print(f"ERROR: {module_name}'s submission does not have a gcd function\n")


# This is the entry point of the script
if __name__ == "__main__":
    load_and_run()
