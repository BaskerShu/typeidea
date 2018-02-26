from setuptools import find_packages, setup

packages = find_packages('typeidea')
print(packages)
setup(
    name='typeidea',
    version='1.0.3',
    url='https://www.ysz.com/',
    author='Lion',
    author_email='yangshuzhi@outlook.com',
    packages=packages,
    package_dir={
        '': 'typeidea',
    },
    include_package_data=True,
    scripts=['typeidea/manage.py'],
    install_requires=[
        'django==1.11.8',
        'xadmin==0.6.1',
        'django-autocomplete-light==3.2.10',
        'django-ckeditor==5.4.0',
        'django-debug-toolbar==1.9.1',
        'django-rest-framework==0.1.0',
        'django-widget-tweaks==1.4.1',
        'django-simple-captcha==0.5.6',
        'django-markdownx==2.0.22',
        'Markdown==2.6.11',
        'mysqlclient==1.3.12',
        'Pillow==5.0.0',
        'coreapi==2.3.3',
        'gunicorn==19.7.1',
        'django-redis==4.8.0',
        'hiredis==0.2.0',
        'redis==2.10.6',
        'gunicorn==19.7.1',
        'raven==6.5.0',
    ],
)
