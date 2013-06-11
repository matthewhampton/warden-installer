import argparse
import subprocess
import os
import sys
import distutils.sysconfig
import pkg_resources

def _run(command):
    subprocess.check_call(command)

def is_installed(package_name):
    try:
        pkg_resources.get_distribution(package_name)
        return True
    except pkg_resources.DistributionNotFound:
        return False

def install_libraries(home, run=None, pip=None, lib=None, scripts=None, prefix=None):
    run = run or _run
    pip = pip or 'pip'
    if lib is None:
        lib= distutils.sysconfig.get_python_lib()
    if scripts is None:
        scripts=os.path.dirname(sys.executable)
    if prefix is None:
        prefix=os.path.dirname(scripts)

    if 'win' in sys.platform:
        pipping_easy_install = 'pipping_easy_install'

        if not is_installed('pipping-easy-install'):
            run([pip, 'install', 'http://github.com/matthewhampton/pipping-easy-install/tarball/master'])

        run([pipping_easy_install, 'Twisted==11.1.0'])
        run([pipping_easy_install, 'psutil'])
        run([pipping_easy_install, 'pycairo'])
        run([pipping_easy_install, 'pywin32'])
        run([pipping_easy_install, 'zope.interface'])
    else:
        if not is_installed('pycairo'):
            run([pip, 'install', "http://cairographics.org/releases/py2cairo-1.8.10.tar.gz" ])
        run([pip, 'install', "python-daemon"])
        run([pip, 'install', "lockfile"])


    run([pip, 'install', 'http://github.com/richg/whisper/tarball/0.9.x-warden#egg=whisper-0.9.10-warden',
         '--install-option=--install-scripts=%s' % scripts,
         '--install-option=--prefix=%s' % prefix,
         '--install-option=--install-lib=%s' % lib,
         '--install-option=--install-data=%s' % (os.path.join(home, 'graphite'))])
    run([pip, 'install', 'http://github.com/richg/carbon/tarball/0.9.x-warden#egg=carbon-0.9.x-warden',
         '--install-option=--install-scripts=%s' % scripts,
         '--install-option=--prefix=%s' % prefix,
         '--install-option=--install-lib=%s' % lib,
         '--install-option=--install-data=%s' % (os.path.join(home, 'graphite'))])
    run([pip, 'install', "http://github.com/richg/Diamond/tarball/master",
         '--install-option=--install-scripts=%s' % scripts,
         '--install-option=--install-lib=%s' % lib,
         '--install-option=--install-data=%s' % (os.path.join(home, 'diamond'))])
    run([pip, 'install', "Django==1.4.3"])
    run([pip, 'install', "http://github.com/richg/graphite-web/tarball/0.9.x-warden#egg=graphite-web-0.9.x-warden",
         '--install-option=--install-scripts=%s' % scripts,
         '--install-option=--prefix=%s' % prefix,
         '--install-option=--install-lib=%s' % lib,
         '--install-option=--install-data=%s' % (os.path.join(home, 'graphite'))])

    run([pip, 'install', "CherryPy==3.2.2" ])

    run([pip, 'install', "sentry==5.2.2"])
    run([pip, 'install', "http://github.com/richg/warden/tarball/master",
         '--install-option=--install-data=%s' % home])


def main():
    parser = argparse.ArgumentParser(description='Warden installer')
    parser.add_argument('home', nargs=1, help="Install the data in to this folder.")
    args = parser.parse_args()
    install_libraries(args.home[0])

if __name__ == '__main__':
    main()