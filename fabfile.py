from fabric import task
from fabric import Connection
from fabric import SerialGroup as Group

#pool = Group('192.168.1.10', '192.168.1.20')
#pool = Group('vagrant@192.168.1.10', 'vagrant@192.168.1.20')

#ca = Connection(user='vagrant', host='192.168.1.10',port='22', connect_kwargs={"password":'vagrant'})

#@task
def install_package(c):
    c.run('sudo apt-get update')


#@task
def install_nginx(c):
    c.run('sudo apt-get install -y nginx')

@task
def run_all(c):
    for host in ('vagrant@192.168.1.10', 'vagrant@192.168.1.20'):
        ca = Connection(host=host, port='22', connect_kwargs={"password":'vagrant'})
        install_package(ca)
        install_nginx(ca)
