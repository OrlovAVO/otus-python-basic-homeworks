from setuptools import setup, find_packages

setup(
    name='BasePython-homeworks-new',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        alembic == 1.8.0
        asn1crypto == 1.5.1
        click == 8.1.3
        Flask == 2.1.2
        Flask - Migrate == 3.1.0
        Flask - SQLAlchemy == 2.5.1
        Flask - WTF == 1.0.1
        greenlet == 1.1.2
        gunicorn == 20.1.0
        h11 == 0.13.0
        importlib - metadata == 4.12.0
        itsdangerous == 2.1.2
        Jinja2 == 3.1.2
        Mako == 1.2.1
        MarkupSafe == 2.1.1
        pg8000 == 1.29.1
        scramp == 1.4.1
        SQLAlchemy == 1.4.39
        Werkzeug == 2.1.2
        WTForms == 3.0.1
        zipp == 3.8.0

    ],
    python_requires='==3.9.*',
)