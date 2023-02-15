# Assignment 3: Volume Rendering

## Objective

The topic of this assignment is the visualization of 3D scalar fields through
(direct) volume rendering. You will experiment with transfer function design and
revisit some of the tasks of the second assignment to compare the effectiveness
of isosurfacing and volume rendering in two application scenarios. Specifically,
you will visualize a medical dataset (similar to the CT volume used in the
previous assignment) and a computational fluid dynamics (CFD) simulation of
turbulent combustion.

## Background

Selecting an effective transfer function is key to achieving good results with
volume rendering. We will see in class that a good transfer function should
reveal boundaries present in the volume when such boundaries exist. When clear
boundaries are not present, the transfer function should be designed to reveal
fuzzy geometric structures in the data. In this assignment, you will be working
with two datasets that illustrate these two scenarios: the CT dataset contains
boundaries corresponding to the interface between different tissue types, while
the CFD dataset describes [vorticity](https://en.wikipedia.org/wiki/Vorticity)
in a turbulent combustion simulation and is globally smooth. The project asks
you to identify remarkable (iso)values in each dataset, which you will use as
reference points to create your transfer functions. The third part of the
project invites you to compare the pros and cons of volume rendering and
isosurfacing in the context of these two datasets.

# Tasks

## Task 1: Important Isosurfaces

Your first task consists in determining for each dataset a set of isovalues that
capture remarkable (salient) structures in the considered field. To do so, you
will use the code you wrote for
[the second assignment](https://github.com/seanwu1105/isosurfaces-color-mapping)
to identify important isosurfaces. In the case of the head dataset, salient
isosurfaces capture boundaries corresponding to the air, skin, muscles, skull,
and teeth. In the case of the combustion dataset, you will look for isosurfaces
that reveal the sheet and tubular structures found in the flame. Bear in mind
that isosurfaces might poorly capture fuzzy structures. Using different
opacities for different isosurfaces, create for each dataset a visualization
showing all isosurfaces simultaneously.

### Deliverables

Create two executables for this task: `iso_head.py` and `iso_flame.py` that each
contain the (hardcoded) information needed to visualize the salient isosurfaces
of the corresponding dataset using transparency. In both cases, your executable
must obtain the file name to visualize from the command line.

```sh
python iso_head.py -i [--input] <head.vti>
```

```sh
python iso_flame.py -i [--input] <flame.vti>
```

### Report

Describe how you selected the isovalues for each dataset in the report. Include
pictures showing each isosurface individually and other images showing _all
isosurfaces combined_ using transparency. Make sure to use the **same camera
setting** across all images corresponding to the same dataset. To that end,
refer to
[the code sample](https://www.cs.purdue.edu/homes/cs530/code/interactor/interactor_demo.py)
that showed you how to print out the current camera setting during an
interactive session and save the current frame to a file. Once you identify a
suitable camera position, hard-code the corresponding parameters in your
program.

## Task 2: Transfer Function Design

Now that you have found good isovalues, you will design a transfer function for
each dataset using those values. For that, create a
[`vtkVolumeProperty`](https://vtk.org/doc/nightly/html/classvtkVolumeProperty.html)
by following the example provided in
[`Examples/VolumeRendering/Python/SimpleRayCast.py`](https://kitware.github.io/vtk-examples/site/Python/VolumeRendering/SimpleRayCast/)
to define both color and opacity transfer functions that emphasize the selected
isovalues. You are already familiar with
[`vtkColorTransferFunctions`](https://vtk.org/doc/nightly/html/classvtkColorTransferFunction.html)
from previous assignments. The opacity transfer function is defined through a
[`vtkPiecewiseFunction`](https://vtk.org/doc/nightly/html/classvtkPiecewiseFunction.html).
Your objective in designing the opacity transfer function is to reveal as much
as possible of the internal structures of each dataset. The volume rendering
itself will be performed by raycasting using a
[`vtkSmartVolumeMapper`](https://vtk.org/doc/nightly/html/classvtkSmartVolumeMapper.html).
Note that this implementation will automatically determine the hardware
resources available and perform GPU-based raycasting whenever possible. Select
the compositing blend mode of `vtkSmartVolumeMapper` for _value compositing_
along each ray. Your implementation should produce high-quality renderings by
combining trilinear interpolation and small sampling distance along each ray:
you will select `SetInterpolationTypeToLinear()` in the API of
`vtkVolumeProperty` and manipulate the discretization along each ray via
`SetSampleDistance()`. You will need to experiment with different values of the
sampling distance to determine the precision necessary to obtain good results.
Good results, in particular, should not exhibit aliasing artifacts such as
[moiré effect](https://en.wikipedia.org/wiki/Moir%C3%A9_pattern). Note that an
appropriate sampling distance value depends on the smoothness of the data and
the properties of your transfer function. Finally, you should activate the
shading option (via `ShadeOn()` in `vtkVolumeProperty()`) in your rendering to
further improve the visual quality of your results.

### Deliverables

Create two executables `dvr_head.py` and ``dvr_flame.py` that contain the
information necessary to create high-quality renderings of the corresponding
dataset. In particular, the opacity and color transfer functions must be
hard-coded in these programs. As for the first task, your executables must
obtain the name of the data file from the command line.

```sh
python dvr_head.py -i[--input] <head.vti>
```

```sh
python dvr_flame.py -i[--input] <flame.vti>
```

### Report

Provide a detailed description (including diagrams) of the various transfer
functions you created, along with a justification of the choices made. What
method did you use to create each opacity transfer function? What do you
consider to be the strengths and limitations of your solutions? Include in the
report several images for each dataset that highlight the effectiveness of your
transfer function and the quality of your volume rendering parameters.

## Task 3: Volume Rendering vs. Isosurfacing

Provide for each dataset a side-by-side comparison between the results obtained
for isosurfacing (Task 1) and volume rendering (Task 2). Make sure to **use the
same camera settings** for both techniques to facilitate their comparison. No
additional code should be written for this task: use the executables created for
the previous tasks to create the images included in the report.

### Report

Comment on the differences between the two techniques. Illustrate your
argumentation by zooming in on particular features of each volume. For each
dataset, which technique do you find most effective? Why? Be specific.

## Summary Analysis

Include your critical assessment of volume rendering in the report: What are
this technique's pros and cons? Refer to the tasks of this project to justify
your opinion.

## Data Sets

You will be visualizing two datasets for this assignment. The first one is a
head CT scan dataset similar to what you used for Project 2. Here, the data
corresponds to a male subject, part of the
[Visible Human Project](https://www.nlm.nih.gov/research/visible/visible_human.html)
(National Library of Medicine). The second dataset corresponds to a
computational fluid dynamics simulation of a turbulent combustion. In this case,
the provided scalar volume corresponds to the magnitude of the
[vorticity](https://en.wikipedia.org/wiki/Vorticity) field. This quantity is
derived from the flow velocity (speed) and can be used to identify
[vortices](https://en.wikipedia.org/wiki/Vortex) in numerical datasets.

Note that both datasets have been smoothed (low-pass filtered) to facilitate
their visualization (e.g., reduce aliasing issues).

The datasets are available
[online](https://www.cs.purdue.edu/homes/cs530/projects/project3.html). All
datasets are of type `vtkImageData`.
