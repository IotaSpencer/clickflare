import click
from clickflare import cfclient
from clickflare.lazy_group import LazyGroup

@click.group(cls=LazyGroup,
  lazy_subcommands={
    "list": "clickflare.clis.accounts_subscriptions.list_subscriptions",
    "show": "clickflare.clis.accounts_subscriptions.show",
    "update": "clickflare.clis.accounts_subscriptions.update",
    "delete": "clickflare.clis.accounts_subscriptions.delete"
  })
def accounts_subscriptions():
  """Manage Cloudflare account subscriptions."""
  pass

@click.command()
@click.option('--account-id', '-i', required=True, help='Account ID')
@click.option('--subscription-id', '-s', required=True, help='Subscription ID')
def show(account_id, subscription_id):
  """Get details of a specific subscription in an account."""
  cf = cfclient.ClickFlareClient()
  response = cf.cf.accounts.subscriptions.get(account_id=account_id, subscription_id=subscription_id)
  click.echo(response)

@click.command()
@click.option('--account-id', '-i', required=True, help='Account ID')
def list_subscriptions(account_id):
  """List all subscriptions in an account."""
  cf = cfclient.ClickFlareClient()
  response = cf.cf.accounts.subscriptions.list(account_id=account_id)
  click.echo(response)

if __name__ == '__main__':
  accounts_subscriptions()
  @click.command()
  @click.option('--account-id', '-i', required=True, help='Account ID')
  @click.option('--subscription-identifier', '-s', required=True, help='Subscription Identifier')
  @click.option('--frequency', '-f', required=True, help='Subscription frequency')
  def update(account_id: str, subscription_identifier: str, price_id: str, frequency: str, seats: int):
    """Update a subscription in an account."""
    cf = cfclient.ClickFlareClient()
    data = {
      "price_id": price_id,
      "frequency": frequency,
      "seats": seats
    }
    response = cf.cf.accounts.subscriptions.update(account_id=account_id, subscription_identifier=subscription_identifier, data=data)
    click.echo(response)

  @click.command()
  @click.option('--account-id', '-i', required=True, help='Account ID')
  @click.option('--subscription-identifier', '-s', required=True, help='Subscription Identifier')
  def delete(account_id: str, subscription_identifier: str):
    """Delete a subscription from an account."""
    cf = cfclient.ClickFlareClient()
    response = cf.cf.accounts.subscriptions.delete(account_id=account_id, subscription_identifier=subscription_identifier)
    click.echo(response)
    """Delete a subscription from an account."""
    cf = cfclient.ClickFlareClient()
    response = cf.cf.accounts.subscriptions.delete(account_id=account_id, subscription_identifier=subscription_identifier)
    click.echo(response)
  
## RatePlan
# id: Optional[str]
# The ID of the rate plan.

# currency: Optional[str]
# The currency applied to the rate plan subscription.

# externally_managed: Optional[bool]
# Whether this rate plan is managed externally from Cloudflare.

# is_contract: Optional[bool]
# Whether a rate plan is enterprise-based (or newly adopted term contract).

# public_name: Optional[str]
# The full name of the rate plan.

# scope: Optional[str]
# The scope that this rate plan applies to.

# sets: Optional[List[str]]
# The list of sets this rate plan applies to.