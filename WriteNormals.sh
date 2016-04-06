# /bin/csh

w=`ls -d *`
for i in $w
do
cd $i

        ~/workspace/code/blender-2.76b-linux-glibc211-x86_64/blender ~/workspace/code/blender_scripts/dummy.blend --background --python ~/workspace/code/blender_scripts/blender_import_export_with_Normals_obj.py model.obj

cd ../

done

