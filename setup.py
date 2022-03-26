"""
License: CC0-1.0 (Public Domain)
"""

# from setuptools import setup, find_packages
#
with open('README.md') as _f:
    _README_MD = _f.read()

from setuptools import setup

_VERSION = '0.1'

setup(
    name='transform_wsdl',
    version=_VERSION,
    description='Transform WSDL file to make it code generator friendly ',
    long_description=_README_MD,
    classifiers=[
    ],
    url='https://github.com/KalyanChakravarthyV/TransformWSDL',
    download_url='https://github.com/KalyanChakravarthyV/TransformWSDL/tarball/{}'.format(_VERSION),  # TODO.
    author='Kalyan Chakravarthy V',
    author_email='kalyan@vadlakonda.in',
    packages=['transform_wsdl'],
    test_suite="testing",
    setup_requires=["pytest-runner"],
    tests_require=["pytest", "pytest-cov"],
    install_requires=[],
    include_package_data=True,
    license='License: CC0-1.0 (Public Domain)',
    keywords='WSDL ArrayTo',
    entry_points={
        'console_scripts': [
            'transform_wsdl=transform_wsdl:tri'
        ]
    }
)
