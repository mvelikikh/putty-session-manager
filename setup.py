from setuptools import setup, find_packages

version = '1.0.dev6'

ext_modules = []
install_requires = ['prettytable']
setup_requires = []

setup(
    name='putty_session_manager',
    version=version,
    author='Mikhail Velikikh',
    author_email='mvelikikh@gmail.com',
    url='https://github.com/mvelikikh/putty-session-manager',
    description='Python command-line utility for PuTTY session management',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    keywords='putty',
    license='GNU General Public License (GPL)',
    classifiers=['Development Status :: 4 - Beta',
                 'Topic :: Internet',
                 'Topic :: Software Development',
                 'Topic :: Software Development :: Libraries',
                 'License :: OSI Approved :: GNU General Public License (GPL)',
                 'Intended Audience :: Developers',
                 'Intended Audience :: System Administrators',
                 'Operating System :: Microsoft :: Windows',
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
