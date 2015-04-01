import sys
import pytoml as toml

from proppy.exceptions import InvalidCommandException, InvalidConfigurationException
from proppy.proposal import Proposal

# with open('test.toml', 'rb') as fin:
#   obj = toml.load(fin)
#   loader = get_loader()
#   env = get_environment()
#   template = env.get_template('%s.html' % obj.get("theme"))
#   tmpl = template.render(proposal=obj)
#   create_pdf(tmpl)

def main(filename):
    if not filename.endswith('.toml'):
        raise InvalidCommandException("You must use a TOML file as input")

    with open(filename, 'rb') as f:
        print("Parsing %s" % filename)
        config = toml.load(f)
        theme = config.get('theme')
        if not theme:
            raise InvalidConfigurationException("Missing theme in TOML file")

        if not config.get('customer'):
            raise InvalidConfigurationException("Missing customer in TOML file")

        if not config.get('project'):
            raise InvalidConfigurationException("Missing customer in TOML file")

        proposal = Proposal(config)

        if proposal.is_valid():
            # Pass it to the template renderer
            pass
        else:
            # show errors and do nothing
            proposal.print_errors()

def run_main():
    if len(sys.argv) != 2:
        raise InvalidCommandException("Invalid number of arguments")

    main(sys.argv[1])


if __name__ == '__main__':
  run_main()
