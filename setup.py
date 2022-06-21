from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in z1nctl/__init__.py
from z1nctl import __version__ as version

setup(
	name="z1nctl",
	version=version,
	description="Z1N Command Line Tools for all things ERPNext",
	author="ZirrusOne",
	author_email="adoing@zirrusone.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
