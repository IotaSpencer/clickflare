import tomllib
import pathlib


class Config:
  def __init__(self):
    cfg_path = pathlib.Path.home() / '.cfcli/config'
    cfg = None
    with open(cfg_path, 'rb') as cfg_file:
      cfg = tomllib.load(cfg_file)
    
    self.token = cfg['cfcli-api']['token']
