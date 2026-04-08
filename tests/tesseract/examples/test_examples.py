"""Tests that run the example scripts to verify API coverage.

Markers:
  - @pytest.mark.viewer: Viewer examples
  - @pytest.mark.planning: Motion planning examples
  - @pytest.mark.basic: Basic examples (collision, kinematics, scene_graph)
  - : Low-level API examples
"""

import pytest
import tesseract.examples


# === Viewer Examples ===


@pytest.mark.viewer
def test_shapes_viewer():
    tesseract.examples.shapes_viewer()


@pytest.mark.viewer
def test_material_mesh_viewer():
    tesseract.examples.tesseract_material_mesh_viewer()


@pytest.mark.viewer
@pytest.mark.planning
def test_abb_irb2400_viewer():
    tesseract.examples.abb_irb2400_viewer()

# === Low-Level API Examples ===


@pytest.mark.basic
def test_collision_example():
    tesseract.examples.tesseract_collision_example()


@pytest.mark.basic
def test_kinematics_example():
    tesseract.examples.tesseract_kinematics_example()


@pytest.mark.basic
def test_scene_graph_example():
    tesseract.examples.scene_graph_example()


@pytest.mark.planning
def test_freespace_ompl_example():
    tesseract.examples.freespace_ompl_example()


@pytest.mark.planning
def test_basic_cartesian_example():
    tesseract.examples.basic_cartesian_example()


@pytest.mark.planning
def test_glass_upright_example():
    tesseract.examples.glass_upright_example()


@pytest.mark.planning
def test_puzzle_piece_example():
    tesseract.examples.puzzle_piece_example()


@pytest.mark.planning
def test_pick_and_place_example():
    tesseract.examples.pick_and_place_example()



@pytest.mark.planning
def test_car_seat_example():
    tesseract.examples.car_seat_example()


@pytest.mark.planning
def test_puzzle_piece_auxillary_axes_example():
    tesseract.examples.puzzle_piece_auxillary_axes_example()


@pytest.mark.planning
def test_pythonic_example():
    tesseract.examples.pythonic_example()


@pytest.mark.planning
def test_planning_composer_example():
    tesseract.examples.tesseract_planning_composer_example()


@pytest.mark.planning
def test_planning_example():
    tesseract.examples.tesseract_planning_example()


@pytest.mark.planning
def test_trajopt_ifopt_example():
    tesseract.examples.tesseract_planning_trajopt_ifopt_example()
