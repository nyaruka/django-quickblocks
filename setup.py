from setuptools import setup, find_packages

setup(
    name = 'django-quickblocks',
    version = __import__('django_quickblocks').__version__,
    licence = 'BSD',

    install_requires = [
        'Django==1.3',
        'PIL==1.1.7',
        'django-reversion==1.3.3'
        ],
    dependency_links = [],
    description = "",
    long_description = open('README.rst').read(),
    author = 'Nicolas Pottier, Eugene Rwagasore',
    author_email = 'code@nyaruka.com',
    url = 'http://www.nyaruka.com/#open',
    download_url = 'http://github.com/nyaruka/django-quickblocks',

    include_package_data = True,
    packages = find_packages(),
    zip_safe = False,
    
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
    )
