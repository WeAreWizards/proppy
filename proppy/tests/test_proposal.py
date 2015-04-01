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
            'start': '2015/03/18',
            'end': '2015/03/26',
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
                    'estimate': 1,
                    'rate': 'dev',
                    'description': 'Ensure those are working properly'
                },
                {
                    'name': 'Add a badge list page',
                    'estimate': 0.5,
                    'rate': 'design',
                    'description': 'Add a badge list page in the profile'
                }
            ],
            'costs': [
                {
                    'discount_fixed': 500,
                    'discount_percentage': 5
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
