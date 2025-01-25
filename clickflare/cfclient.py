from clickflare import config
from cloudflare import Cloudflare

class ClickFlareClient:

  def __init__(self):
    self.cf = Cloudflare(api_token=config.Config().token)