from setuptools import setup

setup(
    name = 'unicode_clock',
    version = '0.1',
    packages = [ 'unicode_clock' ],
    entry_points = {
        'console_scripts' : {
            'unicode_clock=unicode_clock:main'
        }
    }
)
