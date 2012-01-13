from setuptools import setup, find_packages

setup(
    name = 'templatefinder',
    version = '0.1',
    description = 'Simple template loader for Django',
    long_description = '\n'.join((
        'Django templatefinder',
        '',
        'Creates a set of available templates',
        '',
    )),
    author = 'Honza Kral',
    author_email='honza.kral@gmail.com',
    license = 'BSD',
    url='https://github.com/WhiskeyMedia/django-templatefinder',

    packages = find_packages(
        where = '.',
    ),

    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Programming Language :: Python :: 2.7",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires = [
        'Django>=1.3',
    ],
    test_suite = 'unittest'
)
