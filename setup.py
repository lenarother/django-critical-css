import os
from codecs import open

from setuptools import setup, find_packages


BASE_DIR = os.path.abspath(os.path.dirname(__file__))
VERSION = __import__('critical').__version__


with open(os.path.join(BASE_DIR, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='django-critical-css',
    version=VERSION,
    description='django-critical-css aims to speed up webpage rendering by saving critical css in db.',
    long_description=long_description,
    url='https://github.com/lenarother/django-critical-css',
    project_urls={
        'Bug Reports': 'https://github.com/lenarother/django-critical-css/issues',
        'Source': 'https://github.com/lenarother/django-critical-css',
    },
    author='Magdalena Rother',
    author_email='rother.magdalena@gmail.com',
    packages=find_packages(exclude=['tests', 'tests.*']),
    install_requires=['django_rq', 'django-inline_static'],
    include_package_data=True,
    keywords='django',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
)
