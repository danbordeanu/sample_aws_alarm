from setuptools import find_packages, setup
from setuptools.dist import Distribution
from os import path
from distutils.command.register import register as register_orig
from distutils.command.upload import upload as upload_orig
from setuptools import setup

class BinaryDistribution(Distribution):
    def is_pure(self):
        return False

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


class register(register_orig):
    def _get_rc_file(self):
        return path.join('.', '.pypirc')

class upload(upload_orig):
    def _get_rc_file(self):
        return path.join('.', '.pypirc')

setup(
    name='host_host_awsalarhostk',
    version='0.1dev',
    author='Dan Bordeanu',
    author_email='dan.bordeanu@host.com',
    url='https://stash.host.com/projects/SRE/repos/aws_alarm/browse',
    platforms=['any'],
    license='host',
    description=('SDK for creating AWS CloudWatch alerts'),
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    include_package_data=True,
    classifiers=['Development status :: 0 - Beta',
                 'Topic :: Utilities',
                 'License :: host Approved :: host License'],
    install_requires=[
        'boto3',
        'botocore'
      ],
    python_requires='>=3.6',
    zip_safe=False,
    cmdclass={
        'register': register,
        'upload': upload,
    }
)
