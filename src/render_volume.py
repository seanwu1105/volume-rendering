from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonDataModel import vtkPiecewiseFunction
from vtkmodules.vtkIOXML import vtkXMLImageDataReader
from vtkmodules.vtkRenderingCore import (
    vtkColorTransferFunction,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkVolume,
    vtkVolumeProperty,
)
from vtkmodules.vtkRenderingVolume import vtkFixedPointVolumeRayCastMapper


def render_volume(
    filename: str, ctf: vtkColorTransferFunction, opacity_func: vtkPiecewiseFunction
):
    reader = vtkXMLImageDataReader()
    reader.SetFileName(filename)

    # Use CPU rendering for safety. We should use vtkSmartVolumeMapper but it does
    # not work with SetSampleDistance.
    # See https://piazza.com/class/lcp7r42cb4s18t/post/82
    mapper = vtkFixedPointVolumeRayCastMapper()
    mapper.SetInputConnection(reader.GetOutputPort())
    mapper.SetAutoAdjustSampleDistances(False)
    mapper.SetSampleDistance(0.05)

    volume_property = vtkVolumeProperty()
    volume_property.SetColor(ctf)
    volume_property.SetScalarOpacity(opacity_func)
    volume_property.ShadeOn()
    volume_property.SetInterpolationTypeToLinear()

    volume = vtkVolume()
    volume.SetMapper(mapper)
    volume.SetProperty(volume_property)

    renderer = vtkRenderer()
    renderer.AddVolume(volume)
    colors = vtkNamedColors()
    renderer.SetBackground(colors.GetColor3d("Gray"))  # type: ignore
    renderer.ResetCamera()
    renderer.SetUseDepthPeeling(True)
    renderer.SetMaximumNumberOfPeels(100)
    renderer.SetOcclusionRatio(0.1)

    window = vtkRenderWindow()
    window.AddRenderer(renderer)
    window.SetSize(640, 480)
    window.SetAlphaBitPlanes(True)
    window.SetMultiSamples(0)
    window.Render()

    interactor = vtkRenderWindowInteractor()
    interactor.SetRenderWindow(window)

    return interactor
