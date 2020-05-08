import bpy
import os
from .pc_lib import pc_utils

class FILEBROWSER_PT_starter_library_headers(bpy.types.Panel):
    bl_space_type = 'FILE_BROWSER'
    bl_region_type = 'UI'
    bl_label = "Library"
    bl_category = "Attributes"
    bl_options = {'HIDE_HEADER'}

    @classmethod
    def poll(cls, context):
        #Only display when active and File Browser is not open as separate window
        if len(context.area.spaces) > 1:
            pyclone = pc_utils.get_scene_props(context.scene)
            if pyclone.active_library_name == 'Starter Library':
                return True   
        return False

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.scale_y = 1.3
        row.label(text="Starter Library")
        row = layout.row()
        row.scale_y = 1.3
        row.label(text="Library")        

classes = (
    FILEBROWSER_PT_starter_library_headers,
)

register, unregister = bpy.utils.register_classes_factory(classes)                