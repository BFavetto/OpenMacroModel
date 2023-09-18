import setuptools
import os

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

def strip_comments(l):
    return l.split('#', 1)[0].strip()

def reqs(*f):
    return list(filter(None, [strip_comments(l) for l in open(
        os.path.join(os.getcwd(), *f)).readlines()]))

install_requires = reqs('requirements.txt')

setuptools.setup(
    name="openmacromodel",
    version="0.0.1",
    author="Benjamin Favetto",
    author_email="benjamin.favetto@gmail.com",
    description="Tools to Simulate and Estimate Simple Macroeconomic Model",
    long_description=long_description,
    url="https://https://github.com/BFavetto/OpenMacroModel/",
    download_url = "",
    packages=setuptools.find_packages(),
    license='MIT',
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved",
        "Operating System :: OS Independent",
    ],
    keywords = ["macroeconomics", "economic modeling", "time series"],
    license_files=('LICENSE.md',),
    install_requires=install_requires,
    python_requires='>=3.7'
)