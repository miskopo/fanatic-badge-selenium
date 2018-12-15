from setuptools import setup

setup(
    name='fanatic_badge_selenium',
    version='0.0.1',
    packages=['fanatic_badge_selenium'],
    entry_points={
        'console_scripts': [
            'fanatic_badge_selenium = fanatic_badge_selenium.__main__:main'
         ]
    })
