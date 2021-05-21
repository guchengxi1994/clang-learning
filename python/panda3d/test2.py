from math import pi, sin, cos

from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Point3

class MyApp(ShowBase):
    def __init__(self):
        super(MyApp, self).__init__()

        # 加载场景模型（场景树）
        self.scene = self.loader.loadModel("models/environment")
        # 将render设为场景模型的父节点
        self.scene.reparentTo(self.render)

        # 改变场景大小，并设置镜头初始位置
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8, 42, 0)

        # 在任务管理器中添加滚动相机任务
        self.task_mgr.add(self.spinCameraTask, "SpinCameraTask")

        # 加载场景角色(一只熊猫)
        self.pandaActor = Actor(models="models/panda-model",
                                anims={"walk":"models/panda-walk4"})
        # 设置熊猫大小
        self.pandaActor.setScale(0.005, 0.005, 0.005)
        # 将熊猫加入渲染列表
        self.pandaActor.reparentTo(self.render)
        # 加入熊猫的循环动画
        self.pandaActor.loop("walk")

        # 创建interval，使得熊猫前后走动
        # interval参数: [持续时间（s）， 最终的状态， 起始状态]
        posInterval1 = self.pandaActor.posInterval(13,
                                                   Point3(0, -10, 0),
                                                   startPos=Point3(0, 10, 0))
        posInterval2 = self.pandaActor.posInterval(13,
                                                   Point3(0, 10, 0),
                                                   startPos=Point3(0, -10, 0))
        hprInterval1 = self.pandaActor.hprInterval(3,
                                                   Point3(180, 0, 0),
                                                   startHpr=Point3(0, 0, 0))
        hprInterval2 = self.pandaActor.hprInterval(3,
                                                   Point3(0, 0, 0),
                                                   startHpr=Point3(180, 0, 0))
        # 创建sequence（间隔组）
        self.pandaPace = Sequence(posInterval1, hprInterval1,
                                  posInterval2, hprInterval2,
                                  name="pandaPace")
        # 使用loop方法开启间隔组
        self.pandaPace.loop()

    # 定义移动相机的任务
    def spinCameraTask(self, task):
        # 获取一个随时间变化的角度
        angleDegrees = task.time * 6.0      # 镜头每秒转6度
        # 转换成弧度制
        angleRadians = angleDegrees * (pi / 180.0)
        # 重新顶点相机的位置
        self.camera.setPos(20 * sin(angleRadians), -20 * cos(angleRadians), 3)
        # 重新设置角度
        self.camera.setHpr(angleDegrees, 0, 0)
        return Task.cont

app = MyApp()
app.run()