import setuptools
import os


class CleanCommand(setuptools.Command):
    """Custom clean command to tidy up the project root."""
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        os.system('rm -vrf ./dist/*.egg-info ./*.egg-info')


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pokemonlib",
    version="0.0.4",
    author="arthuro555",
    author_email="papinrouge@gmail.com",
    description="An implementation of pokemon algorithms",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/arthuro555/pokemonlib",
    packages=setuptools.find_packages(),
    install_requires=['cryptography', 'pyglet', 'requests'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        "Programming Language :: Python :: 3",
        'Topic :: Software Development',
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    project_urls={
        'Say Thanks!': 'https://saythanks.io/to/arthuro555',
        'Source': 'https://github.com/arthuro555/pokemonlib',
    },
    cmdclass={
        'clean': CleanCommand,
    }
)
