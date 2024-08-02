User guide
##############

Input files
=======================

Configuration file
------------------

The file simulation.ini contains all the basic configurations to run a simulation. This is an example of defining a configuration.

.. code-block:: bash
    
    $NB_PHOTONS 1000000000

+------------------------+---------------+----------------------------------------------------------------------+
| NB_PHOTONS             | int           | The number of photons used in the simulation                         |
+------------------------+---------------+----------------------------------------------------------------------+
| MAXIMUM_DEPTH          | int           | | The maximum number of times that the light bounces                 |
|                        |               | | in the scene                                                       |
+------------------------+---------------+----------------------------------------------------------------------+
| SCALE_FACTOR           | int           | | The size of geometries. The vertices of geometries                 |
|                        |               | | is recalculated by dividing their coordinates by                   |
|                        |               | | this value                                                         |
+------------------------+---------------+----------------------------------------------------------------------+
| T_MIN                  | int           | | The minimum distance between the point of                          |
|                        |               | | intersection and the origin of the light ray                       |
+------------------------+---------------+----------------------------------------------------------------------+
| NB_THREAD              | int           | | The number of threads on the CPU used to calculate in              |
|                        |               | | parallel. This value is between 0 and the number of                |
|                        |               | | cores of your CPU.                                                 |
+------------------------+---------------+----------------------------------------------------------------------+
| BACKFACE_CULLING       | yes/no        | | Define which mode of intersection is chosen: intersect             |
|                        |               | | only with the front face (yes) or intersect with both              |
|                        |               | | faces (no)                                                         |
+------------------------+---------------+----------------------------------------------------------------------+
| BASE_SPECTRAL_RANGE    | int int       | | The base spectral range which includes all the other               |
|                        |               | | spectral ranges. The first value is the start of band              |
|                        |               | | and the second is the end of band. Ex: 100 200                     |                               
+------------------------+---------------+----------------------------------------------------------------------+
| DIVIDED_SPECTRAL_RANGE | int [int int] | | The list of spectral ranges divided from the base                  |
|                        |               | | spectral range. The first value is the number of                   |
|                        |               | | divided parts, the value start and end of band is                  |
|                        |               | | continue right after. These bands have to be smaller               |
|                        |               | | than the base spectral range. Ex: 2 100 150 150 200                |
+------------------------+---------------+----------------------------------------------------------------------+

Room file
---------

| At this version, only files of type .rad is supported by our outil.
| More informations of file .rad can be found in this file `refman.pdf <https://github.com/minhlucky9/photon_mapping/tree/main/docs/refman.pdf>`_

Optical property files
----------------------

Captor file
-----------

Plant file
----------

Run a simulation
========================

Before starting to install the Photon Mapping tools, you should first install all dependencies in a conda environment. The simplest way to do this is to call

.. code-block:: bash
    
    conda env create -f environment.yml

You have to activate the conda environment before installing

.. code-block:: bash
    
    conda activate photonmap

To install as a Python library:

.. code-block:: bash
    
    python -m pip install ./

Visualize the room
========================

The main example is located in the folder ./examples/python/plantgl-rad-scene

.. code-block:: bash
    
    conda activate photonmap
    cd examples/python/plantgl-rad-scene

Command to run the example

.. code-block:: bash
    
    python planglRadScene.py

Test value Tmin
========================