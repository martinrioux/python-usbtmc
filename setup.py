from setuptools import setup, find_packages
import os.path

version_py = os.path.join(os.path.dirname(__file__), 'usbtmc', 'version.py')
with open(version_py, 'r') as f:
    d = dict()
    exec(f.read(), d)
    version = d['__version__']

setup(
    name='python-usbtmc',
    description='Python USBTMC driver for controlling instruments over USB',
    version=version,
    long_description='''This Python package supports the USBTMC instrument
control protocol for controlling instruments over USB.''',
    author='Alex Forencich',
    author_email='alex@alexforencich.com',
    url='http://alexforencich.com/wiki/en/python-usbtmc/start',
    download_url='http://github.com/python-ivi/python-usbtmc/tarball/master',
    keywords='USB USBTMC measurement instrument',
    license='MIT License',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Interface Engine/Protocol Translator',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Hardware :: Hardware Drivers',
        'Topic :: System :: Networking',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3'
    ],
    packages=find_packages(),
    install_requires=[
        # Add any dependencies your project might have
    ],
    entry_points={
        # If your package includes any console scripts, you can define them here
    },
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, <4',
)
