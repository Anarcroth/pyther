from distutils.core import setup

setup(
    # Application name:
    name="Pyther"

    # Version number (initial):
    version="0.1.0",

    # Application author details:
    author="Martin Nestorov",

    # Packages
    packages=["app"],

    # Include additional files into the package
    include_package_data=True,

    # long_description=open("README.md").read(),

    # Dependent packages (distributions)
    install_requires=[
        "curses",
    ],
)
