from bpy.props import BoolProperty
from io_scene_gltf2.io.exp.user_extensions.gltf2_io_user_extensions import UserExtensionBase
from io_scene_gltf2.io.com.gltf2_io_extensions import Extension, ChildOfRootExtension

class KDABKuesaLayers(UserExtensionBase):
    meta = {
        'name': 'KDAB_Kuesa_Layers',
        'isDraft': False,
        'enable': True,
        'url': (
            'https://www.kdab.com'
        ),
    }

    def export(self, blender_object, export_settings):
        # Export per node layers
        kuesa_layer_names = []

        if 'kuesa' in blender_obj.keys() and 'layers' in blender_object.kuesa.keys():
            node_layer_names = [layer.name for layer in blender_object.kuesa.layers]
            if node_layer_names:
                # Child Extension (on node)
                child_extension = ChildOfRootExtension(
                    name=self.meta.name, 
                    path=['layers'],
                    extension=node_layer_names
                )
                # Root Extension (in root gltf)
                extension = Extension(
                    name=self.meta.name,
                    extension={'layers' : child_extension}
                )

                return extension
        return None