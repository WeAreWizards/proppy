import os

from jinja2 import Environment, FileSystemLoader


class ThemeNotFound(Exception):
  pass


def get_loader():
  theme_path = os.path.dirname(os.path.abspath(__file__))
  theme_path = os.path.join(theme_path, "themes")

  return FileSystemLoader(theme_path)


def get_environment():
  return Environment(
    trim_blocks=True,
    lstrip_blocks=True,
    loader=get_loader()
  )

