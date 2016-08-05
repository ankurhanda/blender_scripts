import sys
import bpy,bmesh

print ("First argument: %s" % str(sys.argv[5]))

full_path_to_file = sys.argv[5] #+ '.obj' #"night_stand_0026.obj"
bpy.ops.import_scene.obj(filepath=full_path_to_file, use_edges=True, use_smooth_groups=True, use_split_objects=True, use_split_groups=True,use_groups_as_vgroups=False, use_image_search=True, split_mode='ON',global_clamp_size=0, axis_forward='-Z', axis_up='Y')


cube_map_list = ['balcony',
'bench',
'bin',
'board',
'carpet',
'ceiling',
'cupboard',
'curtain',
'curtains',
'desk',
'door',
'doorframe',
'doors',
'drawer',
'drawers',
'fireplace',
'floor',
'frame',
'fridge',
'furniture',
'mat',
'plant',
'plants',
'rack',
'rail',
'railing',
'shower',
'shower_bath',
'table',
'terrace',
'wall',
'walls',
'wardrobe',
'window',
'window_frame',
'windows'
]


for obj in bpy.data.objects:
    print(obj.name)
    if obj.name != "Camera" and obj.name != "Lamp" :
        bpy.context.scene.objects.active = bpy.data.objects[obj.name]
        if obj.name.lower() in cube_map_list:
            bpy.ops.object.editmode_toggle()
            bpy.ops.uv.cube_project()
            bpy.ops.object.editmode_toggle()
        else:
            bpy.ops.object.mode_set(mode='EDIT', toggle=False)
            bpy.ops.uv.smart_project()


obj_out = sys.argv[5] + "_UVexported.obj"

bpy.ops.export_scene.obj(filepath=obj_out, axis_forward='-Z', axis_up='Y',use_normals=True, use_uvs=True, use_materials=True)

