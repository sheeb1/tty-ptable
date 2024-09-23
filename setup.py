from setuptools import setup, find_packages

setup(
    name='tty-ptable',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'click',  # Specify any dependencies here
    ],
    entry_points={
        'console_scripts': [
            'tty-ptable=tty_ptable.tty_ptable:main',  # Adjust this based on your main function location
        ],
    },
    author='sheeb1',
    author_email='sheeb1@proton.me',
    description='A Periodic table for the Linux terminal',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/sheeb1/tty-ptable',
)
