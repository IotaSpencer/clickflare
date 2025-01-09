import click
from cfcli import cfclient
from cfcli.helpers import get_zone_id

@click.group()
@click.pass_context
def zones_dns_records(ctx):
  pass

@zones_dns_records.command('list')
@click.option('--zone', '-z', required=True, help='Zone (Zone name (e.g. example.com))', type=str)
@click.option('--status', '-s', required=True, help="Zone Status (Zone Status ('initializing', 'pending', 'active', 'moved'))", type=str)
@click.option('--name', '-n', required=True, help='Name (Record name (e.g. example.com))', type=str)
@click.option('--type', '-t', required=True, help='Type (Record type (e.g. A, CNAME, MX, etc))', type=str)
@click.option('--content', '-c', required=True, help='Content (Record content (e.g. 127.0.0.1))', type=str)
@click.option('--proxiable', '-p', required=True, help='Proxiable (Whether the record is proxiable)', type=bool)
@click.option('--proxied', '-x', required=True, help='Proxied (Whether the record is proxied)', type=bool)
@click.option('--ttl', '-l', required=True, help='TTL (Record TTL (e.g. 120))', type=int)
@click.option('--locked', '-k', required=True, help='Locked (Whether the record is locked)', type=bool)

@click.pass_context
def List(ctx, zone):
  zone_id = get_zone_id(zone_name=zone)
  print(zone_id)
  cf = cfclient.CFCLIClient()
  response = cf.cf.dns.records.list(zone_id=zone_id)
  print(response)
  
@zones_dns_records.command('add', help='Add a DNS record', short_help='Add a DNS record')
@click.option('--zone', '-z', required=True, help='Zone (Zone name (e.g. example.com))', type=str)
@click.option('--name', '-n', required=True, help='Name (Record name (e.g. example.com))', type=str)
@click.option('--type', '-t', required=True, help='Type (Record type (e.g. A, CNAME, MX, etc))', type=str)
@click.option('--data', '-d', required=True, help='Data (Record data (e.g. 127.0.0.1))', type=str)
@click.option('--ttl', '-l', required=True, help='TTL (Record TTL (e.g. 120, TTL must be between 60 and 86400 seconds, or 1 for Automatic.))', type=int)
@click.option('--priority', '-p', required=False, help='Priority (Record priority (e.g. 10))', type=int)
@click.option('--comment', '-m', required=False, help='Comment (Record comment (e.g. This is a comment))', type=str)
@click.option('--proxied', '-x', required=False, help='Proxied (Whether the record is proxied)', type=bool)
def add(zone, name, type, data, ttl, priority, proxied):
  zone_id = get_zone_id(zone_name=zone)
  cf = cfclient.CFCLIClient()
  response = cf.cf.dns.records.create(zone_id=zone_id, name=name, type=type, content=data, ttl=ttl, priority=priority, proxied=proxied)
  print(response)