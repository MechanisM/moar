# -*- coding: utf-8 -*-
import os
from setuptools import setup


ROOTDIR = os.path.dirname(__file__)
README = os.path.join(ROOTDIR, 'README.rst')


def run_tests():
    import sys, subprocess
    errno = subprocess.call([sys.executable, 'run_tests.py'])
    raise SystemExit(errno)


setup(
    name='Moar Thumbnails',
    version='0.1',
    author='Juan-Pablo Scaletti',
    author_email='juanpablo@lucumalabs.com',
    packages=['moar'],
    package_data={'moar': [
        '*.*',
        'engines/*.*',
        'stores/*.*',
        'filters/*.*',
        ]},
    zip_safe=False,
    url='http://github.com/lucuma/MoarThumbnails',
    license='MIT license (http://www.opensource.org/licenses/mit-license.php)',
    description='Easy thumbnails for everyone.',
    long_description=open(README).read(),
    install_requires=[],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    test_suite='__main__.run_tests'
)
