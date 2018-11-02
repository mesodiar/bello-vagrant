from fabric import task
from fabric import Connection
from fabric import SerialGroup as Group

pool = Group('vagrant@192.168.1.10', 'vagrant@192.168.1.20', connect_kwargs={"password":'vagrant'})

pool.run('sudo apt-get update')
pool.run('sudo apt-get install -y nginx')

