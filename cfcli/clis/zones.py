import click

@click.group()
def zones():
  pass

@click.command('list')
def List():
  raise click.NotImplementedError