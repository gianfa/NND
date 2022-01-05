from .funx import *

# [NOTUSED] Supposed to be a prototype for a generic layer
LAYER_PROTO = {
    'color': 'blue',
    'type': None,
    'dims': None,
    'pos': None
}

# constructor template for layers
LAYERS = {
    'Dense':{
        'color': 'blue',
        'type': 'Dense',
        'units': 0,
    },
    'FC':{
        'color': 'green',
        'type': 'FC',
    },
    'Conv1D':{
        'color': 'yellow',
        'type': 'Conv1D',
    },
    'Conv2D':{
        'color': 'red',
        'type': 'Conv2D',
    },

}