from proppy.validators import (
    is_currency,
    is_date,
    is_percentage,
    is_present,
    are_valid_deliverables,
    are_valid_rates
)
from proppy.utils import (
    get_work_days_interval,
    to_date
)


class Proposal(object):
    validation_rules = {
        'customer.company': [is_present],
        'customer.person': [is_present],
        'customer.email': [is_present],

        'project.name': [is_present],
        'project.description': [is_present],
        'project.worker': [is_present],
        'project.currency': [is_present, is_currency],
        'project.discount': [is_percentage],

        'project.start': [is_present, is_date()],
        'project.end': [is_present, is_date()],
        'project.uat_start': [is_date(optional=True)],
        'project.uat_end': [is_date(optional=True)],

        'project.rates': [is_present, are_valid_rates],
        'project.deliverables': [is_present, are_valid_deliverables],
    }

    def __init__(self, config):
        self._errors = []
        # Not using .get below as we have already checked for them
        # when loading the toml
        self.customer = config['customer']
        self.project = config['project']

    def _fetch_value(self, field):
        """
        Allow dotted path to class objects dict, ie
        customer.company is equivalent to self.customer['company']
        """
        paths = field.split(".")
        base = getattr(self, paths[0])
        for key in paths[1:]:
            base = base.get(key)

        return base

    def basic_validation(self):
        """
        Only validates using the class validation dict: presence, type etc
        Does not check business logic
        """
        for field, rules in self.validation_rules.items():
            value = self._fetch_value(field)
            for rule in rules:
                valid = rule(value)
                # Only show one error at a time per field
                if not valid:
                    self._errors.append(rule.message % field)
                    break

    def logic_validation(self):
        """
        Ensure there's no 'stupid' data, like a UAT period
        lasting 1 month while the dev is 5 days or a 100% reduction.
        Also saves some of the computed data back on the project object
        for use in templates:
            - start_date
            - end_date
            - dev_length
            - sum_paid_deliverables
            - sum_free_deliverables
        """
        # can't have all the deliverable set to free
        if all(d['free'] for d in self.project['deliverables']):
            self._errors.append("Can't have all deliverables set to free")
            return

        deliverables = self.project['deliverables']
        # not using a rate we haven't specified in a deliverable
        rate_names = [rate['name'] for rate in self.project['rates']]
        if any(d['rate'] not in rate_names for d in deliverables):
            self._errors.append(
                "An unknown rate was used in a deliverable"
            )
            return

        # start and end dates are accurates given the estimates
        self.project['start_date'] = to_date(self.project['start'])
        self.project['end_date'] = to_date(self.project['end'])
        length_project = get_work_days_interval(
            self.project['start_date'], self.project['end_date']
        )
        dev_length = sum([d['estimate'] for d in deliverables])
        self.project['dev_length'] = dev_length
        dev_length /= self.project['worker']
        # not too short
        if dev_length > length_project:
            self._errors.append(
                "Project take more time than the timeline allows"
            )
            return
        # but not too long either
        if length_project > dev_length * 3:
            self._errors.append(
                "Project take way less time than the timeline shows"
            )
            return

        # UAT validation: needs to be after the end date of project
        # and should be shorter than the project
        # UAT is not mandatory though
        if 'uat_start' in self.project:
            self.project['uat_start_date'] = to_date(self.project['uat_start'])
            self.project['uat_end_date'] = to_date(self.project['uat_end'])
            if self.project['uat_start_date'] < self.project['end_date']:
                self._errors.append(
                    "UAT can't start before the end of the project"
                )
                return
            length_uat = get_work_days_interval(
                self.project['uat_start_date'], self.project['uat_end_date']
            )
            if length_uat > dev_length:
                self._errors.append(
                    "UAT can't take longer than the project itself"
                )
                return

        # And finally onto the costs validation
        day_rates = {r['name']: r['amount'] for r in self.project['rates']}

        # the sum we will invoice based on the deliverables itself
        sum_deliverables = 0
        # the sum we give away as a discount, ie free deliverables
        sum_free_deliverables = 0
        for d in deliverables:
            cost = d['estimate'] * day_rates[d['rate']]
            sum_deliverables += cost
            if d['free']:
                sum_free_deliverables += cost

        self.project['sum_deliverables'] = sum_deliverables
        self.project['sum_free_deliverables'] = sum_free_deliverables

        # now we need to check that the discount validation is not too high
        if self.project['discount'] > 20:
            self._errors.append("Discount is set too high")
            return

        self.project['discount_amount'] = (
            (sum_deliverables - sum_free_deliverables) / 100
            * self.project['discount']
        )

        self.project['invoice_amount'] = (
            sum_deliverables
            - sum_free_deliverables
            - self.project['discount_amount']
        )

    def is_valid(self):
        self.basic_validation()
        # If we get errors during basic validation, no need
        # to bother doing the business logic one
        if len(self._errors) > 0:
            return False

        # Call business logic before the return
        self.logic_validation()
        return len(self._errors) == 0

    def print_errors(self):
        print("ERRORS:")
        print('\n'.join(self._errors))
