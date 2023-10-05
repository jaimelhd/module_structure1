from setuptools import setup, find_packages

# Project metadata
name = "example-project"
version = "0.1.0"
description = "An example Python project"
author = "Your Name"
author_email = "your.email@example.com"
url = "https://github.com/yourusername/example-project"

# Required packages (dependencies)
install_requires = [
    # List your project's dependencies here
]

# Entry points (if your project includes scripts or console entry points)
entry_points = {
    'console_scripts': [
        'my_script = example_project.module:main_function',
    ],
}

# Define the package structure and files to include
packages = find_packages()

# Additional package data (e.g., non-Python files)
package_data = {
    'example_project': ['data/*.txt'],
}

# Main setup configuration
setup(
    name=name,
    version=version,
    description=description,
    author=author,
    author_email=author_email,
    url=url,
    packages=packages,
    package_data=package_data,
    install_requires=install_requires,
    entry_points=entry_points,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)xº