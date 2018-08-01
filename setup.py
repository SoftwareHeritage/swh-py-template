#!/usr/bin/env python3

import os

from setuptools import setup, find_packages


def parse_requirements(name=None):
    if name:
        reqf = 'requirements-%s.txt' % name
    else:
        reqf = 'requirements.txt'

    requirements = []
    if not os.path.exists(reqf):
        return requirements

    with open(reqf) as f:
        for line in f.readlines():
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            requirements.append(line)
    return requirements


# Edit this part to match your module
# full sample: https://forge.softwareheritage.org/diffusion/DCORE/browse/master/setup.py
setup(
    name='swh.<module-name>',  # example: swh.loader.pypi
    description='Software Heritage <Module\'s intent>',
    author='Software Heritage developers',
    author_email='swh-devel@inria.fr',
    url='https://forge.softwareheritage.org/diffusion/<module-git-code>',
    packages=find_packages(),  # packages's modules
    scripts=[],   # scripts to package
    install_requires=parse_requirements() + parse_requirements('swh'),
    test_requires=parse_requirements('test'),
    setup_requires=['vcversioner'],
    vcversioner={},
    include_package_data=True,
)
