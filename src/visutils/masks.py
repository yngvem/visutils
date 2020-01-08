import matplotlib.cm as cm
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage.morphology import binary_erosion, generate_binary_structure


def create_outline(mask, width=2, colour=None):
    """Create the outline of the given mask.
    """
    inner = mask.astype(bool)
    structure = generate_binary_structure(inner.ndim, 1).astype(float)
    breakpoint()
    for _ in range(width):
        inner = binary_erosion(inner, structure=structure)

    outline = mask.astype(int) - inner
    outline *= mask
    if colour is not None:
        return apply_colour_to_mask(outline, colour)
    return outline


def apply_colour_to_mask(mask, colour):
    """Set the mask colour equal to a given colour. 
    """
    colour = mcolors.to_rgba(colour)
    colour = np.asarray(colour)
    colour = colour[tuple(np.newaxis for _ in range(mask.ndim))]
    mask = mask[..., np.newaxis]

    return mask*colour
    

def apply_cmap_with_blend(x, cmap, vmin=None, vmax=None, gamma=1):
    """Apply a colour map to an array, using the normalised array values as alpha.
    """
    x = x.astype(float)
    if vmin is None:
        vmin = x.min()
    if vmax is None:
        vmax = x.max()
    x = ((x - vmin)/(vmax - vmin))**gamma
    x = np.minimum(np.maximum(x, 0), 1)
    image = cm.get_cmap(cmap)(x)
    image[..., -1] = x

    return image


def create_legend(colours, labels, ax=None, *args, **kwargs):
    """Create a legend with given colours and labels.

    Additional args and kwargs are passed to matplotlib legend call.
    """
    legend_elements = [
        Line2D(
            [0],
            [0],
            marker='o',
            color='#EEEEEE',
            label=label,
            markerfacecolor=colour,
            markersize=15
        )
        for colour, label in zip(colours, labels)
    ]
    if ax is None:
        ax = plt.gca()

    return ax.legend(handles=legend_elements, *args, **kwargs)

