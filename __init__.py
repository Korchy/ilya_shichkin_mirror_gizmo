# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#   https://github.com/Korchy/ilya_shichkin_mirror_gizmo

if "bpy" in locals():
    import importlib
    importlib.reload(mirror_gizmo_ops)
    importlib.reload(mirror_gizmo_panel)
    importlib.reload(mirror_gizmo_gizmo)
else:
    from . import mirror_gizmo_ops
    from . import mirror_gizmo_panel
    from . import mirror_gizmo_gizmo


bl_info = {
    'name': 'Mirror Ggizmo',
    'category': 'All',
    'author': 'Nikita Akimov',
    'version': (1, 0, 3),
    'blender': (3, 1, 0),
    'location': '3D Viewport - Edit mode',
    'doc_url': 'https://github.com/Korchy/ilya_shichkin_mirror_gizmo',
    'tracker_url': 'https://github.com/Korchy/ilya_shichkin_mirror_gizmo',
    'description': 'In mesh Edit Mode quickly create a mirror of selected vertices by gizmo axis around 3D cursor'
}


def register():
    mirror_gizmo_ops.register()
    mirror_gizmo_panel.register()
    mirror_gizmo_gizmo.register()


def unregister():
    mirror_gizmo_gizmo.unregister()
    mirror_gizmo_panel.unregister()
    mirror_gizmo_ops.unregister()


if __name__ == '__main__':
    register()
