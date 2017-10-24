from setuptools import setup

setup(
    name='makeitgreen',    # This is the name of your PyPI-package.
    version='1.0',                          # Update the version number for new releases
    scripts=['mig'],                  # The name of your scipt, and also the command you'll be using for calling it
    description='Makes your Git Green every time you run this package'
)
