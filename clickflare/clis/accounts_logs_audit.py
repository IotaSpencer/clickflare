import click
from clickflare import cfclient

import clickflare
from clickflare.lazy_group import LazyGroup

@click.group(name="audit", cls=LazyGroup)
def accounts_logs_audit():
  pass

@accounts_logs_audit.command()
@click.decorators
def list():
  raise clickflare.NotImplementedError("Endpoint is in beta and not yet implemented")