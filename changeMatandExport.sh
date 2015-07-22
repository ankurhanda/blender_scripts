#!/bin/sh

cd $1
for f in *.blend
do
  filename="${f##*/}"
  print ${filename}
  extension="${filename##*.}"
  filename="${filename%.*}.obj"
  ~/workspace/code/blender-2.71-linux-glibc211-x86_64/blender -b $f --python /home/ankur/workspace/code/metricScaledSynthCam3D/changematname.py -- $filename
done

