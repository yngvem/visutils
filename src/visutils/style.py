import cycler
import matplotlib.cm as cm
import matplotlib.pyplot as plt


cmap = cm.inferno

palette = ["#D87F6B", "#B56C7D", "#7E6480", "#475B6D", "#224C4C"]

_palette_cycle = [palette[i] for i in [0, 4, 1, 3, 2] * 4]

linestyle = ["-", "--", ":", "-."]
_linestyle_cycle = linestyle*5

tex_preamble = r"""
\usepackage[T1]{fontenc}

\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{mathtools}
\usepackage{bm}
\usepackage{stmaryrd}
\usepackage{dsfont}
"""[1:]


def set_plot_params(use_tex=False, family="Sans-serif", subplot_margins=0.05):
    # Fonts
    plt.rcParams["font.family"] = family
    plt.rcParams["font.sans-serif"] = ["PT Sans"]
    plt.rcParams["font.serif"] = ["Computer Modern"]

    # LaTeX
    plt.rcParams["text.usetex"] = use_tex
    plt.rcParams["text.latex.preamble"] = tex_preamble

    # Figure
    plt.rcParams["figure.figsize"] = [4.71, 4.71 / 1.6]
    plt.rcParams["figure.subplot.left"] = 0.13
    plt.rcParams["figure.subplot.right"] = 0.93
    plt.rcParams["figure.subplot.bottom"] = 0.15
    plt.rcParams["figure.subplot.top"] = 0.9
    plt.rcParams["figure.subplot.wspace"] = subplot_margins
    plt.rcParams["figure.subplot.hspace"] = subplot_margins

    # Axes
    plt.rcParams["axes.titleweight"] = "bold"
    plt.rcParams["axes.labelweight"] = "bold"
    plt.rcParams["axes.xmargin"] = 0
    plt.rcParams["axes.ymargin"] = 0.05
    plt.rcParams["axes.prop_cycle"] = cycler.cycler(color=_palette_cycle, linestyle=_linestyle_cycle)
    plt.rcParams["axes.facecolor"] = "#e5e5f0"
    plt.rcParams["axes.grid"] = True
    plt.rcParams["axes.linewidth"] = 0

    # Grids
    plt.rcParams["grid.color"] = "#FFFFFF"
    plt.rcParams["grid.linestyle"] = '-'
    plt.rcParams["grid.linewidth"] = 1
    plt.rcParams["grid.alpha"] = 1

    plt.rcParams["lines.linewidth"] = 1.5

    plt.rcParams["boxplot.patchartist"] = True
    plt.rcParams["boxplot.whiskerprops.color"] = "C4"
    plt.rcParams["boxplot.capprops.color"] = "C4"
    plt.rcParams["boxplot.boxprops.color"] = "C4"
    plt.rcParams["boxplot.flierprops.color"] = "C4"

    # Boxplots
    #boxplot.notch       : False
    #boxplot.vertical    : True
    #boxplot.whiskers    : 1.5
    #boxplot.bootstrap   : None
    #boxplot.patchartist : False
    #boxplot.showmeans   : False
    #boxplot.showcaps    : True
    #boxplot.showbox     : True
    #boxplot.showfliers  : True
    #boxplot.meanline    : False

    #boxplot.flierprops.color           : black
    #boxplot.flierprops.marker          : o
    #boxplot.flierprops.markerfacecolor : none
    #boxplot.flierprops.markeredgecolor : black
    #boxplot.flierprops.markeredgewidth : 1.0
    #boxplot.flierprops.markersize      : 6
    #boxplot.flierprops.linestyle       : none
    #boxplot.flierprops.linewidth       : 1.0

    #boxplot.boxprops.color     : black
    #boxplot.boxprops.linewidth : 1.0
    #boxplot.boxprops.linestyle : -

    #boxplot.whiskerprops.color     : black
    #boxplot.whiskerprops.linewidth : 1.0
    #boxplot.whiskerprops.linestyle : -

    #boxplot.capprops.color     : black
    #boxplot.capprops.linewidth : 1.0
    #boxplot.capprops.linestyle : -

    #boxplot.medianprops.color     : C1
    #boxplot.medianprops.linewidth : 1.0
    #boxplot.medianprops.linestyle : -

    #boxplot.meanprops.color           : C2
    #boxplot.meanprops.marker          : ^
    #boxplot.meanprops.markerfacecolor : C2
    #boxplot.meanprops.markeredgecolor : C2
    #boxplot.meanprops.markersize      :  6
    #boxplot.meanprops.linestyle       : --
    #boxplot.meanprops.linewidth       : 1.0
