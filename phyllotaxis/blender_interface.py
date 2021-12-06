import bpy
import math

OUTPUT_RENDER = 'render.png'
OUTPUT_MODEL = 'model.fbx'
MODEL_A_PATH = 'phyllotaxis/3d_models/seed.fbx'
MODEL_A_SCALE = (0.25, 0.25, 0.18)
MODEL_B_PATH = 'phyllotaxis/3d_models/small_petal.fbx'
MODEL_B_SCALE = (1.0, 1.0, 1.0)
MODEL_C_PATH = 'phyllotaxis/3d_models/petal.fbx'
MODEL_C_SCALE = (1.3, 2, 1.0)

class Blender:
    def __init__(self, phyllotaxis, inner_circle_threshold=0.60, middle_circle_threshold=0.77):
        self.phyllotaxis = phyllotaxis
        self.inner_circle_threshold = inner_circle_threshold
        self.middle_circle_threshold = middle_circle_threshold
        for obj in bpy.data.objects:
            if obj.name == 'Camera':
                obj.location = (0,0, 1.9* math.sqrt(len(self.phyllotaxis.get_node_list())) + 10)
                obj.rotation_euler = (math.radians(0),math.radians(0),math.radians(0))
        for obj in bpy.data.objects:
            if obj.name == 'Cube':
                bpy.data.objects.remove(obj)
    
    def get_tetha(self, x, y):
        if x + math.sqrt(x**2 + y**2) == 0:
            tetha = 2 * math.atan(math.inf if y > 0 else -1 * math.inf)
        else:
            tetha = 2 * math.atan(y / (x + math.sqrt(x**2 + y**2)))
        return tetha - math.pi/2

    def render(self):
        for i, node in enumerate(self.phyllotaxis.get_node_list()):
            x, y =  node.get_position()
            
            if i < len(self.phyllotaxis.get_node_list()) * self.inner_circle_threshold:
                bpy.ops.import_scene.fbx(filepath=MODEL_A_PATH)
                bpy.data.objects[-1].scale = MODEL_A_SCALE
                bpy.data.objects[-1].location = (x*0.01, y*0.01, 0.0)
            elif i < len(self.phyllotaxis.get_node_list()) * self.middle_circle_threshold:
                bpy.ops.import_scene.fbx(filepath=MODEL_B_PATH)
                bpy.data.objects[-1].scale=MODEL_B_SCALE
                bpy.data.objects[-1].location = (x*0.01, y*0.01, 0.15)
            else:
                bpy.ops.import_scene.fbx(filepath=MODEL_C_PATH)
                bpy.data.objects[-1].scale=MODEL_C_SCALE
                bpy.data.objects[-1].location = (x*0.01, y*0.01, 0.0)
            
            tetha = self.get_tetha(x, y)
            bpy.data.objects[-1].rotation_euler=(0, 0, tetha)

        bpy.ops.export_scene.fbx(filepath=OUTPUT_MODEL)
        bpy.context.scene.render.filepath = OUTPUT_RENDER
        bpy.ops.render.render(write_still=True)

