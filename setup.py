from setuptools import setup

version = (
    open('sqlglot/__init__.py')
    .read()
    .split('__version__ = ')[-1]
    .split("\n")[0]
    .strip()
    .replace("'", '')
)

setup(
    name='sqlglot',
    version=version,
    description='An easily customizable SQL parser and transpiler',
    url='https://github.com/tobymao/sqlglot',
    author='Toby Mao',
    author_email='toby.mao@gmail.com',
    license='MIT',
    packages=['sqlglot'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: SQL',
        'Programming Language :: Python :: 3 :: Only',
    ],
)
