import setuptools

import info

import os
from distutils.command.register import register as register_orig
from distutils.command.upload import upload as upload_orig

from setuptools import setup


class register(register_orig):

    def _get_rc_file(self):
        return os.path.join('.secrets/', '.pypirc')

class upload(upload_orig):

    def _get_rc_file(self):
        return os.path.join('.secrets/', '.pypirc')


def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]


with open("README.md", "r") as fh:
    long_description = fh.read()


install_reqs = parse_requirements('./requirements/package')


setuptools.setup(
    name=info.name,
    version=info.version,
    author=info.author,
    author_email=info.email,
    description=info.description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f'https://github.com/Hedgehogues/{info.name}',
    packages=setuptools.find_packages(exclude=['tests', 'service']),
    classifiers=[
        f"Programming Language :: Python :: {info.python_version}",
        "Operating System :: OS Independent",
    ],
    cmdclass={
        'register': register,
        'upload': upload,
    },
    install_requires=install_reqs,
)
