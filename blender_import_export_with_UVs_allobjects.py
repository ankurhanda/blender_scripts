import sys
import bpy,bmesh

#print sys.argv[1]
print ("First argument: %s" % str(sys.argv[5]))

full_path_to_file = sys.argv[5] + '.obj' #"night_stand_0026.obj"
bpy.ops.import_scene.obj(filepath=full_path_to_file, use_edges=True, use_smooth_groups=True, use_split_objects=True, use_split_groups=True,use_groups_as_vgroups=False, use_image_search=True, split_mode='ON',global_clamp_size=0, axis_forward='-Z', axis_up='Y')


# Get the active mesh
#bpy.context.scene.objects.active = bpy.data.objects["night_stand_0026"]

D = bpy.data

objects = [obj for obj in D.objects if obj.type == 'OBJECT']

for obj in objects:

        objname = obj.name

        print(objname)

        bpy.context.scene.objects.active = bpy.data.objects[objname]
        bpy.ops.object.mode_set(mode='EDIT', toggle=False)

        obj = bpy.context.active_object
        me  = obj.data
        bm  = bmesh.from_edit_mesh(me)

        bpy.ops.uv.smart_project()

        bmesh.update_edit_mesh(me)

#obj_out = "export_copy.obj"
obj_out = sys.argv[5] + "_UVexported.obj"

bpy.ops.export_scene.obj(filepath=obj_out, axis_forward='-Z', axis_up='Y')

