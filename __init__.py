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
    #Get PyClone Window Manager Properties
    pyclone = pc_utils.get_wm_props(bpy.context.window_manager)
    #Check if you library is already registered
    if "Starter Library" not in pyclone.libraries:
        #Add Library with Activate ID, Drop ID, and Icon
        library = pyclone.add_library(name="Starter Library",
                                      activate_id='starter_library.activate',
                                      drop_id='starter_library.drop',
                                      icon='ASSET_MANAGER')

#Standard register/unregister Function for Blender Add-ons
def register():
    starter_library_ops.register()
    starter_library_props.register()
    starter_library_ui.register()

    load_library_on_file_load()
    bpy.app.handlers.load_post.append(load_library_on_file_load)

def unregister():
    starter_library_ops.unregister()
    starter_library_props.unregister()
    starter_library_ui.unregister()

    bpy.app.handlers.load_post.remove(load_library_on_file_load)  

    pyclone = pc_utils.get_wm_props(bpy.context.window_manager)
    pyclone.remove_library("Starter Library")

