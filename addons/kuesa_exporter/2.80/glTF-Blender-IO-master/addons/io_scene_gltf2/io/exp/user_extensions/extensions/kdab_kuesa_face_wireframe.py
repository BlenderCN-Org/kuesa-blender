from bpy.props import BoolProperty
from io_scene_gltf2.io.exp.user_extensions.gltf2_io_user_extensions import UserExtensionBase

class KDABKuesaFaceWireframe(UserExtensionBase):
    meta = {
        'name': 'KDAB_Kuesa_FaceWireframe',
        'isDraft': False,
        'enable': True,
        'url': (
            'https://www.kdab.com'
        ),
        'settings': {
            'export_face_wireframe': BoolProperty(
                name='Export as Face Wireframe',
                description='Export geometry as per face lines instead of triangles',
                default=False
            )
        },
    }

    KDAB_kuesa_extension_name = 'KDAB_Kuesa_FaceWireframe'

    def export(self, export_settings, glTF):
        pass
