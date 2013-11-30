import os
from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver


RACKSPACE_USER = os.environ['RACKSPACE_USER']
RACKSPACE_KEY = os.environ['RACKSPACE_KEY']


Driver = get_driver(Provider.RACKSPACE)
conn = Driver(RACKSPACE_USER, RACKSPACE_KEY)


# retrieve available images and sizes
images = conn.list_images()
sizes = conn.list_sizes()
nodes = conn.list_nodes()

for image in images:
  print image
print '-' * 73
for size in sizes:
  print size
print '-' * 73
for node in nodes:
  print node

