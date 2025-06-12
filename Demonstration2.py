import ast
import re

# Step 1: Checking function documentation and naming convention
def check_functions(source_code):
    issues = []
    tree = ast.parse(source_code)

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            func_name = node.name

            # Check for docstring
            docstring = ast.get_docstring(node)
            if not docstring:
                issues.append(f"Function '{func_name}' is missing a docstring.")

            # Check for snake_case naming
            if not re.match(r'^[a-z_][a-z0-9_]*$', func_name):
                issues.append(f"Function name '{func_name}' does not follow snake_case convention.")

    return issues

# Step 2: Check indentation levels (should be 4 spaces)
def check_indentation(lines):
    issues = []
    for i, line in enumerate(lines, start=1):
        if line.strip() == "":
            continue  # skip empty lines

        leading_spaces = len(line) - len(line.lstrip(' '))
        if leading_spaces % 4 != 0 and line.startswith(' '):
            issues.append(f"Line {i}: Indentation is not a multiple of 4 spaces.")
    return issues

# Step 3: Run the SQA checklist
def run_sqa_checklist(file_path):
    try:
        with open(file_path, 'r') as f:
            code = f.read()
            lines = code.split('\n')

            print(f"Checking '{file_path}' for SQA compliance...\n")
            func_issues = check_functions(code)
            indent_issues = check_indentation(lines)

            all_issues = func_issues + indent_issues

            if not all_issues:
                print(" Code passed all SQA checks!")
            else:
                print("Issues found:")
                for issue in all_issues:
                    print("-", issue)

    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"Error during analysis: {e}")

# Step 4: Main execution
if __name__ == "__main__":
    filename = input("Enter the Python file path to check (e.g., sample.py): ").strip()
    run_sqa_checklist(filename)
