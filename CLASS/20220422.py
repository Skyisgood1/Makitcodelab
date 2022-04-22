#2022-04-22

#001

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
class Voxel(Button):
    def __init__(self, position = (0,0,0)):
        super().__init__(
            parent = scene,
            position = position,
            model = 'block',
            color = color.color(255,255,255),
            scale = 0.5
        )

    def input(self,key):
        if self.hovered:
            if key == 'left mouse down':
                Voxel(position = self.position + mouse.normal)
            elif key == 'right mouse down':
                destroy(self)

sky = Entity(
     parent = scene,
     model = 'sphere',
     texture = load_texture('ssunset.jpg'),
     scale = 500,
     double_sided = True
)
for z in range(20):
    for x in range(20):
        voxel = Voxel(position = (x,0,z))

player = FirstPersonController()

app.run()





















