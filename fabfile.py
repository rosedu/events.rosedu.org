from fabric.api import local


def devel():
    local('jekyll --auto --serve')


def build():
    local('jekyll')


def deploy():
    build()
    local('rsync -rtv _site/ events@rosedu.org:public_html/')
