from math import pi, sin, cos

from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Point3

class MyApp(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)

        #disable mouse controls
        self.disableMouse()

        # Load the environment model.
        self.scene = self.loader.loadModel("models/environment")
        # Reparent the model to render.
        self.scene.reparentTo(self.render)
        # Apply scale and position transforms on the model.
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8, 42, -40)

        #add spin camera task to task manager
        self.taskMgr.add(self.spinCamera, "SpinCameraTask")

        #add in a panda
        self.pandaActor = Actor("models/panda-model", {"walk":"models/panda-walk4"})
        self.pandaActor.setScale(0.005, 0.005, 0.005)
        self.pandaActor.reparentTo(self.render)
        #loop the animation
        self.pandaActor.loop("walk")

        #create 4 intervals for the panda to walk back and forth
        pandaPosInterval1 = self.pandaActor.posInterval(13, Point3(0, -10, 0), startPos=Point3(0, -10, 0))
        pandaPosInterval2 = self.pandaActor.posInterval(13, Point3(0, 10, 0), startPos=Point3(0,0,0))
        pandaHprInterval1 = self.pandaActor.hprInterval(3, Point3(180, 0, 0), startHpr=Point3(0,0,0))
        pandaHprInterval2 = self.pandaActor.hprInterval(3, Point3(0,0,0), startHpr=Point3(180,0,0))

        #create and play the sequence coordinating the intervals
        self.pandaPace = Sequence(pandaPosInterval1,
                                    pandaHprInterval1,
                                    pandaPosInterval2,
                                    pandaHprInterval2,
                                    name="pandaPace")
        self.pandaPace.loop()


    #this is how we spin the camera
    def spinCamera(self, task):
        angleDegrees = task.time * 6.0
        angleRadians = angleDegrees * (pi / 180.0)
        self.camera.setPos(20 * sin(angleRadians), -20.0 * cos(angleRadians), 3)
        self.camera.setHpr(angleDegrees, -50, 0)
        return Task.cont

app = MyApp()
app.run()
