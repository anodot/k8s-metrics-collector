from setuptools import setup, find_packages

app_version = '0.1.0'

setup(
    name='agent',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    version=app_version,
)
