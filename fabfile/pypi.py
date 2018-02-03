# -*- coding: utf-8 -*-
from fabric.api import run


def pip(package_name, version=None):
    command = 'pip install -i http://192.168.65.128:8080/simple --trusted-host 192.168.65.128 '
    if version:
        command += '{package}=={version}'.format(package=package_name, version=version)
    else:
        command += '{package}'.format(package=package_name)

    run(command)
