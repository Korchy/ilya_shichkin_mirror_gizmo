# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#   https://github.com/Korchy/ilya_shichkin_mirror_gizmo

from bpy.types import Panel
from bpy.utils import register_class, unregister_class


class MIRROR_GIZMO_PT_panel(Panel):
    bl_idname = 'MIRROR_GIZMO_PT_panel'
    bl_label = 'Mirror Gizmo'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Mirror Gizmo'

    def draw(self, context):
        layout = self.layout
        layout.operator(
            operator='mirror_gizmo.mirror',
            icon='BLENDER',
            text='Mirror Gizmo'
        )


def register():
    register_class(MIRROR_GIZMO_PT_panel)


def unregister():
    unregister_class(MIRROR_GIZMO_PT_panel)
