import sys
import pytoml as toml

from proppy.exceptions import InvalidCommand, InvalidConfiguration
from proppy.proposal import Proposal
from proppy.render import to_pdf_wkhtml


def main(filename):
    if not filename.endswith('.toml'):
        raise InvalidCommand("You must use a TOML file as input")

    with open(filename, 'rb') as f:
        print("Parsing %s" % filename)
        config = toml.load(f)
        theme = config.get('theme')
        if not theme:
            raise InvalidConfiguration("Missing theme in TOML file")

        if not config.get('customer'):
            raise InvalidConfiguration("Missing customer in TOML file")

        if not config.get('project'):
            raise InvalidConfiguration("Missing project in TOML file")

        proposal = Proposal(config)

        if proposal.is_valid():
            print("Valid proposal, saving it.")
            to_pdf_wkhtml(theme, proposal)
            print("Proposal rendered and saved.")
            exit(0)
        else:
            # show errors and do nothing
            proposal.print_errors()
            exit(1)


def run_main():
    if len(sys.argv) != 2:
        raise InvalidCommand("Invalid number of arguments")

    main(sys.argv[1])


if __name__ == '__main__':
    run_main()
