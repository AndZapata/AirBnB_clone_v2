#!/usr/bin/python3
'''
generates a .tgz archive from the contents of the web_static folder of your
AirBnB Clone repo, using the function do_pack
'''
from fabric.api import local, put, run, env
from datetime import datetime
from os.path import exists

env.hosts = ['35.227.76.167', '35.237.211.62']


def do_pack():
    ''' Function to format an execute in local a fabfile '''
    val = datetime.now().strftime('%Y%m%d%H%M%S')
    local('mkdir -p versions')
    ans = 'versions/web_static_{}.tgz'.format(val)
    try:
        local('tar -czvf {} web_static'.format(ans))
        return ans
    except BaseException:
        return None


def do_deploy(archive_path):
    ''' Fabric script that distributes an archive to web servers '''
    if not exists(archive_path):
        return False
    try:
        put(archive_path, '/tmp/')
        name = archive_path.split('/')[-1]
        extention = name.split('.')[0]
        releases = '/data/web_static/releases/'
        current = '/data/web_static/current'
        run('mkdir -p {}{}/'.format(releases, extention))
        run('tar -xzf /tmp/{} -C {}{}/'.format(name, releases, extention))
        run('rm /tmp/{}'.format(name))
        run('mv {1}{0}/web_static/* {1}{0}/'.format(extention, releases))
        run('rm -rf {}{}/web_static'.format(releases, extention))
        run('rm -rf {}'.format(current))
        run('ln -s {}{}/ {}'.format(releases, extention, current))
        return True
    except:
        return False

def deploy():
    '''
    Fabric script that creates and distributes an archive to web servers
    '''
    test = do_pack()
    if test:
        new_path = do_deploy(test)
        return new_path
    else:
        return False
