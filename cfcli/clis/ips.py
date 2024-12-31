import click
import os
from cfcli import config
from cfcli import cfclient

@click.command()
def ips():
  cf = cfclient.CFCLIClient()
  response = cf.cf.ips.list()
  print(response)