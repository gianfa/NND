"""
NND/$ pytest dnn_designer -vv -s
"""
import pytest
from dnn_designer.funx import *
from dnn_designer.designer import Designer

@pytest.fixture
def nd():
    return Designer()

def test_get_layers_by_key_val(nd):
    nd.layers = [
        {
            'name': 'lay1',
            'type': 'Dense',
        },
        {
            'name': 'lay2',
            'type': 'Conv1D',
        },
        {
            'name': 'lay3',
            'type': 'Dense',
        },
    ]
    lay1s = nd.get_layers_by_key_val('name', 'lay1')
    assert type(lay1s) == list
    assert lay1s[0] == {'name': 'lay1','type': 'Dense',}

    layDenses = nd.get_layers_by_key_val('type', 'Dense')
    assert type(layDenses) == list
    assert len(layDenses) == 2
    assert layDenses == [
        {
            'name': 'lay1',
            'type': 'Dense',
        },
        {
            'name': 'lay3',
            'type': 'Dense',
        },
    ]

def test_check_is_known_layer_type(nd):
    with pytest.raises(Exception):
        nd.check_is_known_layer_type('invented-layer-type')

    lts = ['Dense', 'FC', 'Conv1D', 'Conv2D']
    [ nd.check_is_known_layer_type(lt) for lt in lts]

def test_add_layer():
    nd_noname = Designer()
    nd_noname.add_layer(
        'Dense'
    )
    assert len(nd_noname.layers)==1
    assert nd_noname.layers == [{
        'color': 'blue',
        'type': 'Dense',
        'name': 'Dense-0'
        }]

    nd_noname.add_layer(
        'Dense'
    )
    assert len(nd_noname.layers)==2
    assert nd_noname.layers == [{
            'color': 'blue',
            'type': 'Dense',
            'name': 'Dense-0'
            },
            {
            'color': 'blue',
            'type': 'Dense',
            'name': 'Dense-1'
            }
        ]

    nd_named = Designer()
    nd_named.add_layer(
        layer_type='Dense',
        name='first_layer'
    )
    assert len(nd_named.layers)==1
    assert nd_named.layers == [{
        'color': 'blue',
        'type': 'Dense',
        'name': 'first_layer'
        }]

def test__len__(nd):
    len(nd) == 0
    nd.add_layer(
        'Dense'
    )
    len(nd) == 1
    nd.add_layer(
        'Conv1D'
    )
    len(nd) == 2

def test__str__(nd):
    len(nd) == 0
    nd.add_layer(
        'Dense'
    )
    nd.add_layer(
        'Conv1D'
    )
    print("")
    print(nd)
    breakpoint()

#TODO
def test_check_layername_is_new(nd):
    pass