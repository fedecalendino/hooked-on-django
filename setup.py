from setuptools import setup

setup(
    name="django-hooks",
    packages=[
        "hooks",
        "hooks.apps",
        "hooks.apps.startup",
    ],
    install_requires=[
        "django>1.7",
    ],
)
