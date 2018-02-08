# -*- coding: utf-8 -*-
import os

from fabric.api import env, run, roles, cd, sudo, local
from fabric.contrib.files import exists
from fabric.context_managers import prefix

from fabfile import supervisor
from fabfile.pypi import pip

# env.shell = '/bin/bash -l -i -c '

env.roledefs = {
    'developserver': [
        'baskershu@65.49.132.45:26266',
    ],
}


WORKSAPCE_PATH = '/home/baskershu/myblog'


def get_env_path(virtualenv_name):
    path = os.path.join(WORKSAPCE_PATH, virtualenv_name)
    return path


def get_activate_path(virtualenv_path):
    path = os.path.join(virtualenv_path, 'bin/activate')
    return path


def upload_typeidea():
    local('python setup.py sdist bdist_wheel upload -r pypi')


@roles('developserver')
def deploy_typeidea(version):
    deploy('typeidea', version, 'supervisord_typeidea.conf')


@roles('developserver')
def deploy_sentry(version=None):
    deploy('sentry', version, 'supervisord_sentry.conf')
    sudo('/etc/init.d/nginx reload')  # 重启nginx


def deploy(package, version, config):
    '''
        1. 检验虚拟环境如果没有则创建一个虚拟环境
        2. 安装程序包
        3. 上传supervisord配置
        4. 确实是否安装supervisor
        5. 运行supervisord，启动程序
    '''
    virtualenv_name = '{}-env'.format(package)
    virtualenv_path = get_env_path(virtualenv_name)
    active_file_path = get_activate_path(virtualenv_path)

    ensure_virtualenv(virtualenv_name, active_file_path)

    with prefix('source {}'.format(active_file_path)):
        pip(package, version)
        collectstatic(virtualenv_name, virtualenv_path)
        supervisor.execute(config, virtualenv_path)


def ensure_virtualenv(virtualenv_name, active_file_path):
    if not exists(active_file_path):
        with cd(WORKSAPCE_PATH):
            run('virtualenv %s' % virtualenv_name)


def install_package(package_name, active_file_path, version):
    with prefix('source {}'.format(active_file_path)):
        pip('typeidea', version)


def collectstatic(virtualenv_name, virtualenv_path):
    if not ('sentry' in virtualenv_name):
        with cd(virtualenv_path):
            run('./bin/manage.py collectstatic')
