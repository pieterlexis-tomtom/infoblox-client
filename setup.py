#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

with open('requirements.txt') as requirements_file:
    requirements = requirements_file.read().splitlines()

with open('testing_requirements.txt') as requirements_file:
    testing_requirements = requirements_file.read().splitlines()


setup(
    name='infoblox-client',
    version='0.6.1',
    description="Client for interacting with Infoblox NIOS over WAPI",
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/markdown',
    author="John Belamaric",
    author_email='jbelamaric@infoblox.com',
    url='https://github.com/infobloxopen/infoblox-client',
    packages=[
        'infoblox_client',
    ],
    package_dir={'infoblox-client':
                 'infoblox_client'},
    include_package_data=True,
    install_requires=requirements,
    license="Apache",
    zip_safe=False,
    keywords='infoblox-client',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    test_suite='tests',
    tests_require=testing_requirements
)
