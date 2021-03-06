from distutils.core import setup
setup(
    name = "django-exportable-admin",
    version = "1.1",

    packages = ['django_exportable_admin'],

    author = "Jay Wineinger",
    author_email = "jay.wineinger@gmail.com",

    description = "An app to allow Django admin changelists to be exported to CSV",
    long_description=open('README.rst').read(),
    data_files = [('README.rst',)],

    url = "https://github.com/jwineinger/django-exportable-admin",
    download_url = "https://github.com/jwineinger/django-exportable-admin/downloads",

    requires = [
        "Django (>=1.4.0a0)"
    ],

    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
)
