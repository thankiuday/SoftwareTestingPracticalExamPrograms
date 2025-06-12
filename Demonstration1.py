
'''
code Explanation:

This program calculates the Cyclomatic Complexity of a Python function, which measures the number of independent paths through the code. It uses Python’s ast module to analyze the code structure and counts decision-making points like if, for, while, try, and logical operators. The final complexity is 1 + number of decision points.'''


import ast  


class CyclomaticComplexityCounter(ast.NodeVisitor):
    def __init__(self):
        self.decision_points = 0 

    # Visit 'if' statement
    def visit_If(self, node):
        self.decision_points += 1  
        self.generic_visit(node)   

    # Visit  'for' loop
    def visit_For(self, node):
        self.decision_points += 1  
        self.generic_visit(node)

    # Visit  'while' loop
    def visit_While(self, node):
        self.decision_points += 1
        self.generic_visit(node)

    # Visit  'try-except' block
    def visit_Try(self, node):
        self.decision_points += len(node.handlers)  
        self.generic_visit(node)

    # Visit boolean operations like 'and' / 'or'
    def visit_BoolOp(self, node):
        self.decision_points += len(node.values) - 1  
        self.generic_visit(node)

#calculate the cyclomatic complexity
def calculate_complexity(code):
    tree = ast.parse(code)  
    counter = CyclomaticComplexityCounter()
    counter.visit(tree)  
    return 1 + counter.decision_points  

# Sample Python code to test
code = """
def test(x):
    if x > 0:
        print("Positive")
    else:
        print("Non-positive")
    for i in range(x):
        if i % 2 == 0:
            print("Even")
"""

# Call the function
complexity = calculate_complexity(code)
print(f"Cyclomatic Complexity: {complexity}")
