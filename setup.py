from setuptools import setup, find_packages

version = '0.0.1'
long_description = """
Python library and command line utility to automate common PuTTY session
management tasks.
"""
ext_modules = []
install_requires = ['prettytable']
setup_requires = []

setup(
    name='putty_session_manager',
    version=version,
    author='Mikhail Velikikh',
    author_email='mvelikikh@gmail.com',
    url='https://github.com/mvelikikh/putty-session-manager',
    description='Python library for PuTTY session management',
    long_description=long_description,
    keywords='putty',
    license='BSD',
    classifiers=['Development Status :: 4 - Beta',
                 'Topic :: Internet',
                 'Topic :: Software Development',
                 'Topic :: Software Development :: Libraries',
                 'License :: OSI Approved :: BSD License',
                 'Intended Audience :: Developers',
                 'Intended Audience :: System Administrators',
                 'Operating System :: MacOS :: MacOS X',
                 # 'Operating System :: Microsoft :: Windows', -- Not tested yet
                 'Operating System :: POSIX',
                 'Programming Language :: Python :: 3.7',
                 ],
    ext_modules=ext_modules,
    packages=find_packages(),
    install_requires=install_requires,
    setup_requires=setup_requires,
    entry_points = {
        'console_scripts': [
            'psm = \
            putty_session_manager.__main__:cmdline_main'
        ]
    }
)
