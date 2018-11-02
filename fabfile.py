from fabric import task
from fabric import Connection
from fabric import SerialGroup as Group

#@task
def install_package(c):
    c.run('sudo apt-get update')

#@task
def install_nginx(c):
    c.run('sudo apt-get install -y nginx')

@task
def run_all(c):
    pool = Group('vagrant@192.168.1.10', 'vagrant@192.168.1.20', connect_kwargs={"password":'vagrant'})
    install_package(pool)
    install_nginx(pool)
