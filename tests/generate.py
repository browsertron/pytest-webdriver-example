import os
import os.path as path
import sys
import shutil

input_path = path.dirname(path.realpath(__file__))
output_path = path.normpath(path.join(input_path, 'webdriver'))

# Load the template
with open(path.join(input_path, 'webdriver.template.py')) as f:
    template = f.read()

# Delete all existing tests
if os.path.exists(output_path):
    shutil.rmtree(output_path)
os.mkdir(output_path)

# Use the last arg for desired count
desired = int(sys.argv[-1])

# Write all the new tests
for num in range(desired):
    test_path = path.join(output_path, 'test_{}.py'.format(num))
    test_contents = template.replace('{{num}}', str(num))
    with open(test_path, 'w') as f:
        f.write(test_contents)

shutil.copy2(path.join(input_path, 'webdriver_monkey_patch.py'), output_path)
shutil.copy2(path.join(input_path, 'conftest.py'), output_path)
