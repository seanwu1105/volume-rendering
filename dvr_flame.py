from src.camera_settings import add_save_camera_settings_observer, load_camera_settings
from src.iso_config import FLAME_CONFIG
from src.parse_args import parse_args
from src.render_volume import (
    get_ctf_from_config,
    get_opacity_func_from_config,
    render_volume,
)
from src.vtk_side_effects import import_for_rendering_core, import_for_rendering_volume


def main():
    import_for_rendering_core()
    import_for_rendering_volume()
    args = parse_args()

    ctf = get_ctf_from_config(FLAME_CONFIG)

    opacity_func = get_opacity_func_from_config(FLAME_CONFIG, width=250)

    interactor = render_volume(args.input, ctf, opacity_func)
    settings_name = "dvr_flame"
    load_camera_settings(interactor, settings_name)
    add_save_camera_settings_observer(interactor, settings_name)
    interactor.Start()


if __name__ == "__main__":
    main()
