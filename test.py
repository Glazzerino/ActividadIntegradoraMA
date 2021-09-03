
import agentpy as ap
import numpy as np
import matplotlib.pyplot as plt
import IPython
from model.Garage import Garage

parameters = {
   "size": 20,
   "robots": 5,
   "boxes": 10,
}

garage = Garage(parameters)

def animation_plot(model, ax):
   attr_grid = model.grid.attr_grid("condition")
   color_dict = {0:'#d62c2c', 1:'#7FC97F', 2:'#0000FF', 3:'#FFFF00', None:'#d5e5d5'}
   ap.gridplot(attr_grid, ax=ax, color_dict=color_dict, convert=True)
   ax.set_title(f"Look at my robots\n")
   
fig, ax = plt.subplots()
animation = ap.animate(garage, fig, ax, animation_plot)
IPython.display.HTML(animation.to_jshtml(fps=30))