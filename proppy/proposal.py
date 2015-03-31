

class Proposal(object):
  def __init__(self, data):
    self.project = data.get('project')
    self.work = data.get('work')
    self.costs = data.get('costs')
