from clickflare import cfclient


def get_zone_id(zone_name):
  """
  Retrieve the zone ID for a given zone name.
  
  Args:
    zone_name (str): The name of the zone for which to retrieve the ID.
  Returns:
    str: The ID of the zone if found, otherwise None.
  Raises:
    Exception: If there is an error in retrieving the zone information.
  """
  
  cf = cfclient.ClickFlareClient()
  response = cf.cf.zones.list(match='all', name=zone_name)
  return response.result[0].id