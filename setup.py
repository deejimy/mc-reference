from setuptools import setup, find_packages

setup(
    name='mkdocs-accent-normalizer',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'mkdocs>=1.5.0',
    ],
    entry_points={
        'mkdocs.plugins': [
            'accent_normalizer = docs_plugins.accent_normalizer:AccentNormalizerPlugin',
        ],
    },
)