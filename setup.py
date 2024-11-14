from setuptools import find_packages, setup

setup(
    name="subprocess_execution",
    version="0.1.0",
    author="josh waddington",
    author_email="josh.waddington1@gmail.com",
    description="Efficient library for running Python code in isolated subprocesses.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/joshwadd/subprocess_execution/",
    packages=find_packages(),
    install_requires=[
        # List your library's dependencies here
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        # Add additional classifiers as appropriate
    ],
    python_requires=">=3.6",
)
