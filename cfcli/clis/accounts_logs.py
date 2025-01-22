import click

from cfcli.lazy_group import LazyGroup

@click.group(name="logs", cls=LazyGroup,
  lazy_subcommands={
    "audit_logs": "cfcli.clis.accounts_logs_audit.accounts_logs_audit",
}, help="Manage Cloudflare account logs.")
def accounts_logs():
  pass