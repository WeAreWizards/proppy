from proppy.proposal import Proposal


def _get_config():
    return {
        'customer': {
            'company': 'ACME',
            'email': 'boss@acme.com',
            'person': 'Bob Marley'
        },
        'project': {
            'name': 'Project X',
            'description': 'This is what we are supposed',
            'currency': '£',
            'discount': 5,
            'worker': 1,
            'start': '2015/03/18',
            'end': '2015/03/23',
            'uat_start': '2015/03/27',
            'uat_end': '2015/03/31',
            'rates': [
                {
                    'amount': 800,
                    'name': 'dev'
                },
                {
                    'amount': 700,
                    'name': 'pm'
                },
                {
                    'amount': 750,
                    'name': 'design'
                }
                ],
            'deliverables': [
                {
                    'name': 'Fix Facebook and Twitter integration',
                    'estimate': 2,
                    'rate': 'dev',
                    'free': False,
                    'description': 'Ensure those are working properly'
                },
                {
                    'name': 'Add a badge list page',
                    'estimate': 0.5,
                    'rate': 'design',
                    'free': True,
                    'description': 'Add a badge list page in the profile'
                }
            ]
        }
    }


def test_fetch_value():
    config = _get_config()
    proposal = Proposal(config=config)
    customer = config['customer']
    assert proposal._fetch_value('customer') == customer
    assert proposal._fetch_value('customer.company') == customer['company']
    assert proposal._fetch_value('project.rates') == config['project']['rates']
    assert proposal._fetch_value('customer.nonexistent') is None


def test_basic_validation_one_error():
    wrong_config = _get_config()
    del wrong_config['customer']['email']
    proposal = Proposal(config=wrong_config)
    proposal.basic_validation()
    assert len(proposal._errors) == 1
    assert "Field customer.email is missing" == proposal._errors[0]


def test_basic_several_several_errors_in_a_field():
    """
    Validation should stop at first failure for a field
    """
    wrong_config = _get_config()
    wrong_config['project']['currency'] = ''
    proposal = Proposal(config=wrong_config)
    proposal.basic_validation()
    assert len(proposal._errors) == 1
    assert "Field project.currency is missing" == proposal._errors[0]


def test_logic_validation_not_doing_everything_free():
    wrong_config = _get_config()
    wrong_config['project']['deliverables'][0]['free'] = True
    proposal = Proposal(config=wrong_config)
    proposal.logic_validation()
    assert len(proposal._errors) == 1
    assert "Can't have all deliverables set to free" == proposal._errors[0]


def test_logic_validation_unknown_rate_in_deliverable():
    wrong_config = _get_config()
    wrong_config['project']['deliverables'][1]['rate'] = 'magic'
    proposal = Proposal(config=wrong_config)
    proposal.logic_validation()
    assert len(proposal._errors) == 1
    assert "An unknown rate was used in a deliverable" == proposal._errors[0]


def test_logic_validation_timeline_too_short():
    wrong_config = _get_config()
    wrong_config['project']['start'] = '2015/03/25'
    proposal = Proposal(config=wrong_config)
    proposal.logic_validation()
    assert len(proposal._errors) == 1
    assert "Project take more time than the timeline allows" == proposal._errors[0]  # NOQA


def test_logic_validation_timeline_too_long():
    wrong_config = _get_config()
    wrong_config['project']['start'] = '2015/02/25'
    proposal = Proposal(config=wrong_config)
    proposal.logic_validation()
    assert len(proposal._errors) == 1
    assert "Project take way less time than the timeline shows" == proposal._errors[0]  # NOQA


def test_logic_validation_uat_starting_during_project():
    wrong_config = _get_config()
    wrong_config['project']['uat_start'] = '2015/03/19'
    proposal = Proposal(config=wrong_config)
    proposal.logic_validation()
    assert len(proposal._errors) == 1
    assert "UAT can't start before the end of the project" == proposal._errors[0]  # NOQA


def test_logic_validation_uat_too_long():
    wrong_config = _get_config()
    wrong_config['project']['uat_end'] = '2015/04/19'
    proposal = Proposal(config=wrong_config)
    proposal.logic_validation()
    assert len(proposal._errors) == 1
    assert "UAT can't take longer than the project itself" == proposal._errors[0]  # NOQA

def test_logic_validation_discount_too_high():
    wrong_config = _get_config()
    wrong_config['project']['discount'] = 50
    proposal = Proposal(config=wrong_config)
    proposal.logic_validation()
    assert len(proposal._errors) == 1
    assert "Discount is set too high" == proposal._errors[0]  # NOQA
