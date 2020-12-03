from os import path

from setuptools import setup

this_directory = path.abspath(path.dirname(__file__))

with open(path.join(this_directory, "readme.md"), encoding="utf-8") as f:
    long_description = f.read()


setup(
    name="hooked-on-django",
    version="0.1.0",
    url="https://github.com/fedecalendino/hooked-on-django",
    description="Simple django application to trigger hooked methods.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Fede Calendino",
    author_email="fede@calendino.com",
    license="MIT",
    packages=[
        "hooks",
        "hooks.apps",
        "hooks.apps.startup",
    ],
    install_requires=[
        "django>1.7",
    ],
    keyword=[
        "django",
        "hooks",
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Framework :: Django :: 3.1',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Internet :: WWW/HTTP',
    ],
    project_urls={
        'Source': 'https://github.com/fedecalendino/hooked-on-django',
    },
)
