import click
from clickflare import cfclient

@click.command()
@click.option('--jdcloud', '-j', required=False, help="Whether to include JD Cloud IPs", type=bool)
@click.pass_context
def ips(ctx, jdcloud):
  cf = cfclient.ClickFlareClient()
  if jdcloud:
    response = cf.cf.ips.list(networks='jdcloud')
  else:
    response = cf.cf.ips.list(networks='')
  print(response)