#!/usr/bin/env python

from setuptools import setup

with open("README.rst") as readme_f:
    README = readme_f.read()

with open("requirements.txt") as requirements_f:
    REQUIREMENTS = requirements_f.readlines()


setup(
    name="habitual",
    version="0.1.1",
    description="Send notifications for things on a fixed, repeated schedule",
    long_description=README,
    url="https://github.com/cdown/habitual",
    license="Public Domain",
    author="Chris Down",
    author_email="chris@chrisdown.name",
    py_modules=["habitual"],
    entry_points={"console_scripts": ["habitual=habitual:main"]},
    keywords="cron habit tracking schedule",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: Public Domain",
        "Programming Language :: Python :: 3",
        "Topic :: Utilities",
    ],
    install_requires=REQUIREMENTS,
)
