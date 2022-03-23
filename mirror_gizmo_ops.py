# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#   https://github.com/Korchy/ilya_shichkin_mirror_gizmo

from bpy.props import IntProperty, EnumProperty
from bpy.types import Operator
from bpy.utils import register_class, unregister_class


class MIRROR_GIZMO_OT_mirror(Operator):
    bl_idname = 'mirror_gizmo.mirror'
    bl_label = 'Mirror Gizmo'
    bl_description = 'Mirror Gizmo'
    bl_options = {'REGISTER', 'UNDO'}

    angle: IntProperty(
        name='Angle',
        default=90,
        subtype='UNSIGNED',
        min=0,
        max=360
    )

    axis: EnumProperty(
        name='Axis',
        items=[
            ('X', 'X', 'X'),
            ('NEG_X', '-X', '-X'),
            ('Y', 'Y', 'Y'),
            ('NEG_Y', '-Y', '-Y'),
            ('Z', 'Z', 'Z'),
            ('NEG_Z', '-Z', '-Z')
        ],
        default='X',
        # default={'X'},
        # options={'ENUM_FLAG'}
    )

    def execute(self, context):
        print(self.angle, self.axis)
        return {'FINISHED'}

    @classmethod
    def poll(cls, context):
        return context.area.type == 'VIEW_3D' and context.mode == 'EDIT_MESH'


def register():
    register_class(MIRROR_GIZMO_OT_mirror)


def unregister():
    unregister_class(MIRROR_GIZMO_OT_mirror)
