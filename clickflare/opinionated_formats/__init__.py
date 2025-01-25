from typing import Any


def to_format(data, format, endpoint: str) -> Any:
  """
  Convert data to the specified format for a given endpoint.

  Args:
      data: The data to be formatted.
      format: The desired format for the data. Supported formats are 'table' and 'yaml'.
      endpoint (str): The endpoint associated with the data.

  Returns:
      The formatted data if the format is supported.

  Raises:
      ValueError: If an unsupported format is specified.
  """

  if format == 'table':
    return data
  elif format == 'yaml':
    return data
  else:
    raise ValueError(f'Unknown format: {format}')