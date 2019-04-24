# Copyright (c) 2018 The Khronos Group Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import bpy
import os
import sys

try:
    argv = sys.argv
    if "--" in argv:
        argv = argv[argv.index("--") + 1:]  # get all args after "--"
    else:
        argv = []

    filepath = argv[0]

    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.import_scene.gltf(filepath=argv[0])

    extension = '.gltf'
    if '--glb' in argv:
        extension = '.glb'

    path = os.path.splitext(filepath)[0] + extension
    path_parts = os.path.split(path)
    output_dir = os.path.join(path_parts[0], argv[1])
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    if extension == '.glb':
        bpy.ops.export_scene.gltf(export_format='GLB', filepath=os.path.join(output_dir, path_parts[1]))
    else:
        bpy.ops.export_scene.gltf(export_format='GLTF_SEPARATE', filepath=os.path.join(output_dir, path_parts[1]))
except Exception as err:
    print(err, file=sys.stderr)
    sys.exit(1)
