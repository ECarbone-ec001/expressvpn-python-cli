from setuptools import setup, find_packages

setup(
    name='expressvpn-python-cli',
    version='1.0.0',
    packages=find_packages(),
    url='https://github.com/ECarbone-ec001/expressvpn-python-cli',
    license='MIT',
    author='Emanuele Carbone',
    author_email='onecsdc@gmail.com',
    description='Fork of the expressvpn-python library by Philippe Remy, with CLI support',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
    ],
    python_requires='>=3.13',
)

