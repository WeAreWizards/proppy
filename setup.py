from setuptools import find_packages, setup


name = 'proppy'

setup(
    name=name,
    version='0.1.0',
    url='https://github.com/WeAreWizards/proppy',
    license='MIT',
    description='A proposal generator',
    long_description='A proposal generator',
    author='We Are Wizards',
    author_email='vincent@wearewizards.io',
    packages=find_packages(),
    install_requires=[
        'pytoml==0.1.2',
        'WeasyPrint==0.23',
    ],
    entry_points={
        'console_scripts': [
            'proppy = proppy.main:run_main',
        ],
    },
    package_data={'proppy': ['themes/*.html']},
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ]
)
