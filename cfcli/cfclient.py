from cfcli import config
from cloudflare import Cloudflare

class CFCLIClient:

  def __init__(self):
    self.cf = Cloudflare(api_token=config.Config().token)