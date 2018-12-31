from setuptools import setup

setup(
    name='snapshotalyzer',
    version='0.1',
    author='Adam Schiestel',
    author_email='adam.schiestel@vistraenergy.com',
    description='Manages EC2 instances',
    license='GPLv3+',
    packages=['shotty'],
    url='https://github.com/aschiestel/snapshotalyzer',
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
    ''',
)