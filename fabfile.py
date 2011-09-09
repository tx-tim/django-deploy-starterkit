"""
The tutorial's fabfile.

This starts out pretty simple -- just automating deployment on a single
server with a few commands. Then it gets a bit more complex (a basic
provisioning example).
"""

import contextlib
from fabric.api import env, run, cd, sudo, put, require, settings, hide, puts
from fabric.contrib import project, files

# This is a bit more complicated than needed because I'm using Vagrant
# for the examples.
env.hosts = ['33.33.33.22']
env.user = 'vagrant'
env.key_filename = '/usr/local/Cellar/ruby/1.9.2-p180/lib/ruby/gems/1.9.1/gems/vagrant-0.8.6/keys/vagrant'


# Constants for where everything lives on the server.
#env.root = "/home/web/myblog"


def setup_machine():
    """
    Set up (bootstrap) a new server.
    
    This essentially does all the tasks in the script done by hand in one
    fell swoop. In the real world this might not be the best way of doing
    this -- consider, for example, what the various creation of directories,
    git repos, etc. will do if those things already exist. However, it's
    a useful example of a more complex Fabric operation.
    """
    # Initial setup and package install.
    sudo("aptitude update")
    sudo("aptitude -y install git-core python-dev python-setuptools "
                              "postgresql-dev postgresql-client build-essential "
                              "libpq-dev subversion mercurial apache2 "
                              "libapache2-mod-wsgi")


def setup_web():
    # Initial setup and package install.
    sudo("mkdir -p /home/website/static")
