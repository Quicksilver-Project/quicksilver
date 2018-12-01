# Copyright (C) 2018 Logan Campos - @binaryflesh
from setuptools import setup
from pathlib import Path

runPath = Path(__file__).parent

def get_long_description() -> str:
    readme_md = runPath / "README.md"
    with open(readme_md, encoding="utf-8") as ld:
        return ld.read()

setup(
    name="quicksilver",
    version="Planning",
    description="Agnostic Code Analyzer that generates useful UML-like diagrams",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    keywords="uml automation",
    author="Logan Campos",
    author_email="logan.campos123@gmail.com",
    url="https://github.com/binaryflesh/quicksilver",
    license="MIT",
    python_requires=">=3.6",
    install_requires=[],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Code Generators",
    ]
)