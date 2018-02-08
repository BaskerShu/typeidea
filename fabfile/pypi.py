# -*- coding: utf-8 -*-
from fabric.api import run


def pip(package_name, version=None):
    command = 'pip install -i http://65.49.132.45:8080/simple --trusted-host 65.49.132.45 '
    if version:
        command += '{package}=={version}'.format(package=package_name, version=version)
    else:
        command += '{package}'.format(package=package_name)

    run(command)
