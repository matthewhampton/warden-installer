from setuptools import setup
import re

def get_version():
    VERSIONFILE="wardeninstaller/__init__.py"
    initfile_lines = open(VERSIONFILE, "rt").readlines()
    VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
    for line in initfile_lines:
        mo = re.search(VSRE, line, re.M)
        if mo:
            return mo.group(1)
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))

setup(
    name             = 'warden-installer',
    version          = get_version(),
    license          =  'MIT',
    description      = 'Installs warden and its dependencies',
    long_description = \
        """
Installs the various dependencies for warden.  This is required because graphite+carbon+whisper don't play so well with Django i.t.o. install-data directives.
        """,
    author           = 'Matthew Hampton',
    author_email     = 'support@sjsoft.com',
    packages         = ['wardeninstaller'],
    package_data={'wardeninstaller': ['warden_requirements*.txt']},
    #package_dir       ={'' },
    zip_safe = False,
    install_requires = ['pip'],
    keywords         = 'sentry carbon graphite monitoring warden installer',
    url              = 'https://github.com/matthewhampton/warden-installer',
    entry_points     = {
        'console_scripts': [
            'warden_installer = wardeninstaller.Installer:main',
        ]
    },
    classifiers      = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: System :: Monitoring',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)