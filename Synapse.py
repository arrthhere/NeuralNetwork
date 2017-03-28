class Synapse(object):
    _weight = None

    def __init__(self, weight):
        self._weight = weight

    def get_weight(self):
        return self._weight