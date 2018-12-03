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
    version="v0.0.1a",
    description="Agnostic project analyzer that generates resourceful diagrams. WIP",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    keywords="productivity, software-analysis, analysis-of-information-systems, root-cause-analysis, software-analysis-and-modeling structural-analysis, wip, wip-do-not-use, software-composition-analysis"
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
    ]
)