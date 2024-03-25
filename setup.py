from setuptools import setup, find_packages

setup(
    name='vnengine',
    version='0.1',
    packages=find_packages(),
    test_suite='tests',
    classifiers=[
        'Programming Language :: Python :: 3.12',   
    ],
    entry_points={
        'console_scripts': [
            'vnengine = vnengine.cli:main'
        ]
    },
    install_requires=[
        'googletrans==4.0.0rc1',
        'pygame==2.5.2',
        'setuptools==69.0.3',
        'Sphinx==7.2.6',
        'sphinx-rtd-theme==2.0.0',
        'pyinstaller==6.4.0',

    ],
    author='Lucas Veit',
    description='Library used for development of Visual Novels',
)