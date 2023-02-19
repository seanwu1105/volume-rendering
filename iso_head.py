from src.camera_settings import add_save_camera_settings_observer, load_camera_settings
from src.iso_config import HEAD_CONFIG
from src.parse_args import parse_args
from src.render_isosurfaces import render_isosurfaces
from src.vtk_side_effects import import_for_rendering_core


def main():
    import_for_rendering_core()
    args = parse_args()

    interactor = render_isosurfaces(args.input, HEAD_CONFIG)
    settings_name = "iso_head"
    load_camera_settings(interactor, settings_name)
    add_save_camera_settings_observer(interactor, settings_name)
    interactor.Start()


if __name__ == "__main__":
    main()
