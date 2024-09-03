from setuptools import setup, find_packages

# Read the contents of your README file
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='penndraw',
    version='0.1.8',
    author='Harry Smith',
    author_email='sharry@seas.upenn.edu',
    description='Drawing library for use at University of Pennsylvania (adapted from Princeton\'s StdDraw)',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/cis110/PennDraw/',
    packages=find_packages(),
    package_data={
        # Adjust the path as needed
        'penndraw': ['*.jpg', '*.jpeg', '*.png'],
    },
    include_package_data=True,
    install_requires=[
        'multipledispatch==1.0.0',
        'mypy==1.9.0',
        'mypy-extensions==1.0.0',
        'pyglet==2.0.14',
        'tomli==2.0.1',
        'typing-extensions==4.10.0',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    python_requires='>=3.10',
)
