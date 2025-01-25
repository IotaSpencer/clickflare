import click
from clickflare import cfclient

from clickflare.lazy_group import LazyGroup

@click.group(cls=LazyGroup,
  lazy_subcommands={
    "dns_records": "clickflare.clis.zones_dns_records.zones_dns_records",
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
  cf = cfclient.ClickFlareClient()
  response = cf.cf.zones.list()
  print(response.result)
