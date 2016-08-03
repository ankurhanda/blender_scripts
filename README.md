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
