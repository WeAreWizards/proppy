from weasyprint import HTML, CSS


def create_pdf(html):
  HTML(string=html).write_pdf('out.pdf')
