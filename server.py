from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from model import MoneyModel

def agent_portrayal(agent):
    portrayal = {"Shape": "circle", "Color": "red", "Filled": "true", "Layer": 0, "r": 0.5}
    return portrayal

grid = CanvasGrid(agent_portrayal, 10, 10, 500, 500)

server = ModularServer(MoneyModel, [grid], "Money Model", {"N": 100, "width": 10, "height": 10})