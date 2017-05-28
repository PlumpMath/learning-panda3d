from direct.showbase.ShowBase import ShowBase   # import the bits of panda
from panda3d.core import GeoMipTerrain          # that we need

class MyApp(ShowBase):                          # our 'class'
    def __init__(self):
        ShowBase.__init__(self)                        # initialise
        terrain = GeoMipTerrain("worldTerrain")        # create a terrain
        terrain.setHeightfield("mapheight.png")        # set the height map
        terrain.setColorMap("maptex.png")           # set the colour map
        terrain.setBruteforce(True)                    # level of detail
        root = terrain.getRoot()                       # capture root
        root.reparentTo(render)                        # render from root
        root.setSz(60)                                 # maximum height
        terrain.generate()                             # generate

app = MyApp()                                   # our 'object'
app.run()                                       # away we go

#well that is interesting
#    Hold down the left mouse button and you should find you can move the camera left/right and up/down.
#    Hold down the right mouse button and you will be able to zoom in/out.
#    Hold down both mouse buttons and you will be able to rotate the camera.

