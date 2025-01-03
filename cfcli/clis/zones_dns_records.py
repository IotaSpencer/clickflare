import click
from cfcli import cfclient

@click.group()
@click.pass_context
def zones_dns_records(ctx):
  pass

@zones_dns_records.command('list')
@click.pass_context
def List(ctx):
  print(ctx.output)
  cf = cfclient.CFCLIClient()
  response = cf.cf.zones_dns_records.list()
  print(response)