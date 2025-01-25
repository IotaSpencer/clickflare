import click

from clickflare.lazy_group import LazyGroup


@click.group(cls=LazyGroup,
  lazy_subcommands={
    "logs": "clickflare.clis.accounts_logs.accounts_logs",
    "members": "clickflare.clis.accounts_members.accounts_members",
    "roles": "clickflare.clis.accounts_roles.accounts_roles",
    "subscriptions": "clickflare.clis.accounts_subscriptions.accounts_subscriptions",
    "tokens": "clickflare.clis.accounts_tokens.accounts_tokens",
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