import bpy
from .pc_lib import pc_utils
from . import starter_library_ops
from . import starter_library_props
from . import starter_library_ui
from bpy.app.handlers import persistent

#Standard bl_info for Blender Add-ons
bl_info = {
    "name": "Starter Library",
    "author": "Andrew Peel",
    "version": (0, 0, 1),
    "blender": (2, 80, 0),
    "location": "Asset Library",
    "description": "This is a starting point for pyclone libraries",
    "warning": "",
    "wiki_url": "",
    "category": "Asset Library",
}

@persistent
def load_library_on_file_load(scene=None):
    pc_utils.register_library(name="Starter Library",
                              activate_id='starter_library.activate',
                              drop_id='starter_library.drop',
                              icon='ASSET_MANAGER')

#Standard register/unregister Function for Blender Add-ons
def register():
    starter_library_ops.register()
    starter_library_props.register()
    starter_library_ui.register()

    bpy.app.handlers.load_post.append(load_library_on_file_load)

def unregister():
    starter_library_ops.unregister()
    starter_library_props.unregister()
    starter_library_ui.unregister()

    bpy.app.handlers.load_post.remove(load_library_on_file_load)  

    pc_utils.unregister_library("Starter Library")

