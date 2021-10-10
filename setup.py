#!/usr/bin/python3

import setuptools


with open("README.md", "r", encoding="utf-8") as readme_file:
    long_description = readme_file.read()

setuptools.setup(
    name="python-drools-sdk",
    version="0.0.1",
    author="PapiHack",
    author_email="mssmbaye@gmail.com",
    description="A Drools KIE SERVER client library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PapiHack/python-drools-sdk",
    keywords=[
        'python', 'drools', 'kie-server', 
        'python drools sdk', 'python kie-server client', 
        'python drools client'
        ],
    project_urls={
        "Bug Tracker": "https://github.com/PapiHack/python-drools-sdk/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"python_drools_sdk": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
