# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#   https://github.com/Korchy/ilya_shichkin_mirror_gizmo

import bpy
from bpy.props import IntProperty, EnumProperty
from bpy.types import Operator
from bpy.utils import register_class, unregister_class
from math import radians
from mathutils import Euler


class MIRROR_GIZMO_OT_mirror_gizmo(Operator):
    bl_idname = 'mirror_gizmo.mirror_gizmo'
    bl_label = 'Mirror Gizmo'
    bl_description = 'Mirror Gizmo'
    bl_options = {'INTERNAL'}

    def execute(self, context):
        # show mirror gizmo
        context.window_manager.gizmo_group_type_ensure('mirror_gizmo.mirror')
        # continue modal
        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}

    def modal(self, context, event):
        if event.type == 'LEFTMOUSE' and event.value == 'PRESS':
            # hide gizmo - success
            context.window_manager.gizmo_group_type_unlink_delayed('mirror_gizmo.mirror')
        elif event.type == 'LEFTMOUSE' and event.value == 'RELEASE':
            # finish modal - here because if in 'PRESS' gizmo can't process its operator
            return {'FINISHED'}
        elif event.type in ['ESC', 'RIGHTMOUSE']:
            # hide gizmo - canceled
            context.window_manager.gizmo_group_type_unlink_delayed('mirror_gizmo.mirror')
            return {'CANCELLED'}
        return {'PASS_THROUGH'}

    @classmethod
    def poll(cls, context):
        return context.area.type == 'VIEW_3D' and context.mode == 'EDIT_MESH'


class MIRROR_GIZMO_OT_mirror(Operator):
    bl_idname = 'mirror_gizmo.mirror'
    bl_label = 'Mirror Gizmo'
    bl_description = 'Mirror Gizmo'
    bl_options = {'REGISTER', 'UNDO'}

    angle: IntProperty(
        name='Angle',
        default=45,
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
        bpy.ops.object.mode_set(mode='OBJECT')
        # empty to control mirror angle
        empty = context.blend_data.objects.new(
            name='mirror_empty',
            object_data=None
        )
        empty.empty_display_type = 'ARROWS'
        empty.location = context.scene.cursor.location
        context.scene.collection.objects.link(empty)
        rotation = Euler((
            radians(-self.angle if 'NEG' in self.axis else self.angle) if 'X' in self.axis else 0.0,
            radians(-self.angle if 'NEG' in self.axis else self.angle) if 'Y' in self.axis else 0.0,
            radians(-self.angle if 'NEG' in self.axis else self.angle) if 'Z' in self.axis else 0.0
        ), 'XYZ')
        empty.rotation_euler = rotation
        # mirror modifier
        mirror_modifier = context.object.modifiers.new(
            name="mirror",
            type='MIRROR'
        )
        mirror_modifier.mirror_object = empty
        mirror_modifier.merge_threshold = 0.0005
        mirror_modifier.use_axis = (
            True if 'X' in self.axis else False,
            True if 'Z' in self.axis else False,
            True if 'Y' in self.axis else False
        )
        mirror_modifier.use_bisect_axis = (
            True if 'X' in self.axis else False,
            True if 'Z' in self.axis else False,
            True if 'Y' in self.axis else False
        )
        mirror_modifier.use_bisect_flip_axis = (
            False if 'X_NEG' in self.axis else True,
            False if 'Z_NEG' in self.axis else True,
            False if 'Y_NEG' in self.axis else True
        )
        # apply and clear
        bpy.ops.object.modifier_apply(
            modifier=mirror_modifier.name
        )
        bpy.data.objects.remove(empty, do_unlink=True)
        bpy.ops.object.mode_set(mode='EDIT')
        return {'FINISHED'}

    @classmethod
    def poll(cls, context):
        return context.area.type == 'VIEW_3D' and context.mode == 'EDIT_MESH'


def register():
    register_class(MIRROR_GIZMO_OT_mirror_gizmo)
    register_class(MIRROR_GIZMO_OT_mirror)


def unregister():
    unregister_class(MIRROR_GIZMO_OT_mirror)
    unregister_class(MIRROR_GIZMO_OT_mirror_gizmo)
