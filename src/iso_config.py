import typing


class IsosurfaceConfig(typing.TypedDict):
    isovalue: int
    color: tuple[float, float, float, float]


HEAD_CONFIG: tuple[IsosurfaceConfig, ...] = (
    {"isovalue": 631, "color": (0.898, 0.7098, 0.631, 0.5)},
    {"isovalue": 996, "color": (0.67, 0.21, 0.21, 0.5)},
    {"isovalue": 1526, "color": (0.898, 0.898, 0.898, 0.6)},
)

FLAME_CONFIG: tuple[IsosurfaceConfig, ...] = (
    {"isovalue": 6501, "color": (0.372116, 0.092816, 0.499053, 0.7)},
    {"isovalue": 33698, "color": (0.828886, 0.262229, 0.430644, 0.7)},
    {"isovalue": 41235, "color": (0.973381, 0.46152, 0.361965, 0.7)},
    {"isovalue": 65000, "color": (0.997341, 0.733545, 0.505167, 0.8)},
)
