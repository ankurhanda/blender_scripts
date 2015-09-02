import bpy,bmesh

full_path_to_file = "night_stand_0026.obj"
bpy.ops.import_scene.obj(filepath=full_path_to_file, use_edges=True, use_smooth_groups=True, use_split_objects=True, use_split_groups=True,use_groups_as_vgroups=False, use_image_search=True, split_mode='ON',global_clamp_size=0, axis_forward='-Z', axis_up='Y')


# Get the active mesh
#me = bpy.context.active_object
#bm = bmesh.from_edit_mesh(me)
bpy.context.scene.objects.active = bpy.data.objects["night_stand_0026"]

bpy.ops.object.mode_set(mode='EDIT', toggle=False)


obj = bpy.context.active_object
me = obj.data
bm = bmesh.from_edit_mesh(me)

#uv_layer = bm.loops.layers.uv.verify()
#bm.faces.layers.tex.verify()# currently blender needs both layers.

#adjust UVs
#for f in bm.faces:
#	for l in f.loops:
#		luv = l[uv_layer]
#		if luv.select: #apply the location of the vertex as a UV
#			luv.uv = l.vert.co.xy

bpy.ops.uv.smart_project()

#image = bpy.data.images.new(name="test.jpg", width=800, height=600)

#for uv_face in obj.data.uv_textures.active.data:
#    uv_face.image = image

#bpy.ops.object.bake_image()

name = "night_stand_0026"

mat = bpy.data.materials.new(name)

me.materials.append(mat)

bmesh.update_edit_mesh(me)

obj_out = "exporte_obj.obj"
 
bpy.ops.export_scene.obj(filepath=obj_out, axis_forward='-Z', axis_up='Y')
