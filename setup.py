from setuptools import setup, find_packages
import os

# Read the content of README.md if it exists
long_description = ""
if os.path.exists("README.md"):
    with open("README.md", "r") as fh:
        long_description = fh.read()

setup(
    name='module',  # The name of your package
    version='0.1',  # The initial version of the package
    packages=find_packages(),  # Automatically finds and includes all packages
    install_requires=[],  # List of dependencies, if any
    author='Keerthi',  # Your name
    author_email='keerthireddyc7@gmail.com',  # Your email
    description='A LinkedList implementation package for educational purposes',  # Short description
    long_description=long_description,  # Long description (optional)
    long_description_content_type='text/markdown',  # Markdown format for long description
    url='https://github.com/Keerthi11123/module',  # URL for the package (e.g., GitHub)
    classifiers=[  # Optional metadata about the package
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # License type
        'Operating System :: OS Independent',  # Cross-platform compatibility
    ],
)
