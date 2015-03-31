import pytoml as toml

from pdf import create_pdf
from templates import get_loader, get_environment


with open('test.toml', 'rb') as fin:
  obj = toml.load(fin)
  loader = get_loader()
  env = get_environment()
  template = env.get_template('%s.html' % obj.get("theme"))
  tmpl = template.render(proposal=obj)
  print(tmpl)
  create_pdf(tmpl)
