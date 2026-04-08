"""Tests that run the example scripts to verify API coverage.

Markers:
  - @pytest.mark.viewer: Viewer examples
  - @pytest.mark.planning: Motion planning examples
  - @pytest.mark.basic: Basic examples (collision, kinematics, scene_graph)
  - @pytest.mark.lowlevel: Low-level API examples
"""

import pytest
import tesseract_planning.examples


# === Viewer Examples ===


@pytest.mark.viewer
def test_shapes_viewer():
    tesseract_planning.examples.shapes_viewer()


@pytest.mark.viewer
def test_material_mesh_viewer():
    tesseract_planning.examples.tesseract_material_mesh_viewer()


@pytest.mark.viewer
@pytest.mark.planning
def test_abb_irb2400_viewer():
    tesseract_planning.examples.abb_irb2400_viewer()


# === High-Level API Examples ===

@pytest.mark.basic
def test_collision_example():
    tesseract_planning.examples.tesseract_collision_example()


@pytest.mark.basic
def test_kinematics_example():
    tesseract_planning.examples.tesseract_kinematics_example()


@pytest.mark.basic
def test_geometry_showcase_example():
    tesseract_planning.examples.geometry_showcase_example()


@pytest.mark.planning
def test_freespace_ompl_example():
    tesseract_planning.examples.freespace_ompl_example()


@pytest.mark.planning
def test_basic_cartesian_example():
    tesseract_planning.examples.basic_cartesian_example()


@pytest.mark.planning
def test_glass_upright_example():
    tesseract_planning.examples.glass_upright_example()


@pytest.mark.planning
def test_pick_and_place_example():
    tesseract_planning.examples.pick_and_place_example()


@pytest.mark.planning
def test_car_seat_example():
    tesseract_planning.examples.car_seat_example()


@pytest.mark.planning
def test_puzzle_piece_auxillary_axes_example():
    tesseract_planning.examples.puzzle_piece_auxillary_axes_example()


@pytest.mark.planning
def test_raster_example():
    tesseract_planning.examples.raster_example()


@pytest.mark.planning
def test_online_planning_example():
    tesseract_planning.examples.online_planning_example()


@pytest.mark.planning
def test_online_planning_sqp_example():
    tesseract_planning.examples.online_planning_sqp_example()


@pytest.mark.planning
def test_freespace_hybrid_example():
    tesseract_planning.examples.freespace_hybrid_example()


@pytest.mark.planning
def test_chain_example():
    tesseract_planning.examples.chain_example()
