import click
from clickflare import cfclient

import clickflare

from clickflare.lazy_group import LazyGroup

@click.group(name="members", cls=LazyGroup,
  lazy_subcommands={
    "list": "clickflare.clis.accounts_members.accounts_members.list",
    "add": "clickflare.clis.accounts_members.accounts_members.add",
    "delete": "clickflare.clis.accounts_members.accounts_members.delete",
    "show": "clickflare.clis.accounts_members.accounts_members.show",
    "update": "clickflare.clis.accounts_members.accounts_members.update",
  }, help="Manage Cloudflare Account members")
def accounts_members():
  pass

@accounts_members.command()
@click.option('--account-id', '-a', required=True, help="Account ID", type=str)
@click.option('--member-id', '-m', required=True, help="Member ID", type=str)
def delete(account_id, member_id):
  cf = cfclient.ClickFlareClient()
  response = cf.cf.accounts.members.delete(account_id=account_id, member_id=member_id)
  print(response)
  
@accounts_members.command()
@click.option('--account-id', '-a', required=True, help="Account ID", type=str)
@click.option('--member-id', '-m', required=True, help="Member ID", type=str)
def show(account_id, member_id):
  cf = cfclient.ClickFlareClient()
  response = cf.cf.accounts.members.get(account_id=account_id, member_id=member_id)
  print(response)
  
@accounts_members.command()
@click.option('--account-id', '-a', required=True, help="Account ID", type=str)
@click.option('--member-id', '-m', required=True, help="Member ID", type=str)
@click.option('--role-ids', '-r', required=True, help="Role ID", type=str, multiple=True)
def update(account_id, member_id, role_ids):
  cf = cfclient.ClickFlareClient()
  response = cf.cf.accounts.members.update(account_id=account_id, member_id=member_id, roles=role_ids)
  print(response)