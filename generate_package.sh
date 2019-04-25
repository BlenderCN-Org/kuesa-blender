#!/bin/sh

BASE_PWD=$(dirname "$(readlink -f "$0")")
KUESA_TOOLS_DIR=$BASE_PWD/addons/
KUESA_EXPORTER_DIR_2_79=$BASE_PWD/addons/kuesa_exporter/2.79/glTF-Blender-Exporter/scripts/addons/
KUESA_EXPORTER_DIR_2_80=$BASE_PWD/addons/kuesa_exporter/2.80/glTF-Blender-IO-master/addons/
DATE_STR=$(date "+%d_%m_%y")
GIT_VERSION=$(git describe --tags)

# Create zip file for Kuesa Tools
cd "$KUESA_TOOLS_DIR" && zip -r "$BASE_PWD/kuesa_${DATE_STR}_${GIT_VERSION}.zip" kuesa

# Create zip file for Kuesa Exporter 2.79
cd "$KUESA_EXPORTER_DIR_2_79" && zip -r "$BASE_PWD/kuesa_exporter_2.79_${DATE_STR}_${GIT_VERSION}.zip" io_scene_gltf2

# Create zip file for Kuesa Exporter 2.80
cd "$KUESA_EXPORTER_DIR_2_80" && zip -r "$BASE_PWD/kuesa_exporter_2.80_${DATE_STR}_${GIT_VERSION}.zip" io_scene_gltf2
