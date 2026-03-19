# API Reference

Auto-generated API documentation from docstrings.

## Modules Overview

### High-Level API

| Module | Description |
|--------|-------------|
| [`tesseract.planning`](planning.md) | Robot, Planner, Composer classes |

### Core Modules

| Module | Description |
|--------|-------------|
| [`tesseract.common`](tesseract_common.md) | Common types (Isometry3d, etc.) |
| [`tesseract.geometry`](tesseract_geometry.md) | Geometric primitives |
| [`tesseract.scene_graph`](tesseract_scene_graph.md) | Links, joints, scene graph |
| [`tesseract.environment`](tesseract_environment.md) | Environment, commands |
| [`tesseract.collision`](tesseract_collision.md) | Collision managers, contacts |
| [`tesseract.kinematics`](tesseract_kinematics.md) | Kinematic groups, solvers |

### Planning Modules

| Module | Description |
|--------|-------------|
| [`tesseract.command_language`](tesseract_command_language.md) | Waypoints, instructions |
| [`tesseract.motion_planners`](tesseract_motion_planners.md) | Base planner types |
| [`tesseract.motion_planners_ompl`](tesseract_motion_planners_ompl.md) | OMPL planner |
| [`tesseract.motion_planners_trajopt`](tesseract_motion_planners_trajopt.md) | TrajOpt planner |
| [`tesseract.motion_planners_descartes`](tesseract_motion_planners_descartes.md) | Descartes planner |
| [`tesseract.motion_planners_simple`](tesseract_motion_planners_simple.md) | Simple interpolation |
| [`tesseract.task_composer`](tesseract_task_composer.md) | Task composition |

### Low-Level SQP Modules

| Module | Description |
|--------|-------------|
| [`tesseract.trajopt_ifopt`](trajopt_ifopt.md) | Variables, constraints, costs (Var, Node, collision, Cartesian) |
| [`tesseract.trajopt_sqp`](trajopt_sqp.md) | SQP solver (TrustRegionSQPSolver, OSQP) |

## Import Patterns

### High-Level (Recommended)

```python
from tesseract.planning import Robot, Planner, Composer

robot = Robot.from_tesseract_support("abb_irb2400")
planner = Planner(robot)
```

### Direct Module Access

```python
from tesseract.environment import Environment
from tesseract.scene_graph import Link, Joint
from tesseract.geometry import Box, Sphere
```

### SQP API

```python
from tesseract.trajopt_ifopt import Bounds, CartPosConstraint, createNodesVariables
from tesseract.trajopt_sqp import TrustRegionSQPSolver, OSQPEigenSolver
```

## Type Conventions

| C++ Type | Python Type |
|----------|-------------|
| `Eigen::Isometry3d` | `tesseract_common.Isometry3d` |
| `Eigen::VectorXd` | `numpy.ndarray` |
| `Eigen::MatrixXd` | `numpy.ndarray` |
| `std::vector<std::string>` | `list[str]` |
| `std::shared_ptr<T>` | Python object (ref counted) |
| `std::optional<T>` | `T` or `None` |

## Memory Management

Objects are reference-counted via nanobind/pybind. Generally:

- Objects returned by functions are owned by Python
- Objects stored in containers maintain references
- No manual memory management needed

!!! warning "Vector Members"
    C++ `std::vector` members return copies. Use explicit methods:

    ```python
    # Wrong (silent no-op)
    link.visual.append(visual)

    # Correct
    link.addVisual(visual)
    ```
