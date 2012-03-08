
from djfab import *

_setup(
  envs=dict(
    public=dict(
      # django settings
      project_name='instadoc',
      requirements_file='requirements/apps.txt',
      # linux remote host settings
      environment='public',
      os=CONST.OS.DEBIAN,
      hosts=["aegis.ca-net.org"],
      server_name="instadoc.ca-net.org",
      linux_user='instadoc',
      linux_group='instadoc',
      linux_user_ssh_keys=[
      ],
      application_server=CONST.APPLICATION_SERVER.WSGI,
      web_server=CONST.WEB_SERVER.APACHE,
    ),
  ),
)
