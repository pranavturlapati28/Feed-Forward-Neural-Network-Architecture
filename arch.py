import random
import tkinter as tk
class Node:
    def __init__(self):
        self.strength = 0.0
        self.connections = []

    def set_Strength(self, strength: float) -> None:
        self.strength = strength

    def get_Strength(self) -> float:
        return self.strength

    def addCon(self, connection):
        self.connections.append(connection)
        
        
class Connection:
    weight = 0.0
    def __init__(self, node1, node2):
        self.Node1 = node1
        self.Node2 = node2
    def set_weight(self, weight):
        self.weight = weight
    def get_weight(self):
        return weight
    def getNode1(self) -> Node:
        return self.Node1
    def getNode2(self) -> Node:
        return self.Node2


class Layer:
    def __init__(self, node_layer=None):
        self.node_layer = node_layer or []

    def build(self, n_nodes):
        for _ in range(n_nodes):
            self.node_layer.append(Node())

    def get_layer(self):
        return self.node_layer

    def __str__(self):
        rv = ""
        for node in self.node_layer:
            print(f"Node: {node.get_Strength()}")
            rv += f"Node: {node.get_Strength()}|"
        return rv


class TNetwork:
    def __init__(self, layer1, layer2):
        self.layer1 = layer1
        self.layer2 = layer2

    def bCon(self):
        for node1 in self.layer1.get_layer():
            for node2 in self.layer2.get_layer():
                connection = Connection(node1, node2)
                # Assign a random weight to the connection in the range [-1, 1]
                weight = random.uniform(-1, 1)
                connection.set_weight(weight)
                node1.addCon(connection)
                
                
class NetworkDisplay(tk.Tk):
    def __init__(self, network):
        super().__init__()
        self.title("Neural Network Display")
        self.geometry("800x600")

        self.network = network
        self.node_ovals = {}  # Dictionary to store oval objects for nodes

        self.canvas = tk.Canvas(self, bg="white", width=800, height=600)
        self.canvas.pack()

    def draw_network(self):
        self.canvas.delete("all")
        self.node_ovals.clear()  # Clear the dictionary before redrawing

        layer1_nodes = self.network.layer1.get_layer()
        layer2_nodes = self.network.layer2.get_layer()

        # Draw nodes in layer1
        for i, node in enumerate(layer1_nodes):
            x = 100
            y = 100 + i * 50
            node_oval = self.canvas.create_oval(x-10, y-10, x+10, y+10, fill="blue")
            self.canvas.create_text(x+30, y, text=f"Node {i+1}")
            self.node_ovals[node] = node_oval

        # Draw nodes in layer2
        for i, node in enumerate(layer2_nodes):
            x = 500
            y = 100 + i * 50
            node_oval = self.canvas.create_oval(x-10, y-10, x+10, y+10, fill="green")
            self.canvas.create_text(x-30, y, text=f"Node {i+1}")
            self.node_ovals[node] = node_oval

        # Draw connections
        for node1 in layer1_nodes:
            for connection in node1.connections:
                node2 = connection.getNode2()
                x1, y1, x2, y2 = self.canvas.coords(self.node_ovals[node1])
                x3, y3, x4, y4 = self.canvas.coords(self.node_ovals[node2])
                x1_center, y1_center = (x1 + x2) / 2, (y1 + y2) / 2
                x2_center, y2_center = (x3 + x4) / 2, (y3 + y4) / 2
                self.canvas.create_line(x1_center, y1_center, x2_center, y2_center, arrow=tk.LAST)
