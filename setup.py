#!/usr/bin/env python2
from setuptools import setup, find_packages
from distutils.util import convert_path
from distutils.command.install import INSTALL_SCHEMES
import os, glob, platform

# Get all template files
templates = []
for dirpath, dirnames, filenames in os.walk(convert_path('pwnlib/shellcraft/templates')):
    for f in filenames:
        templates.append(os.path.relpath(os.path.join(dirpath, f), 'pwnlib'))

# Get the version
ns = {}
with open(convert_path('pwnlib/version.py')) as fd:
    exec fd.read() in ns
version = ns['__version__']

# This makes binjitsu-LICENSE.txt appear with the package folders
for scheme in INSTALL_SCHEMES.values():
    scheme['data'] = scheme['purelib']

# Find all of the console scripts
console_scripts = []
for filename in glob.glob('pwnlib/commandline/*'):
    filename = os.path.basename(filename)
    filename, ext = os.path.splitext(filename)

    if ext != '.py' or '__init__' in filename:
        continue

    script = '%s=pwnlib.commandline.%s:main' % (filename, filename)
    console_scripts.append(script)

install_requires     = ['paramiko','argparse', 'mako', 'pyelftools',
                        'capstone==2.1', 'ropgadget', 'pyserial', 'requests']

# This is a hack until somebody ports psutil to OpenBSD
if platform.system() != 'OpenBSD':
    install_requires.append('psutil')

setup(
    name                 = 'binjitsu',
    packages             = find_packages(),
    version              = version,
    data_files           = [('',
                             ['LICENSE-binjitsu.txt',
                             ]),
                            ('/etc/bash_completion.d',
                             ['extra/bash_completion.d/shellcraft',
                             ])
                            ],
    package_data         = {
        'pwnlib': [
            'data/crcsums.txt',
            'data/binutils/*',
            'data/includes/*.h',
            'data/includes/*/*.h',
        ] + templates,
    },
    entry_points = {'console_scripts': console_scripts},
    scripts              = glob.glob("bin/*"),
    description          = "CTF framework and exploit development library.",
    author               = "Zach Riggle",
    author_email         = "zachriggle@gmail.com",
    url                  = 'https://github.com/binjitsu/binjitsu/',
    download_url         = "https://github.com/binjitsu/binjitsu/tarball/%s" % version,
    install_requires     = install_requires,
    license              = "Mostly MIT, some GPL/BSD, see LICENSE-binjitsu.txt and LICENSE-pwntools.txt",
    classifiers          = [
        'Topic :: Security',
        'Environment :: Console',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Intended Audience :: Developers'
    ]
)
