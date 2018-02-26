# -*- coding: utf-8 -*-
from fabric.api import run


def pip(package_name, version=None):
    command = 'pip install -i http://111.231.238.12:8080/simple --trusted-host 111.231.238.12 '
    if version:
        command += '{package}=={version}'.format(package=package_name, version=version)
    else:
        command += '{package}'.format(package=package_name)

    run(command)
