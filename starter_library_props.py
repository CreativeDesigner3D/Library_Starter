import bpy
import os
from bpy.types import (
        Operator,
        Panel,
        PropertyGroup,
        UIList,
        )
from bpy.props import (
        BoolProperty,
        FloatProperty,
        IntProperty,
        PointerProperty,
        StringProperty,
        CollectionProperty,
        EnumProperty,
        )

class Starter_Library_Scene_Props(PropertyGroup):
    library_enum: EnumProperty(name="Library Tabs",
                               items=[('OPTION1',"Option 1","Example Enum"),
                                      ('OPTION2',"Option 2","Example Enum"),
                                      ('OPTION3',"Option 3","Example Enum")],
                               default='OPTION1')

    library_bool: BoolProperty(name="Bool")
    library_float: FloatProperty(name="Float")
    library_string: StringProperty(name="String")
    library_int: IntProperty(name="Int")

    def draw_filebrowser_header(self,layout,context):
        row = layout.row()
        row.scale_y = 1.3
        row.label(text="Starter Library")
        row = layout.row()
        row.scale_y = 1.3
        row.label(text="Library")   

    @classmethod
    def register(cls):
        bpy.types.Scene.starter_library = PointerProperty(
            name="Starter Library Props",
            description="Starter Library Props",
            type=cls,
        )
        
    @classmethod
    def unregister(cls):
        del bpy.types.Scene.starter_library

classes = (
    Starter_Library_Scene_Props,
)

register, unregister = bpy.utils.register_classes_factory(classes)        