
def validate_presence(value):
  return value is not None


def validate_currency(value):
  return value in ["£"]


def validate_percentage(value):
  """
  0 is a pretty useless percentage in a proposal
  so counting it as falsy
  """
  return 0 < value <= 100


