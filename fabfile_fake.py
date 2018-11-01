from fabric import Connection

print('parn')
c = Connection(user='vagrant', host='192.168.1.10',port='22', connect_kwargs={"password":'vagrant'})
c.run('sudo apt-get update')
c.run('sudo apt-get install -y nginx')
c.run('sudo curl -sS https://get.docker.com/ | sh')
