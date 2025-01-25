import toml
import pathlib


class Config:
  def __init__(self):
    cfg_path = pathlib.Path.home() / '.clickflare/config'
    cfg = None
    with open(cfg_path, 'r') as cfg_file:
      cfg = toml.load(cfg_file)
    
    self.token = cfg['cf-api']['token']
