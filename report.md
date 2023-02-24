# Report

See [README.md](./README.md) for details on how to run the application.

## Task 1: Important Isosurfaces

Select the isovalues corresponding to the skin (631), muscle (996), and bone
(1526) of the model.

### Head

#### Isosurface: 631

![head isosurface with isovalue 631](./assets/report/iso-head-631.png)

#### Isosurface: 996

![head isosurface with isovalue 996](./assets/report/iso-head-996.png)

#### Isosurface: 1526

![head isosurface with isovalue 1526](./assets/report/iso-head-1526.png)

#### Combined

![combined head isosurfaces](./assets/report/iso-head-combined.png)

### Flame

Select the isovalues corresponding to:

- environment (6501)
- lowest value of the visible flame (33698)
- mean value of the visible flame (41235)
- highest value of the visible flame (65000)

#### Isosurface: 6501

![flame isosurface with isovalue 6501](./assets/report/iso-flame-6501.png)

#### Isosurface: 33698

![flame isosurface with isovalue 33698](./assets/report/iso-flame-33698.png)

#### Isosurface: 41235

![flame isosurface with isovalue 41235](./assets/report/iso-flame-41235.png)

#### Isosurface: 65000

![flame isosurface with isovalue 65000](./assets/report/iso-flame-65000.png)

#### Combined

![combined flame isosurfaces](./assets/report/iso-flame-combined.png)

## Task 2: Transfer Function Design

### Head

![volume rendering of head 0](./assets/report/dvr-head.png)

![volume rendering of head 1](./assets/report/dvr-head-1.png)

![volume rendering of head 2](./assets/report/dvr-head-2.png)

#### Transfer Function

- Use the previous isovalues to define the value of "peaks".
- Set the opacity of the bone slightly higher than the skin and muscle for
  better visibility.
- Set the width of each peaks to 150 to render the fuzzy edges of each isovalue.

![volume rendering function for head](./assets/report/dvr-head-function.png)

### Flame

![volume rendering of flame 0](./assets/report/dvr-flame.png)

![volume rendering of flame 1](./assets/report/dvr-flame-1.png)

![volume rendering of flame 2](./assets/report/dvr-flame-2.png)

#### Transfer Function

- Use the previous isovalues to define the value of "peaks".
- Set the opacity of the highest value of the visible flame slightly higher than
  other peaks for better visibility.
- Set the width of each peaks to 500 to render the fuzzy edges of each isovalue.

![volume rendering function for flame](./assets/report/dvr-flame-function.png)

#### Strengths and Limitations

The transfer function with multiple peaks is suitable for rendering the model
with different "layers", such as the head model with three tissues. However, it
could not perfectly visualize the flame model, which does not have a clear
boundary between different parts of the model. Widening the peaks and increasing
the number of peaks could be helpful to improve the visualization of the flame
model.

Also, our method choosing the width of the peaks uniformly could be improved.
For instance, the width of the peaks for the muscle tissue in the head model
could be wider than the width of others.

## Task 3: Volume Rendering vs. Isosurfacing

### Head

| Isosurfacing                                                 | Volume Rendering                                          |
| ------------------------------------------------------------ | --------------------------------------------------------- |
| ![isosurface of head](./assets/report/iso-head-combined.png) | ![volume rendering of head](./assets/report/dvr-head.png) |

### Flame

| Isosurfacing                                                   | Volume Rendering                                            |
| -------------------------------------------------------------- | ----------------------------------------------------------- |
| ![isosurface of flame](./assets/report/iso-flame-combined.png) | ![volume rendering of flame](./assets/report/dvr-flame.png) |
