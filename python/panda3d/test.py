from direct.showbase.ShowBase import ShowBase
from math import pi, sin, cos
from direct.task import Task
from direct.actor.Actor import Actor

__default_model_path__ = "D:/anaconda/Lib/site-packages/panda3d/models/"


class MyTestApp(ShowBase):
    def __init__(self):
        super().__init__(self)
        self.environ = self.loader.loadModel("models/environment")
        self.environ.reparentTo(
            self.render)  #self.render 渲染树根节点，设置之后才能对所有元素进行渲染
        self.environ.setScale(0.25, 0.25, 0.25)
        self.environ.setPos(-8, 42, 0)
        self.taskMgr.add(self.spinCameraTask,
                         'SpinCameraTask')  #调用任务spinCameraTask()
        self.panda()

    def spinCameraTask(self, task):
        angleDegrees = task.time * 6
        angleRadians = angleDegrees * (pi / 180)
        self.camera.setPos(20 * sin(angleRadians), -20 * cos(angleRadians), 3)
        self.camera.setHpr(angleDegrees, 0, 0)
        return Task.cont

    def panda(self):
        self.pandaActor = Actor(
            {
                'p1': 'models/panda-model',
                'p2': 'models/panda'
            }, {
                'p1': {
                    'walk': 'models/panda-walk4'
                },
                'p2': {
                    'walk': 'models/panda-walk'
                }
            })
        self.pandaActor.setScale(0.005, 0.005, 0.005)
        self.pandaActor.reparentTo(
            self.render)  #self.render 渲染树根节点，设置以后才能对所有元素进行渲染
        # self.pandaActor.loop('walk')
        # self.pandaActor.loop("work2")
        self.pandaActor.attach('p1','p2','waist')

    def box(self):
        ...


if __name__ == "__main__":
    app = MyTestApp()
    app.run()