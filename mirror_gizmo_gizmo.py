# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#   https://github.com/Korchy/ilya_shichkin_mirror_gizmo

from bpy.types import GizmoGroup
from bpy.utils import register_class, unregister_class
from math import radians
from mathutils import Matrix


class MIRROR_GIZMO_GT_mirror(GizmoGroup):
    bl_idname = 'mirror_gizmo.mirror'
    bl_label = 'Mirror Gizmo'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'WINDOW'
    bl_options = {'3D', 'SELECT'}

    def setup(self, context):
        # Z
        gizmo = self.gizmos.new('GIZMO_GT_arrow_3d')
        # operator
        op = gizmo.target_set_operator(
            operator='mirror_gizmo.mirror'
        )
        op.axis = 'Z'
        op.angle = 0
        # location
        m = Matrix.LocRotScale(
            context.scene.cursor.location,
            None,
            None
        )
        gizmo.matrix_basis = m.normalized()
        # draw
        gizmo.draw_style = 'BOX'
        gizmo.color = 0.0, 0.0, 1.0
        gizmo.alpha = 0.5
        gizmo.color_highlight = 1.0, 0.5, 1.0
        gizmo.alpha_highlight = 0.5
        # local link
        self.z = gizmo

        # NEG_Z
        gizmo = self.gizmos.new('GIZMO_GT_arrow_3d')
        # operator
        op = gizmo.target_set_operator(
            operator='mirror_gizmo.mirror'
        )
        op.axis = 'NEG_Z'
        op.angle = 0
        # location
        m = Matrix.LocRotScale(
            context.scene.cursor.location,
            Matrix.Rotation(radians(180.0), 4, 'X').to_3x3(),
            None
        )
        gizmo.matrix_basis = m.normalized()
        # draw
        gizmo.draw_style = 'BOX'
        gizmo.color = 0.0, 0.0, 1.0
        gizmo.alpha = 0.2
        gizmo.color_highlight = 1.0, 0.5, 1.0
        gizmo.alpha_highlight = 0.2
        # local link
        self.neg_z = gizmo

        # X
        gizmo = self.gizmos.new('GIZMO_GT_arrow_3d')
        # operator
        op = gizmo.target_set_operator(
            operator='mirror_gizmo.mirror'
        )
        op.axis = 'X'
        op.angle = 0
        # location
        m = Matrix.LocRotScale(
            context.scene.cursor.location,
            Matrix.Rotation(radians(90.0), 4, 'Y').to_3x3(),
            None
        )
        gizmo.matrix_basis = m.normalized()
        # draw
        gizmo.draw_style = 'BOX'
        gizmo.color = 1.0, 0.0, 0.0
        gizmo.alpha = 0.5
        gizmo.color_highlight = 1.0, 0.5, 1.0
        gizmo.alpha_highlight = 0.5
        # local link
        self.x = gizmo

        # NEG_X
        gizmo = self.gizmos.new('GIZMO_GT_arrow_3d')
        # operator
        op = gizmo.target_set_operator(
            operator='mirror_gizmo.mirror'
        )
        op.axis = 'NEG_X'
        op.angle = 0
        # location
        m = Matrix.LocRotScale(
            context.scene.cursor.location,
            Matrix.Rotation(radians(-90.0), 4, 'Y').to_3x3(),
            None
        )
        gizmo.matrix_basis = m.normalized()
        # draw
        gizmo.draw_style = 'BOX'
        gizmo.color = 1.0, 0.0, 0.0
        gizmo.alpha = 0.2
        gizmo.color_highlight = 1.0, 0.5, 1.0
        gizmo.alpha_highlight = 0.2
        # local link
        self.neg_x = gizmo

        # Y
        gizmo = self.gizmos.new('GIZMO_GT_arrow_3d')
        # operator
        op = gizmo.target_set_operator(
            operator='mirror_gizmo.mirror'
        )
        op.axis = 'Y'
        op.angle = 0
        # location
        m = Matrix.LocRotScale(
            context.scene.cursor.location,
            Matrix.Rotation(radians(90.0), 4, 'X').to_3x3(),
            None
        )
        gizmo.matrix_basis = m.normalized()
        # draw
        gizmo.draw_style = 'BOX'
        gizmo.color = 0.0, 1.0, 0.0
        gizmo.alpha = 0.5
        gizmo.color_highlight = 1.0, 0.5, 1.0
        gizmo.alpha_highlight = 0.5
        # local link
        self.y = gizmo

        # NEG_Y
        gizmo = self.gizmos.new('GIZMO_GT_arrow_3d')
        # operator
        op = gizmo.target_set_operator(
            operator='mirror_gizmo.mirror'
        )
        op.axis = 'NEG_Y'
        op.angle = 0
        # location
        m = Matrix.LocRotScale(
            context.scene.cursor.location,
            Matrix.Rotation(radians(-90.0), 4, 'X').to_3x3(),
            None
        )
        gizmo.matrix_basis = m.normalized()
        # draw
        gizmo.draw_style = 'BOX'
        gizmo.color = 0.0, 1.0, 0.0
        gizmo.alpha = 0.2
        gizmo.color_highlight = 1.0, 0.5, 1.0
        gizmo.alpha_highlight = 0.2
        # local link
        self.neg_y = gizmo

    def refresh(self, context):
        pass
        # ob = context.object
        # gizmo = self.gizmo
        # gizmo.matrix_basis = Matrix(context.scene.cursor.matrix).normalized()

    @classmethod
    def poll(cls, context):
        return context.object and context.mode == 'EDIT_MESH'


def register():
    register_class(MIRROR_GIZMO_GT_mirror)


def unregister():
    unregister_class(MIRROR_GIZMO_GT_mirror)
