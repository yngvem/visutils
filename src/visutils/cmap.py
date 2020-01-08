import matplotlib.colors as mpl_colors
import numpy as np
from colorspacious import cspace_convert, deltaE

from .utils import UniformResampler


def _colour_distance(colour_1, colour_2, input_space='sRGB1', uniform_space='CAM02-UCS'):
    distances = [deltaE(c1, c2, input_space, uniform_space) for c1, c2 in zip(colour_1, colour_2)]
    return np.array(distances)



def normalise_cmap(
    cmap,
    cmap_samples=101,
    resampling_rate=10,
    spline_degree=1,
    smoothing_factor=0,
    uniform_space="CAM02-UCS",
):
    """Reinterpolate colormap so that it is perceptually uniform.

    Arguments
    ---------
    cmap_samples: int
        Number of linearly spaced points from the colormap to sample.
        Used for spline interpolation
    resampling_rate: Numeric
        The uniform resampling will contain ``resampling_rate*cmap_samples``
        perceptually equispaced colours.
    spline_degree: int
        Which kind of spline interpolation to use when resampling
    uniform_space:
        Colorspace accepted by the ``cpsace_convert`` function in ``colorspacious``.
        This is the colourspace that the uniform interpolation will happen in.
    """
    rgb_original = cmap(np.linspace(0, 1, cmap_samples))[:, :-1]
    # ciecam_original = cspace_convert(rgb_original, "sRGB1", "CAM02-UCS")
    rgb_resampled = UniformResampler(
        resampling_rate=resampling_rate,
        spline_degree=spline_degree,
        smoothing_factor=smoothing_factor,
        distance_function=_colour_distance
    ).fit_predict(rgb_original)
    # rgb_resampled = cspace_convert(ciecam_resampled, "CAM02-UCS", "sRGB1")
    rgb_resampled[rgb_resampled < 0] = 0
    rgb_resampled[rgb_resampled > 1] = 1
    breakpoint()
    return mpl_colors.LinearSegmentedColormap.from_list(cmap.name, rgb_resampled, resampling_rate*cmap_samples)
