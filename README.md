# NND
Neural Networks Designer

<img src='https://img.shields.io/badge/made%20for-DNN%20hackers-blue'>
  

### Repo content
* [dnn_designer](./dnn_designer/), package for designing neural networks.
* [nbs](./nbs/), examples notebooks directory.

### Status
Beginnning. There is a PoC in [first_test.ipynb](./dnn_designer/first_test.ipynb), based on a couple of functions written in [funx.py](./dnn_designer/funx.py).  
The flow i still too much disconnected, must be adjusted to be more dev friendly.
  
Example of current flow:
1. define shapes by name (function) and position (x,y,z).
2. define the scene (`voxelarray`) and the shapes colors.
3. plot everything
    1. eventually add text labels to the shapes

##### Issues
1. A dev should not pass by the (2) step
2. plotting should be more user friendly, accepting angle as well.
3. Adding labels should be flaggable and automatically done.

