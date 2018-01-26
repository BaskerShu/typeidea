from setuptools import find_packages, setup

packages = find_packages('typeidea')
print(packages)
setup(
    name='typeidea',
    version='0.1',
    url='https://www.ysz.com/',
    author='Lion',
    author_email='yangshuzhi@outlook.com',
    packages=packages,
    package_dir={
        '': 'typeidea',
    },
    include_package_data=True,
    scripts=['typeidea/manage.py'],
    install_requires=['django==1.11.7'],
)
