# Export Normals
The script blender_import_export_with_Normals_obj.py allows you to export an OBJ format model with normals-map.

# Export UV maps

blender_import_export_with_UVs.py exports any OBJ model with smart UV mapping option in blender. 

# Smart UV projection and Export

If the mesh is further decomposed into multiple sub-meshes, blender_import_export_with_UVs_allobjects.py export the OBJ model with smart UV mapping for each sub-mesh.

#How to import obj file in blender and rename materials with their object names
```
~/workspace/code/blender-2.76b-linux-glibc211-x86_64/blender -b ../blender_scripts/dummy.blend --python ../blender_scripts/changematname_importOBJ.py bedroom1_layout.obj
```
#Explanation

```
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

bpy.ops.import_scene.obj(filepath=full_path_to_file,
                         #To ensure that objects and groups are preserved while importing
                         #use the following flags
                         use_split_groups=True, 
                         use_split_objects=True, 
                         use_image_search=True, 
                         use_smooth_groups=False, 
                         use_groups_as_vgroups=False)


C = bpy.context
D = bpy.data

objects = [obj for obj in D.objects if obj.type == 'MESH']

for obj in objects:
        objname=obj.name
            mat=D.materials.new(objname)
                obj.data.materials.clear()
                    obj.data.materials.append(mat)

obj_out = 'test.obj'

bpy.ops.export_scene.obj(filepath=obj_out, axis_forward='-Z', axis_up='Y'
                        use_normals=True, use_uvs=True, use_materials=True)

```
