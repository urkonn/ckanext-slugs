from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
    name='ckanext-slugs',
    version=version,
    description="CKAN extension for custom slugs",
    long_description='''
    ''',
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='Julio Acuna',
    author_email='urkonn@gmail.com',
    url='',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.slugs'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points='''
        [ckan.plugins]
        # Add plugins here, e.g.
        org_slugs=ckanext.slugs.plugin:OrganizationSlug
    ''',
)
