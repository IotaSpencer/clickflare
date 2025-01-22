import click
from cfcli import cfclient

import cfcli
from cfcli.lazy_group import LazyGroup

@click.group(name="audit", cls=LazyGroup)
def accounts_logs_audit():
  pass

@accounts_logs_audit.command()
@click.decorators
def list():
  raise cfcli.NotImplementedError("Endpoint is in beta and not yet implemented")