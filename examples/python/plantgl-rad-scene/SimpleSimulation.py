from photonmap.Simulator import *
from openalea.plantgl.all import * 

if __name__ == "__main__":

    simulator = Simulator()

    #setup configuration
    simulator.nb_photons = 1000000
    simulator.max_depth = 5

    simulator.resetScene()

    #setup environment
    ground_ts = TriangleSet(pointList = [(0,0,0), (1,0,0), (0,1,0)], indexList = [(0, 2, 1)])
    ground_mat = Material(
                        name="Ground",
                        ambient = Color3(0,0,0),
                        specular = Color3( 127 ), #spec = 0.5 = 127/255
                        shininess = 1,
                        transparency = 0
                    )
    ground_sh = Shape(ground_ts, ground_mat)

    simulator.addEnvToScene(ground_sh)

    #setup light
    light_ts = TriangleSet(pointList = [(0,0,5), (1,0,5), (0,1,5)], indexList = [(0, 1, 2)])
    light_mat = Material(
                        name="Light",
                        emission = Color3(255, 255, 255)
                    )
    light_sh = Shape(light_ts, light_mat)
    simulator.addEnvToScene(light_sh)

    #setup captor
    captor_ts = TriangleSet(pointList = [(0,0,1), (1,0,0), (0,1,0)], indexList = [(0, 1, 2)])
    simulator.addCaptorToScene(captor_ts, (0,0,3))

    #run
    res = simulator.run()
    simulator.writeResults()