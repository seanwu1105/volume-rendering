from src.parse_args import parse_args
from src.render_isosurfaces import IsosurfaceConfig, render_isosurfaces
from src.vtk_side_effects import import_for_rendering_core

if __name__ == "__main__":
    import_for_rendering_core()
    args = parse_args()

    configs: tuple[IsosurfaceConfig, ...] = (
        {"isovalue": 6500, "color": (0.372116, 0.092816, 0.499053, 0.8)},
        {"isovalue": 30000, "color": (0.828886, 0.262229, 0.430644, 0.8)},
        {"isovalue": 65000, "color": (0.997341, 0.733545, 0.505167, 0.7)},
    )

    render_isosurfaces(args.input, configs).Start()
