import sys
import os
import ast

excluded_files = {'run_all_tests.py', 'unittests.py'}
for filename in os.listdir('tests'):
    if filename.endswith('.py') and filename not in excluded_files:
        print('Running', filename)
        with open(os.path.join('tests', filename)) as f:
            code = ast.parse(f.read())
            print(ast.get_docstring(code))
        os.system(f'python -m tests.{filename}')
