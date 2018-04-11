from setuptools import setup, find_packages


with open('requirements.txt') as f:
    requirements = f.read().split('\n')

with open('README.md') as f:
    long_description = f.read()

setup(
    name='admixture_amigo',
    version='1.0.0',
    description='Run Admixture on a PLINK dataset for many values of K',
    author='Juan Manuel Berros',
    author_email='juanma.berros@gmail.com',
    url='https://github.com/biocodices/admixture_amigo',
    license='MIT',
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'admixture_amigo = admixture_amigo.admixture_amigo:main'
        ]
    },
    packages=find_packages(),
    long_description=long_description,
)
