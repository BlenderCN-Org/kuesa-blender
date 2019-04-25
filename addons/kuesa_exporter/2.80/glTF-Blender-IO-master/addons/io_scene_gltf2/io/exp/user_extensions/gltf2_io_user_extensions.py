# Copyright 2019 The glTF-Blender-IO authors.
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

import glob
import imp
import importlib
import os.path
from io_scene_gltf2.io.com.gltf2_io_extensions import Extension

class UserExtensionBase:

    def export(self, export_settings, glTF) -> Extension:
        return None


class UserExtensionLoader:
    """Dynamically load extension modules for custom user extensions"""
    def __init__(self):
        files = [
            os.path.basename(f)[:-3]
            for f in glob.glob(os.path.dirname(__file__) + '/extensions/*.py')
            if os.path.isfile(f)
        ]
        modules = [f for f in files if not f.startswith('_')]

        if '_IMPORTED' not in locals():
            _IMPORTED = True

        self.extensions = []
        for module in modules:
            module = importlib.import_module('..extensions.' + module, __name__)
            if '_IMPORTED' in locals():
                imp.reload(module)
            for attr in [getattr(module, attr) for attr in dir(module)]:
                if hasattr(attr, 'meta'):
                    self.extensions.append(attr)
