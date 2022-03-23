# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#   https://github.com/Korchy/ilya_shichkin_mirror_gizmo

import bpy
from bpy.props import BoolProperty, CollectionProperty, IntProperty, StringProperty
from bpy.types import PropertyGroup, Scene, WindowManager
from bpy.utils import register_class, unregister_class
from .vse_comb import VSECombinator


class VSE_COMB_project_dir(PropertyGroup):

    name: StringProperty(
        default=''
    )


class VSE_COMB_project_item(PropertyGroup):

    name: StringProperty(
        default=''
    )


def register():
    # project path
    Scene.vse_comb_project_path = StringProperty(
        name='Project Path',
        subtype='DIR_PATH',
        update=lambda self, context: VSECombinator.load_project(
            context=context,
            scene=self
        ),
        default=bpy.context.preferences.addons[__package__].preferences.projects_base_path
        # default='i:/dev/blender/_zakaz/Victor_Vangeli/vse_combinator/_all/vse_projects/swords/'
    )
    # project dirs
    register_class(VSE_COMB_project_dir)
    WindowManager.vse_comb_project = CollectionProperty(type=VSE_COMB_project_dir)
    WindowManager.vse_comb_project_active_dir = IntProperty(
        name='active project directory',
        default=-1
    )
    # project items
    register_class(VSE_COMB_project_item)
    WindowManager.vse_comb_project_items = CollectionProperty(type=VSE_COMB_project_item)
    WindowManager.vse_comb_project_active_item = IntProperty(
        name='active project item',
        default=-1
    )
    # project description
    Scene.vse_comb_project_desc = StringProperty(
        name='Project Description',
        default=''
    )
    # project image
    Scene.vse_comb_project_image = StringProperty(
        name='Project Image',
        default=''
    )
    # option for test with render
    WindowManager.vse_comb_test_with_render = BoolProperty(
        name='Test With Render',
        default=False
    )


def unregister():
    # option for test with render
    del WindowManager.vse_comb_test_with_render
    # project image
    del Scene.vse_comb_project_image
    # project description
    del Scene.vse_comb_project_desc
    # project items
    del WindowManager.vse_comb_project_active_item
    del WindowManager.vse_comb_project_items
    unregister_class(VSE_COMB_project_item)
    # project dirs
    del WindowManager.vse_comb_project_active_dir
    del WindowManager.vse_comb_project
    unregister_class(VSE_COMB_project_dir)
    # project path
    del Scene.vse_comb_project_path
