import click
from cfcli import cfclient

from cfcli.lazy_group import LazyGroup

@click.group(cls=LazyGroup,
  lazy_subcommands={
    "dns_records": "cfcli.clis.zones_dns_records.zones_dns_records",
  })

@click.pass_context
def zones(ctx):
  pass

@zones.command('list')
@click.option('--name', '-n', required=True, help='Zone (Zone name (e.g. example.com))', type=str)
@click.option('--status', '-s', required=True, help="Zone Status (Zone Status ('initializing', 'pending', 'active', 'moved'))", type=str)
@click.pass_context
def List(ctx):
  print(ctx.parent.parent.params)
  cf = cfclient.CFCLIClient()
  response = cf.cf.zones.list()
  print(response.result)
