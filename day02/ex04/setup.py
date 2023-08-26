from setuptools import setup, find_packages

setup(
    name='my_minipack',
    version='1.0.0',
    url='None',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    author='fgaribot',
    author_email='fgaribot@student.42.fr',
    description='How to create a package in Python.',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Students',
        'Topic :: Education',
        'Topic :: HowTo',
        'Topic :: Package',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
    ],
)
