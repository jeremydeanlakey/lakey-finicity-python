import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lakey-finicity",
    version="0.0.1",
    author="Jeremy Dean Lakey",
    author_email="jeremy.lakey@gmail.com",
    description="A client library for Finicity's API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jeremydeanlakey/lakey-finicity-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
