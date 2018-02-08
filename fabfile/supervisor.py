# -*- coding: utf-8 -*-
from fabric.api import put, cd, run

from .pypi import pip


def execute(config, virtualenv_path):
    upload_config(config, virtualenv_path)
    if not ensure_package():
        pip('supervisor')
    if ensure_progress():
        shutdown(virtualenv_path)
    start(virtualenv_path)


def upload_config(config, virtualenv_path):
    put('config/{}'.format(config), '{}/supervisord.conf'.format(virtualenv_path))


def ensure_package():
    result = run('which supervisord', warn_only=True)
    if 'no supervisord' in result:
        return False
    else:
        return True


def ensure_progress():
    result = run('ps -ef | grep -v grep | grep supervisord', warn_only=True)
    return bool(result)


def shutdown(virtualenv_path):
    with cd(virtualenv_path):
        run('supervisorctl -c supervisord.conf shutdown')


def start(virtualenv_path):
    with cd(virtualenv_path):
        run('supervisord -c supervisord.conf')
