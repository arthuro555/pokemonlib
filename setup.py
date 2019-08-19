import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pokemonlib",
    version="0.0.1",
    author="arthuro555",
    author_email="papinrouge@gmail.com",
    description="An implementation of pokemon algorithms",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/arthuro555",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)