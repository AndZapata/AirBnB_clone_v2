#!/usr/bin/python3
'''
generates a .tgz archive from the contents of the web_static folder of your
AirBnB Clone repo, using the function do_pack
'''
from fabric.api import local
from datetime import datetime


def do_pack():
    ''' Function to format an execute in local a fabfile '''
    val = datetime.now().strftime('%Y%m%d%H%M%S')
    local('mkdir -p versions')
    ans = 'versions/web_static_{}.tgz'.format(val)
    try:
        local('tar -czvf {} web_static'.format(ans))
        return ans
    except:
        return None
