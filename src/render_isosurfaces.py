import typing

from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import vtkLookupTable
from vtkmodules.vtkCommonExecutionModel import vtkAlgorithmOutput
from vtkmodules.vtkFiltersCore import vtkContourFilter
from vtkmodules.vtkIOXML import vtkXMLImageDataReader
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkDataSetMapper,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
)


class IsosurfaceConfig(typing.TypedDict):
    isovalue: int
    color: tuple[float, float, float, float]


def render_isosurfaces(file_path: str, configs: typing.Sequence[IsosurfaceConfig]):
    reader = vtkXMLImageDataReader()
    reader.SetFileName(file_path)

    actors = (
        build_isosurface_actor(reader.GetOutputPort(), **config) for config in configs
    )

    renderer = vtkRenderer()
    for actor in actors:
        renderer.AddActor(actor)
    colors = vtkNamedColors()
    renderer.SetBackground(colors.GetColor3d("Gray"))  # type: ignore
    renderer.ResetCamera()

    window = vtkRenderWindow()
    window.AddRenderer(renderer)
    window.SetSize(640, 480)

    interactor = vtkRenderWindowInteractor()
    interactor.SetRenderWindow(window)
    interactor.Initialize()

    return interactor


def build_isosurface_actor(
    reader_output: vtkAlgorithmOutput,
    isovalue: int,
    color: tuple[float, float, float, float],
):
    contour_filter = vtkContourFilter()
    contour_filter.SetValue(0, isovalue)
    contour_filter.SetInputConnection(reader_output)

    lut = vtkLookupTable()
    lut.SetNumberOfTableValues(1)
    lut.SetTableValue(0, color)
    lut.Build()

    mapper = vtkDataSetMapper()
    mapper.SetLookupTable(lut)
    mapper.SetInputConnection(contour_filter.GetOutputPort())

    actor = vtkActor()
    actor.SetMapper(mapper)

    return actor
