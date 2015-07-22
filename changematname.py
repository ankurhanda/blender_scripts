import bpy
import sys

C = bpy.context
D = bpy.data

objects = [obj for obj in D.objects if obj.type == 'MESH']

for obj in objects:
    objname=obj.name
    mat=D.materials.new(objname)
    obj.data.materials.clear()
    obj.data.materials.append(mat)   
   
argv = sys.argv
argv = argv[argv.index("--") + 1:] # get all args after "--"
 
obj_out = argv[0]
 
bpy.ops.export_scene.obj(filepath=obj_out, axis_forward='-Z', axis_up='Y')
