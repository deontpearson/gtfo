from setuptools import find_packages, setup

with open("requirements.txt") as fd:
    requirements = [dependency.strip() for dependency in fd]

with open("dev-requirements.txt") as fd:
    dev_requirements = [dependency.strip() for dependency in fd]

with open("README.md") as f:
    README = f.read()

setup(
    name="gtfo",
    version="1",
    author="deontpearson",
    author_email="me@deonpearson.com",
    packages=find_packages(
        where=".", exclude=["*.tests", "*.tests.*", "tests.*", "tests"]
    ),
    package_data={},
    scripts=[],
    description="A tool to scan GTFOBins",
    long_description=README,
    long_description_content_type="text/markdown",
    include_package_data=True,
    install_requires=requirements,
    extras_require={"dev": dev_requirements},
    classifiers=[
        "Intended Audience :: Anyone",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.8",
    ],
    entry_points={
        "console_scripts": [
            "gtfo=cli:run",
        ]
    },
)
