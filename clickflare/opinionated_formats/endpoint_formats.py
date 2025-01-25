class EndpointFormats:
  TABLE = 'table'
  YAML = 'yaml'
  
  @staticmethod
  def all():
    return [EndpointFormats.TABLE, EndpointFormats.YAML]
  
  @staticmethod
  def default():
    return EndpointFormats.YAML
  
  @staticmethod
  def get(format):
    return format if format in EndpointFormats.all() else EndpointFormats.default()
  
  @staticmethod
  def is_supported(format):
    return format in EndpointFormats.all()
  
  @staticmethod
  def is_default(format):
    return format == EndpointFormats.default()
  
  @staticmethod
  def is_table(format):
    return format == EndpointFormats.TABLE
  
  @staticmethod
  def is_yaml(format):
    return format == EndpointFormats.YAML
  
  @staticmethod
  def get_format_for_endpoint(endpoint, format):
    pass