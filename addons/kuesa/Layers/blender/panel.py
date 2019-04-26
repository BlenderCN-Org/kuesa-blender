# panel.pri
#
# This file is part of Kuesa.
#
# Copyright (C) 2018 Klarälvdalens Datakonsult AB, a KDAB Group company, info@kdab.com
# Author: Mike Krus <mike.krus@kdab.com>
#
# Licensees holding valid proprietary KDAB Kuesa licenses may use this file in
# accordance with the Kuesa Enterprise License Agreement provided with the Software in the
# LICENSE.KUESA.ENTERPRISE file.
#
# Contact info@kdab.com if any conditions of this licensing are not clear to you.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import bpy
from .properties import KuesaLayersListItem
# Blender panels for Layers


class KuesaLayersList(bpy.types.UIList):

    STATE_ICONS = {
        KuesaLayersListItem.STATE_OFF: "PROP_OFF",
        KuesaLayersListItem.STATE_MID: "PROP_CON",
        KuesaLayersListItem.STATE_ON:  "PROP_ON"
    }

    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        remove_icon = "ZOOMOUT" if bpy.app.version < (2,80) else "REMOVE"
        add_icon = "ZOOMIN" if bpy.app.version < (2,80) else "ADD"
        select_icon = "HAND" if bpy.app.version < (2,80) else "RESTRICT_SELECT_OFF"
        layout.label(text=item.name)
        row = layout.row(align=True)
        row.label(text="", icon=self.STATE_ICONS[item.state])
        op_remove = row.operator("kuesa_layers.item_remove", icon=remove_icon, text="")
        op_remove.index = index
        op_add = row.operator("kuesa_layers.item_add", icon=add_icon, text="")
        op_add.index = index
        op_select = row.operator("kuesa_layers.item_select", icon=select_icon, text="")
        op_select.index = index


class KuesaLayerManager(bpy.types.Panel):

    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS" if bpy.app.version < (2, 80) else 'UI' # tools section
    lb_context = "objectmode" # object mode only
    bl_category = "Kuesa" # 'Kuesa' tab
    bl_label = "Kuesa Layers"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        refresh_icon = "INFO" if bpy.app.version < (2,80) else "FILE_REFRESH"
        new_icon = "PARTICLES" if bpy.app.version < (2,80) else "PLUS"
        edit_icon = "LINE_DATA" if bpy.app.version < (2,80) else "GREASEPENCIL"
        layout = self.layout
        row = layout.row(align=True)
        row.operator("kuesa_layers.refresh", text="Refresh", icon=refresh_icon)
        row = layout.row(align=True)
        row.template_list("KuesaLayersList", "", context.scene.kuesa_layers, "layer_names_list", context.scene.kuesa_layers, "layer_index")
        row = layout.row(align=True)
        col = row.column(align=True)
        col.prop(context.scene.kuesa_layers, "current_layer_name", text="")
        row_ = col.row(align=True)
        row_.operator("kuesa_layers.new_layer", text="New", icon=new_icon)
        row_.operator("kuesa_layers.rename_layer", text="Rename", icon=edit_icon)
