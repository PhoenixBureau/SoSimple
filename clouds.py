import os
from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver
from libcloud.compute.deployment import (
  MultiStepDeployment,
  ScriptDeployment,
  SSHKeyDeployment,
  FileDeployment,
  )


RACKSPACE_USER = os.environ['RACKSPACE_USER']
RACKSPACE_KEY = os.environ['RACKSPACE_KEY']
KEY_DATA = (
  'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDXzaAWCJnsvaFxPbwtprAKLH/f0rMvEt'
  'Pzy8W7Y9gkuQguGglEY26xFPWl68Ip54pMLxM2qsmutUHcdKwM2km1QKUk2z6P+SyBulww'
  '6sCSh2rcwBMiLVrric87K8RHf0AALNP/MG9S8HTVbql/EapRlgPP/zcBYJ9ugaagYZPW2T'
  'L9atS5of4WUpkmQ6GeJltclz1QWWHe8oachsikraKTrwjHa+F1UFKcnw7oWHQPp0iITH1E'
  '5GpUtyTi6Y45e4YFn1uz0vPdstLb3EjxF7nxHJwYBN6U7vQJr2rZV0DHREV+g+gfVLztcc'
  'RDgcbqmkN0Nf2T0XfdMrSI9yo89yIp sforman@hushmail.com'
  )
SCRIPT = '''\
#!/usr/bin/env bash
export UNAME=bob
export HOM=/home/$UNAME
adduser --disabled-password --gecos "" $UNAME
mkdir $HOM/.ssh
chmod og-rwx $HOM/.ssh
echo 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDXzaAWCJnsvaFxPbwtprAKLH/f0rMvEtPzy8W7Y9gkuQguGglEY26xFPWl68Ip54pMLxM2qsmutUHcdKwM2km1QKUk2z6P+SyBulww6sCSh2rcwBMiLVrric87K8RHf0AALNP/MG9S8HTVbql/EapRlgPP/zcBYJ9ugaagYZPW2TL9atS5of4WUpkmQ6GeJltclz1QWWHe8oachsikraKTrwjHa+F1UFKcnw7oWHQPp0iITH1E5GpUtyTi6Y45e4YFn1uz0vPdstLb3EjxF7nxHJwYBN6U7vQJr2rZV0DHREV+g+gfVLztccRDgcbqmkN0Nf2T0XfdMrSI9yo89yIp sforman@hushmail.com' \
  > $HOM/.ssh/authorized_keys
chmod og-rwx $HOM/.ssh/authorized_keys
chown -R $UNAME:$UNAME $HOM/.ssh

aptitude update && aptitude -y install git python-virtualenv python-pip

'''


Driver = get_driver(Provider.RACKSPACE)
conn = Driver(RACKSPACE_USER, RACKSPACE_KEY, region='ord')


msd = MultiStepDeployment([
  # Note: This key will be added to the authorized keys for the root user
  # (/root/.ssh/authorized_keys)
  SSHKeyDeployment(KEY_DATA),
  ScriptDeployment(SCRIPT),
  FileDeployment('start.script', '/home/bob/start.sh'),
  ])


# retrieve available images and sizes
d = dict((int(i.id), i) for i in conn.list_images())
s = dict((int(i.id), i) for i in conn.list_sizes())
loc = conn.list_locations()[0]


if __name__ == '__main__':
  if raw_input('y to make server') == 'y':
    node = conn.deploy_node(
      name='fred' + str(len(conn.list_nodes())),
      size=s[1],
      image=d[125],
      location=loc,
      deploy=msd,
      )
    print node, node.extra

