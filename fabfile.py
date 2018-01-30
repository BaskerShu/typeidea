# -*- coding: utf-8 -*-
import os

from fabric.api import env, run, roles, cd, put
from fabric.contrib.files import exists
from fabric.context_managers import prefix

# env.shell = '/bin/bash -l -i -c '

env.roledefs = {
    'developserver': [
        'baskershu@192.168.65.128',
    ],
}


WORKSAPCE_PATH = '/home/baskershu/workspace'
VIRTUALENV_PATH = os.path.join(WORKSAPCE_PATH, 'typeidea-env')
ACTIVE_FILE_PATH = os.path.join(VIRTUALENV_PATH, 'bin/activate')


@roles('developserver')
def run_typeidea(version):
    '''
        1. 检验虚拟环境如果没有则创建一个虚拟环境
        2. 运行虚拟环境
        3. 安装程序包
        4. 进入到虚拟环境中的bin目录中运行虚拟环境
    '''

    ensure_virtualenv('typeidea-env')

    install_typeidea(version)

    upload_supervisord_config()

    ensure_supervisord()

    run_supervisord()


def pip(package_name, version=None):
    command = 'pip install -i http://192.168.65.128:8080/simple --trusted-host 192.168.65.128 '
    if version:
        command += '{package}=={version}'.format(package=package_name, version=version)
    else:
        command += '{package}'.format(package=package_name)

    run(command)


def ensure_virtualenv(virtualenv_name):
    if not exists(ACTIVE_FILE_PATH):
        with cd(WORKSAPCE_PATH):
            run('virtualenv %s' % virtualenv_name)


def install_typeidea(version):
    with prefix('source {}'.format(ACTIVE_FILE_PATH)):
        pip('typeidea', version)


def upload_supervisord_config():
    put('config/supervisord.conf', '{}/supervisord.conf'.format(VIRTUALENV_PATH))


def ensure_supervisord():
    with prefix('source {}'.format(ACTIVE_FILE_PATH)):
        result = run('which supervisord', warn_only=True)
        if not result:
            pip('supervisor')


def run_supervisord():
    with prefix('source {}'.format(ACTIVE_FILE_PATH)):
        result = run('ps -ef | grep -v grep | grep supervisord', warn_only=True)
        if result:
            supervisord_shutdown()

        supervisord_start()


def supervisord_shutdown():
    with cd(VIRTUALENV_PATH):
        run('supervisorctl -c supervisord.conf shutdown')


def supervisord_start():
    with prefix('source {}'.format(ACTIVE_FILE_PATH)):
        with cd(VIRTUALENV_PATH):
            run('supervisord -c supervisord.conf')
