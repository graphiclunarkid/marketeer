from distutils.core import setup, Command

classifiers = []
classifiers.append('Development Status :: 2 - Pre-Alpha')
classifiers.append('Environment :: Console')
classifiers.append('Intended Audience :: Developers')
classifiers.append('Intended Audience :: End Users/Desktop')
classifiers.append('Intended Audience :: Financial and Insurance Industry')
classifiers.append('Intended Audience :: Science/Research')
classifiers.append('License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)')
classifiers.append('Operating System :: OS Independent')
classifiers.append('Programming Language :: Python')
classifiers.append('Programming Language :: Python :: 3')
classifiers.append('Topic :: Office/Business :: Financial')
classifiers.append('Topic :: Office/Business :: Financial :: Investment')
classifiers.append('Topic :: Scientific/Engineering :: Information Analysis')

class PyTest(Command):
    user_options = []
    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import sys,subprocess
        errno = subprocess.call([sys.executable, 'runtests.py'])
        raise SystemExit(errno)

setup(
    name = 'marketeer',
    version = '0.1.2',
    author = 'Richard King',
    author_email = 'mail@richardskingdom.net',
    url = 'https://github.com/graphiclunarkid/marketeer',
    packages = ['marketeer'],
    description = 'Trading bot',
    long_description = '',
    classifiers = classifiers,
    cmdclass = {'test': PyTest},
    )
