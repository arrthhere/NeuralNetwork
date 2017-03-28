from Neuron import *

class NeuralNetwork(object):

    def __init__(self, input_layer_size, hidden_layers_num, hidden_layer_size, output_layer_size):
        self._neurons_count = 0

        self._input_layer = []
        for i in range(input_layer_size):
            self._neurons_count += 1
            self._input_layer.append(Neuron(self._neurons_count, True))

        self._hidden_layers = []
        for i in range(hidden_layers_num):
            self._hidden_layers.append([])
            for j in range(hidden_layer_size):
                self._neurons_count += 1
                self._hidden_layers[i].append(Neuron(self._neurons_count, False))

        self._output_layer = []
        for i in range(output_layer_size):
            self._neurons_count += 1
            self._output_layer.append(Neuron(self._neurons_count, False))

        self._synapses = {}
        self._synapses[(1, 3)] = 0.45
        self._synapses[(1, 4)] = 0.78
        self._synapses[(2, 3)] = -0.12
        self._synapses[(2, 4)] = 0.13
        self._synapses[(3, 5)] = 1.5
        self._synapses[(4, 5)] = -2.3

        self.calculate([1, 0])

    def calculate(self, input_data):
        for i in range(len(input_data)):
            self._input_layer[i].add_input_data(input_data[i])
            self._input_layer[i].activate()

        for i in range(len(self._hidden_layers[0])):
            for j in range(len(self._input_layer)):
                id1 = self._input_layer[j].get_id()
                id2 = self._hidden_layers[0][i].get_id()
                self._hidden_layers[0][i].add_input_data(self._input_layer[j].get_output_data() * self._synapses[(id1, id2)])

            self._hidden_layers[0][i].activate()

       # for layer_count in range(1, len(self._hidden_layers)):
       #     for i in range(len(self._hidden_layers[layer_count])):
       #         for j in range(len(self._hidden_layers[layer_count - 1])):
       #             id1 = self._hidden_layers[layer_count - 1][j]
       #             id2 = self._hidden_layers[layer_count][i]
       #             self._hidden_layers[layer_count][i].add_input_data(self._hidden_layers[layer_count - 1][j].get_output_data() * self._synapses[(id1, id2)])
       #     self._hidden_layers[layer_count][i].activate()

        for i in range(len(self._output_layer)):
            last_hidden_layer = len(self._hidden_layers) - 1
            for j in range(len(self._hidden_layers[last_hidden_layer])):
                id1 = self._hidden_layers[last_hidden_layer][j].get_id()
                id2 = self._output_layer[i].get_id()
                self._output_layer[i].add_input_data(self._hidden_layers[last_hidden_layer][j].get_output_data() * self._synapses[(id1, id2)])
            self._output_layer[i].activate()
            print(self._output_layer[i].get_output_data())
