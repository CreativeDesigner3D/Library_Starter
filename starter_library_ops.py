import bpy,os,inspect

from bpy.types import (Header, 
                       Menu, 
                       Panel, 
                       Operator,
                       PropertyGroup)

from bpy.props import (StringProperty,
                       BoolProperty,
                       IntProperty,
                       FloatProperty,
                       FloatVectorProperty,
                       PointerProperty,
                       EnumProperty,
                       CollectionProperty)
from . import starter_library_utils
from .pc_lib import pc_utils

class starter_library_OT_activate(Operator):
    bl_idname = "starter_library.activate"
    bl_label = "Activate Library"
    bl_options = {'UNDO'}
    
    library_name: StringProperty(name='Library Name')

    def execute(self, context):
        #Code to initalize library goes here
        #This can be left blank
        print('Activate Starter Library:',self.library_name)
        path = starter_library_utils.get_library_path()
        pc_utils.update_file_browser_path(context,path)
        return {'FINISHED'}

class starter_library_OT_drop(Operator):
    bl_idname = "starter_library.drop"
    bl_label = "Drop File"
    bl_options = {'UNDO'}
    
    filepath: StringProperty(name='Library Name')

    def execute(self, context):
        print('Drop File:',self.filepath)
        #This is called when a file is dropped with your library active
        return {'FINISHED'}

classes = (
    starter_library_OT_activate,
    starter_library_OT_drop,
)

register, unregister = bpy.utils.register_classes_factory(classes)

if __name__ == "__main__":
    register()
