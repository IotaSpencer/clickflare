import click

from cfcli.lazy_group import LazyGroup


@click.group(cls=LazyGroup,
  lazy_subcommands={
    "logs": "cfcli.clis.accounts_logs.accounts_logs",
    "members": "cfcli.clis.accounts_members.accounts_members",
    "roles": "cfcli.clis.accounts_roles.accounts_roles",
    "subscriptions": "cfcli.clis.accounts_subscriptions.accounts_subscriptions",
    "tokens": "cfcli.clis.accounts_tokens.accounts_tokens",
  })

@click.pass_context
def accounts(ctx):
  pass

def create():
  pass

def delete():
  pass

def list():
  pass

def show():
  pass

def update():
  pass