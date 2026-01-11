from setuptools import setup, find_packages

setup(
    name="excel2json-converter",
    version="1.0.0",
    description="Convert Excel files to JSON using Python",
    author="Your Name",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "openpyxl"
    ],
    entry_points={
        "console_scripts": [
            "excel2json=main:main"
        ]
    },
)
