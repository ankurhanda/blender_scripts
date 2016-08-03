import bpy, bmesh
import sys

print ("First argument: %s" % str(sys.argv[5]))
full_path_to_file = sys.argv[5] # + '.obj' #"night_stand_0026.obj"


print('sys.argv[0] =', sys.argv[0])
print('sys.argv[1] =', sys.argv[1])
print('sys.argv[2] =', sys.argv[2])
print('sys.argv[3] =', sys.argv[3])
print('sys.argv[4] =', sys.argv[4])
print('sys.argv[5] =', sys.argv[5])

bpy.ops.import_scene.obj(filepath=full_path_to_file, use_split_groups=True, use_split_objects=True, use_image_search=True, use_smooth_groups=False, use_groups_as_vgroups=False)


C = bpy.context
D = bpy.data

objects = [obj for obj in D.objects if obj.type == 'MESH']

for obj in objects:
    objname=obj.name
    mat=D.materials.new(objname)
    obj.data.materials.clear()
    obj.data.materials.append(mat)   
   
#argv = sys.argv
#argv = argv[argv.index("--") + 1:] # get all args after "--"
 
obj_out = 'test.obj'
 
bpy.ops.export_scene.obj(filepath=obj_out, axis_forward='-Z', axis_up='Y')
