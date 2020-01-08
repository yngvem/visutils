import matplotlib.pyplot as plt


@contextmanager
@wraps(plt.figure)
def notebook_figure(*args, **kwargs):
    """Create a figure and plot inside it. Then once context is finished the figure is shown and closed."""
    fig = plt.figure(*args, **kwargs)
    yield fig
    plt.show()
    plt.close(fig)
