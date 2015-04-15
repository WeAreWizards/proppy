import os
import subprocess
import tempfile

from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML


def to_html(theme, proposal):
    """
    Loads a jinja2 template specified in the toml file (no custom
    path for now) and renders it giving the proposal data as
    a context
    """
    theme_path = os.path.dirname(os.path.abspath(__file__))
    theme_path = os.path.join(theme_path, "themes")

    env = Environment(
        trim_blocks=True,
        lstrip_blocks=True,
        loader=FileSystemLoader(theme_path)
    )
    template = env.get_template('%s.html' % theme)

    return template.render(
        project=proposal.project,
        customer=proposal.customer
    )


def to_pdf(theme, proposal):
    """
    First get the HTML and then render it as a PDF.
    TODO: change output file
    """
    html = to_html(theme, proposal)
    HTML(string=html).write_pdf('out.pdf')


def to_pdf_wkhtml(theme, proposal):
    """
    First get the HTML and then render it as a PDF.
    TODO: change output file
    """
    html = to_html(theme, proposal)
    with tempfile.NamedTemporaryFile(suffix='.html') as f:
        f.write(html.encode('utf8'))
        f.flush()
        subprocess.check_call(['wkhtmltopdf', '--print-media-type', f.name, 'out.pdf'])
