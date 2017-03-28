import math

class Neuron(object):

    def __init__(self, id, is_input_neuron):
        self._id = id
        self._is_input_neuron = is_input_neuron
        self._input_data = 0
        self._output_data = 0

    def __repr__(self):
        return "id: %d, input data: %d, output data: %d" % (self._id, self._input_data, self._output_data)

    def activate(self):
        if self._is_input_neuron:
            self._output_data = self._input_data
        else:
            self._output_data = 1.0 / (1 + math.exp(-self._input_data))

    def clear(self):
        self._input_data = 0
        self._output_data = 0

    def get_id(self):
        return self._id

    def add_input_data(self, input_data):
        self._input_data += input_data

    def get_output_data(self):
        return self._output_data



