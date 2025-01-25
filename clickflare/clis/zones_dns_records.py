import click
from clickflare import cfclient
from clickflare.helpers import get_zone_id

@click.group()
@click.pass_context
def zones_dns_records(ctx):
  pass

@zones_dns_records.command('list', help='List DNS records', short_help='List DNS records')
@click.option('--zone', '-z', metavar="ZONE", required=True, help='Zone (Zone name (e.g. example.com))', type=str)
@click.option('--name', '-n', metavar="NAME", required=False, help='Name (Record name (e.g. example.com))', type=str)
@click.option('--name-contains', '-c', required=False, help='name.contains (Record name contains query parameter (e.g. example))', type=str)
@click.option('--name-startswith', required=False, help='name.startswith (Record name starts with query parameter (e.g. example))', type=str)
@click.option('--name-endswith', required=False, help='name.endswith (Record name ends with query parameter (e.g. example))', type=str)
@click.option('--type', '-t', metavar="TYPE", required=False, help='Type (Record type (e.g. A, CNAME, MX, etc))', type=str)
@click.option('--content', '-c', metavar="CONTENT", required=False, help='Content (Record content (e.g. 127.0.0.1))', type=str)
@click.option('--content-contains', '-o', metavar="CONTENT_SUBSTRING", required=False, help='content.contains (Record content contains query parameter (e.g. 127))', type=str)
@click.option('--content-startswith', metavar="CONTENT_PREFIX", required=False, help='content.startswith (Record content starts with query parameter (e.g. 127))', type=str)
@click.option('--content-endswith', metavar="CONTENT_SUFFIX", required=False, help='content.endswith (Record content ends with query parameter (e.g. 127))', type=str)
@click.option('--tag-absent', required=False, help='Name of a tag which must not be present on the DNS record. Tag filters are case-insensitive.', type=str)
@click.option('--tag-contains', metavar="TAG_SUBSTRING", required=False, help='A tag and value, of the form <tag-name>:<tag-value>. The API will only return DNS records that have a tag named <tag-name> whose value contains <tag-value>. Tag filters are case-insensitive.', type=str)
@click.option('--tag-endswith', metavar="TAG_SUFFIX", required=False, help='A tag and value, of the form <tag-name>:<tag-value>. The API will only return DNS records that have a tag named <tag-name> whose value ends with <tag-value>. Tag filters are case-insensitive.', type=str)
@click.option('--tag-startswith', metavar="TAG_PREFIX", required=False, help='A tag and value, of the form <tag-name>:<tag-value>. The API will only return DNS records that have a tag named <tag-name> whose value starts with <tag-value>. Tag filters are case-insensitive.', type=str)
@click.option('--tag-present', '-p', required=False, help='Name of a tag which must be present on the DNS record. Tag filters are case-insensitive.', type=str)
@click.option('--tag-match', required=False, help='List records that tag matches any or all of the specified properties', type=click.Choice(choices=['any', 'all']), )
@click.option('--proxiable', '-p', required=False, help='Proxiable (Whether the record is proxiable)', type=bool)
@click.option('--proxied', '-x', required=False, help='Proxied (Whether the record is proxied)', type=bool)
@click.option('--ttl', '-l', metavar="TTL_SECONDS", required=False, help='TTL (Record TTL in seconds (e.g. 120))', type=int)
@click.option('--locked', '-k', required=False, help='Locked (Whether the record is locked)', type=bool)
@click.option('--status', '-s', metavar="STATUS", required=False, help="Zone Status (Zone Status ('initializing', 'pending', 'active', 'moved'))", type=click.Choice(choices=['initializing', 'pending', 'active', 'moved']))
@click.option('--search', '-s', required=False, help='Search (Search query (Searches through all record properties))', type=str)
@click.option('--page', '-p', required=False, help='Page (Page number (e.g. 1))', type=int)
@click.option('--per-page', '-r', required=False, help='Per Page (Number of records per page (e.g. 20))', type=int)
@click.option('--order', '-o', required=False, help='Order (Order of records (e.g. name, type, content, ttl, proxiable, proxied, locked))', type=str)
@click.option('--direction', '-d', required=False, help='Direction (Direction of order (e.g. asc, desc))', type=click.Choice(choices=['asc', 'desc']), )
@click.option('--match', '-m', required=False, help='Match (Match type (e.g. all, any))', type=click.Choice(choices=['all', 'any']), )
@click.pass_context
def List(ctx, zone, name, type, content, proxiable, proxied, ttl, locked, **kwargs):
  print(kwargs)
  zone_id = get_zone_id(zone_name=zone)
  print(zone_id)
  cf = cfclient.ClickFlareClient()
  response = cf.cf.dns.records.list(zone_id=zone_id, extra_query=kwargs)
  print(response)
  
@zones_dns_records.command('add', help='Add a DNS record', short_help='Add a DNS record')
@click.option('--zone', '-z', required=True, help='Zone (Zone name (e.g. example.com))', type=str, prompt=True)
@click.option('--name', '-n', required=True, help='Name (Record name (e.g. example.com))', type=str, prompt=True)
@click.option('--type', '-t', required=True, help='Type (Record type (e.g. A, CNAME, MX, etc))', type=str, prompt=True)
@click.option('--data', '-d', required=True, help='Data (Record data (e.g. 127.0.0.1))', type=str, prompt=True)
@click.option('--ttl', '-l', required=True, prompt=True, help='TTL (Record TTL (e.g. 120, TTL must be between 60 and 86400 seconds, or 1 for Automatic.))', type=int)
@click.option('--priority', '-p', required=False, help='Priority (Record priority (e.g. 10))', type=int)
@click.option('--comment', '-m', required=False, help='Comment (Record comment (e.g. This is a comment))', type=str, prompt=True)
@click.option('--proxied', '-x', required=False, help='Proxied (Whether the record should be proxied)', type=bool)
@click.option('--tags', metavar="TAG",required=False, default=None, multiple=True, help='Tags (Record tags (e.g. --tags tag1:value1 --tags tag2:value2))', type=str)
def add(zone, name, type, data, ttl, priority, proxied, comment, tags, **kwargs):
  zone_id = get_zone_id(zone_name=zone)
  cf = cfclient.ClickFlareClient()
  response = cf.cf.dns.records.create(zone_id=zone_id, comment=comment, name=name, type=type, content=data, ttl=ttl, priority=priority, proxied=proxied, tags=tags, extra_query=kwargs)
  print(response)
  
@zones_dns_records.command('rem', help='Remove a DNS record', short_help='Remove a DNS record')
@click.option('--zone', '-z', required=True, help='Zone (Zone name (e.g. example.com))', type=str, prompt=True)
@click.option('--record-id', '-r', required=True, help='Record ID (Record ID (e.g. 1234567890abcdef1234567890abcdef))', type=str, prompt=True)
def rem(zone, record_id):
  zone_id = get_zone_id(zone_name=zone)
  cf = cfclient.ClickFlareClient()
  response = cf.cf.dns.records.delete(zone_id=zone_id, dns_record_id=record_id)
  print(response)
  