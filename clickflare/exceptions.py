import click
class NotImplementedError(click.ClickException):
    def __init__(self, exit_code, message):
      """
      Initializes the NotImplementedError with a custom message.

      Args:
          message (str): The error message to display.

      Attributes:
          message (str): Stores the error message.
          exit_code (int): Exit code for the error, defaults to 1.
      """

      super(NotImplementedError, self).__init__(message)
      self.message = message
      self.exit_code = exit_code or 1
      self.show()