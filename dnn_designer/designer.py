from typing import Any
from functools import reduce
import matplotlib.pyplot as plt
import numpy as np

from .funx import *
from .layers import LAYERS

class Designer():

    def __init__(self, name:str='', dnn_constructor:str=None):
        self.name = name
        self.layers = []
        self.axes = None
        self.dnn_constructor = dnn_constructor # for later (Keras, TF,...)

    def get_layers_by_key_val(self, key:str, value:Any) -> list:
        return [l for l in self.layers if l[key]==value]

    def get_layers_by_type(self, layer_type:str) -> list:
        return self.get_layers_by_key_val('type', layer_type)

    def check_is_known_layer_type(self, layer_type:str):
        if not layer_type in LAYERS.keys():
            raise KeyError(f"Unkonwn layer type '{layer_type}'." +\
                f" Allowed layer types: {LAYERS.keys()}"
                )

    def check_layername_is_new(self, name:str):
        if len(self.get_layers_by_key_val('name', name))>0:
            raise Exception(f"Name '{name}' already present for a stored layer."+\
                f" Please provide another name"
                )

    def create_layer(self, name:str, layer_type:str):
        layer = LAYERS[layer_type].copy()
        layer['name'] = name
        return layer

    def add_layer(
        self,
        layer_type:str, 
        name:str=None
    ):
        # TODO: add args specific for the layers
        self.check_is_known_layer_type(layer_type)
        if not name is None:
            self.check_layername_is_new(name)
        else:
            n_lays_type = len(self.get_layers_by_type(layer_type))
            name = f"{layer_type}-{n_lays_type}" # e.g. "Dense-9"
        self.layers.append(self.create_layer(name, layer_type))

    def render(self, angle:float=None):
        # prepare some coordinates
        X_len = 20
        Y_len = 20
        Z_len = 20
        X, Y, Z = np.indices((X_len, Y_len, Z_len))
        self.axes = (X, Y, Z)

        # draw_shapes #
        LAYERS_MARGIN = 1
        """
        Here we define a pointer in order to sequentially
        add up the layers.
        It's defined by xp, yp, zp.
        """
        xp, yp, zp = 0, 0, 0 # bottom left corner of 3D axes

        shapes = []
        poses = []
        for l in self.layers:
            if l['type'] == 'Dense':
                pos = (xp, yp, zp)
                shapes.append(draw_Dense(l['units'], pos, self.axes))
                poses.append(pos)
                xp, yp, zp = xp+1+LAYERS_MARGIN, yp, zp
            elif l['type'] == 'Dense2D':
                pos = (xp, yp, zp)
                shapes.append(draw_Dense2D(*l['units'], pos, self.axes))
                poses.append(pos)
                xp, yp, zp = xp+1+LAYERS_MARGIN, yp, zp
            else:
                raise NotImplementedError(f"Just be patience for a little while")

        # combine shapes #
        voxelarray = reduce(lambda x,y: x|y, shapes)

        # set the colors #
        colors = np.empty(voxelarray.shape, dtype=object)
        for shape, l in zip(shapes, self.layers):
            colors[shape] = l['color']

        # PLOT #
        ## Start the plot ##
        ax = plt.figure(figsize=(10,10)).add_subplot(projection='3d')
        ax.voxels(voxelarray, facecolors=colors, edgecolor='k')
        # Title #
        ax.text(2, Y_len/2, Z_len*0.9,self.name, fontsize=22)
        # Layers labels #
        # for shape, p, l in zip(shapes, poses, self.layers):
        #     ax.text(p[0], -1, 0,r'Input(Dense(10x10))', fontsize=11)
        # Rotate the plot 3D #
        # ax.view_init(30, angle)
        # Remove plot grid and axis #
        plt.grid(False)
        plt.axis('off')
        plt.show()


    def __len__(self):
        return len(self.layers)

    def __str__(self):
        network = f"\n"+" "*8+"NETWORK\n" + "_"*26 + "\n"
        layers = [f"{l['name'].ljust(10)} | {l['type']}" for l in self.layers]
        layers_sep = ("\n" + "_"*26 + "\n")
        return network + layers_sep.join(layers)