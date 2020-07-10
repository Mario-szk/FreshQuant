import setuptools


setuptools.setup(
    name='FreshQuant',
    version='0.0.1',
    author="xupeng",
    author_email=["15601598009@163.com"],
    description="FreshQuant",
    long_description="FreshQuant",
    url="",
    packages=setuptools.find_packages(),
    package_data={'freshquant': [
    ]},
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'kafka == 1.3.5',
        'pandas == 1.0.3',
        'numpy == 1.18.4',
        'protobuf == 3.12.1',
        'pyaml == 20.4.0',
        'PyYAML == 5.3.1',
        'requests == 2.23.0',
        'click == 7.0',
        'sqlalchemy == 1.3.17',
        'arrow == 0.15.6',
        'cx-Oracle == 7.3.0',
        'Jinja2 == 2.11.2',
    ],
    entry_points={'console_scripts': [
        'FreshQuant=freshquant.cmds:cli',
    ]},
)
