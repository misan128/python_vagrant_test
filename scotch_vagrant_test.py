import vagrant
from fabric.api import env, execute, task, run

@task
def runTcpServer():
	run('echo "Inicia Task"')
	run('python3 ~/dev/python/tcp_server/tcp_server.py')


v = vagrant.Vagrant()
v.up()
env.hosts = [v.user_hostname_port()]
env.key_filename = v.keyfile()
env.disable_known_hosts = True # useful for when the vagrant box ip changes.
execute(runTcpServer) # run a fabric task on the vagrant host.