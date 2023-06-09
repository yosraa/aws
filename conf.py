from typing import Dict

class Config:
  DEBUG = False
  AWS_EXTRA_PARAMETERS: dict[str, str] = {}

  
class LocalConfig(Config):
  DEBUG = True
  AWS_EXTRA_PARAMETERS = {"endpoint_url": ""}
  
config_by_name = dict(
  local=LocalConfig,
)
