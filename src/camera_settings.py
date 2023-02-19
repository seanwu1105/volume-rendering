import json
import typing

from vtkmodules.vtkRenderingCore import vtkCamera, vtkRenderWindowInteractor
from vtkmodules.vtkRenderingUI import vtkXRenderWindowInteractor

CAMERA_SETTINGS_FILENAME = "camera_settings.json"


def add_save_camera_settings_observer(interactor: vtkRenderWindowInteractor, name: str):
    def save_camera_settings_observer(obj: vtkXRenderWindowInteractor, _: str):
        key = obj.GetKeySym()
        if key == "c":
            save_camera_settings(
                obj.GetRenderWindow()
                .GetRenderers()
                .GetFirstRenderer()
                .GetActiveCamera(),
                f"{name}_{CAMERA_SETTINGS_FILENAME}",
            )

    interactor.AddObserver("KeyPressEvent", save_camera_settings_observer)  # type: ignore


def save_camera_settings(camera: vtkCamera, filename: str):
    settings: CameraSettings = {
        "position": camera.GetPosition(),
        "focal_point": camera.GetFocalPoint(),
        "view_up": camera.GetViewUp(),
        "clipping_range": camera.GetClippingRange(),
    }
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(settings, f, indent=2)
        f.write("\n")
        print(f"Saved camera settings to {filename}")


def load_camera_settings(interactor: vtkRenderWindowInteractor, name: str):
    _load_camera_settings(
        interactor.GetRenderWindow()
        .GetRenderers()
        .GetFirstRenderer()
        .GetActiveCamera(),
        f"{name}_{CAMERA_SETTINGS_FILENAME}",
    )


def _load_camera_settings(camera: vtkCamera, filename: str):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            settings: CameraSettings = json.load(f)
    except FileNotFoundError:
        print(f"File not found: {filename} (use default camera settings)")
        return
    camera.SetPosition(settings["position"])
    camera.SetFocalPoint(settings["focal_point"])
    camera.SetViewUp(settings["view_up"])
    camera.SetClippingRange(settings["clipping_range"])
    print(f"Loaded camera settings from {filename}")


class CameraSettings(typing.TypedDict):
    position: tuple[float, float, float]
    focal_point: tuple[float, float, float]
    view_up: tuple[float, float, float]
    clipping_range: tuple[float, float]
