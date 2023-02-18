from src.camera_settings import add_save_camera_settings_observer, load_camera_settings
from src.parse_args import parse_args
from src.render_isosurfaces import IsosurfaceConfig, render_isosurfaces
from src.vtk_side_effects import import_for_rendering_core

if __name__ == "__main__":
    import_for_rendering_core()
    args = parse_args()

    configs: tuple[IsosurfaceConfig, ...] = (
        {"isovalue": 631, "color": (0.898, 0.7098, 0.631, 0.3)},
        {"isovalue": 1029, "color": (0.67, 0.21, 0.21, 0.3)},
        {"isovalue": 1226, "color": (0.898, 0.898, 0.898, 0.4)},
    )

    interactor = render_isosurfaces(args.input, configs)
    SETTINGS_NAME = "iso_head"
    load_camera_settings(interactor, SETTINGS_NAME)
    add_save_camera_settings_observer(interactor, SETTINGS_NAME)
    interactor.Start()
