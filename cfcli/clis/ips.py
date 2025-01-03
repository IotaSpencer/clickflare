import click
import os
from cfcli import config
from cfcli import cfclient

@click.command()
@click.pass_context
def ips(ctx):
  cf = cfclient.CFCLIClient()
  response = cf.cf.ips.list()
  print(response)