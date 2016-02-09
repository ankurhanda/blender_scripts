import sys
import bpy,bmesh


#How to run the script: http://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/Import-Export/Wavefront_OBJ

#print sys.argv[1]
print ("First argument: %s" % str(sys.argv[5]))

full_path_to_file = sys.argv[5] # + '.obj' #"night_stand_0026.obj"
bpy.ops.import_scene.obj(filepath=full_path_to_file, use_edges=True, use_smooth_groups=True, use_split_objects=True, use_split_groups=True,use_groups_as_vgroups=False, use_image_search=True, split_mode='ON',global_clamp_size=0, axis_forward='-Z', axis_up='Y')



obj_out = "export_copy.obj"
#obj_out = sys.argv[5] + "_copy.obj"
 
bpy.ops.export_scene.obj(filepath=obj_out, axis_forward='-Z', axis_up='Y', use_normals=True)
