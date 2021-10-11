#!/usr/bin/python3

import setuptools


with open("README.md", "r", encoding="utf-8") as readme_file:
    long_description = readme_file.read()

setuptools.setup(
    name="python-drools-sdk",
    version="0.0.3",
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
    install_requires=[
        "certifi==2021.10.8",
        "charset-normalizer==2.0.6",
        "idna==3.2",
        "jsons==1.5.1",
        "requests==2.26.0",
        "typish==1.9.3",
        "urllib3==1.26.7",
    ],
    package_dir={"python_drools_sdk": "src"},
    packages=[
        'python_drools_sdk',
        'python_drools_sdk.commands',
        'python_drools_sdk.exceptions',
        'python_drools_sdk.utils',
        'python_drools_sdk.kie',
    ],
    python_requires=">=3.6",
)
