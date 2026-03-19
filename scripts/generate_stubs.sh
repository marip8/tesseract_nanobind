#!/bin/bash
# Generate .pyi stub files from nanobind modules
#
# Usage:
#   ./scripts/generate_stubs.sh          # Generate stubs to src/
#   ./scripts/generate_stubs.sh --check  # Verify stubs are up to date

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
SRC_DIR="$PROJECT_ROOT/src/tesseract"

# Module name -> subdir mapping
# Format: "full.module.name:subdir"
MODULES=(
    "tesseract.collision._tesseract_collision:collision"
    "tesseract.command_language._tesseract_command_language:command_language"
    "tesseract.common._tesseract_common:common"
    "tesseract.environment._tesseract_environment:environment"
    "tesseract.geometry._tesseract_geometry:geometry"
    "tesseract.kinematics._tesseract_kinematics:kinematics"
    "tesseract.motion_planners._tesseract_motion_planners:motion_planners"
    "tesseract.motion_planners_descartes._tesseract_motion_planners_descartes:motion_planners_descartes"
    "tesseract.motion_planners_ompl._tesseract_motion_planners_ompl:motion_planners_ompl"
    "tesseract.motion_planners_simple._tesseract_motion_planners_simple:motion_planners_simple"
    "tesseract.motion_planners_trajopt._tesseract_motion_planners_trajopt:motion_planners_trajopt"
    "tesseract.motion_planners_trajopt_ifopt._tesseract_motion_planners_trajopt_ifopt:motion_planners_trajopt_ifopt"
    "tesseract.scene_graph._tesseract_scene_graph:scene_graph"
    "tesseract.srdf._tesseract_srdf:srdf"
    "tesseract.state_solver._tesseract_state_solver:state_solver"
    "tesseract.task_composer._tesseract_task_composer:task_composer"
    "tesseract.time_parameterization._tesseract_time_parameterization:time_parameterization"
    "tesseract.urdf._tesseract_urdf:urdf"
    "tesseract.trajopt_ifopt._trajopt_ifopt:trajopt_ifopt"
    "tesseract.trajopt_sqp._trajopt_sqp:trajopt_sqp"
)

# Pattern file for type cleanup (if exists)
PATTERN_FILE="$PROJECT_ROOT/stubs/patterns.txt"
PATTERN_ARG=""
if [ -f "$PATTERN_FILE" ]; then
    PATTERN_ARG="-p $PATTERN_FILE"
fi

echo "Generating stubs for ${#MODULES[@]} modules..."

# Generate each module to its correct subdirectory
for entry in "${MODULES[@]}"; do
    MODULE="${entry%%:*}"
    SUBDIR="${entry##*:}"
    STUB_NAME="${MODULE##*.}"  # e.g., _tesseract_kinematics
    OUTPUT_DIR="$SRC_DIR/$SUBDIR"
    OUTPUT_FILE="$OUTPUT_DIR/${STUB_NAME}.pyi"

    echo "  $MODULE -> $SUBDIR/"

    TRAJOPT_LOG_THRESH=ERROR python -m nanobind.stubgen \
        -m "$MODULE" \
        $PATTERN_ARG \
        -o "$OUTPUT_FILE" \
        -q 2>&1 | grep -v "^You can set logging" || true
done

# Create py.typed marker
touch "$SRC_DIR/py.typed"

echo ""
echo "Done. Generated ${#MODULES[@]} stub files."
echo ""
echo "Generated files:"
find "$SRC_DIR" -name "*.pyi" -type f 2>/dev/null | sort | head -25
