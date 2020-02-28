from setuptools import setup, find_packages

requires = [
    'pyramid',
    'paster_pastedeploy',
    'pyramid-ipython',
    'waitress',
    'sqlalchemy',
    'psycopg2',
    'pyramid_tm',
    'transaction',
    'zope.sqlalchemy'
]

setup(
    name = "pyramid-pg",
    version = '0.0',
    description = 'A TODO App To Learn Pyramid Web Framework',
    author = 'thealphadollar',
    author_email = 'code@thealphadollar.me',
    keywords = 'web pyramid todo',
    packages = find_packages(),
    include_package_data = True,
    install_requires = requires,
    entry_points = {
        'paste.app_factory': [
            'main = todo:main',
        ],
        'console_scripts': [
            'initdb = todo.scripts.initializedb.main'
        ]
    }
)