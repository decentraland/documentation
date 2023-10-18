@ echo off

FOR %%F IN (*.GLB) DO (
	start "" /b GLTF-PIPELINE -i "%%F" -t -o "out/%%F"
)
PAUSE