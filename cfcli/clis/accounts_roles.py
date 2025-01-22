import click
from cfcli import cfclient
from cfcli.lazy_group import LazyGroup

@click.group(cls=LazyGroup,
  lazy_subcommands={
    "list": "cfcli.clis.accounts_roles.list_roles",
    "show": "cfcli.clis.accounts_roles.show",
  })
def accounts_roles():
  """Manage Cloudflare account roles."""
  pass

@click.command()
@click.option('--account-id', '-i', required=True, help='Account ID')
@click.option('--role-id', '-r', required=True, help='Role ID')
def show(account_id, role_id):
  """Get details of a specific role in an account."""
  cf = cfclient.CFCLIClient()
  response = cf.cf.accounts.roles.get(account_id=account_id, role_id=role_id)
  click.echo(response)

@click.command()
@click.argument('account_id')
@click.option('--api-token', required=True, help='Cloudflare API token')
def list_roles(account_id):
  """List all roles in an account."""
  cf = cfclient.CFCLIClient()
  response = cf.cf.accounts.roles.list(account_id=account_id)
  click.echo(response)
  


if __name__ == '__main__':
  accounts_roles()