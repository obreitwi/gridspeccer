#!/usr/bin/env python2
# encoding: utf-8

import matplotlib as mpl
import matplotlib.image as mpimg
from matplotlib import gridspec as gs
from matplotlib import collections as coll
import pylab as p
import copy
import numpy as np
from scipy.misc import imresize

from . import core
from . import aux
from .core import log


def get_gridspec():
    """
        Return dict: plot -> gridspec
    """
    # TODO: Adjust positioning
    gs_main = gs.GridSpec(1, 1, hspace=0.01,
                          left=0.06, right=0.95, top=.98, bottom=0.01)
    gs_top = gs.GridSpecFromSubplotSpec(2, 1, gs_main[0, 0], wspace=0.2,
                                        height_ratios=[1., 1.])

    return {
        # these are needed for proper labelling
        # core.make_axes takes care of them

        "mnistTsne": gs_top[0, 0],
        "fashionTsne": gs_top[1, 0]
    }


def adjust_axes(axes):
    """
        Settings for all plots.
    """
    # TODO: Uncomment & decide for each subplot!
    for ax in axes.values():
        core.hide_axis(ax)

    for k in [ 'mnistTsne', 'fashionTsne'
    ]:
        axes[k].set_frame_on(False)


def plot_labels(axes):
    core.plot_labels(axes,
                     labels_to_plot=[
                         "mnistTsne",
                         "fashionTsne"
                     ],
                     label_ypos = {'fashionTsne': 1.,
                                   'mnistTsne': 1.},
                     label_xpos={'fashionTsne': -0.03,
                                 "mnistTsne": -0.03
                                 }
                     )


def get_fig_kwargs():
    width = 6.
    alpha = 2.
    return {"figsize": (width, alpha*width)}


###############################
# Plot functions for subplots #
###############################
#
# naming scheme: plot_<key>(ax)
#
# ax is the Axes to plot into
#


def plot_fashionTsne(ax):

    # get the data
    nImages = 150
    images = core.get_data('figDream/fashionImages.npy')
    positions = core.get_data('figDream/fashionPositions.npy')
    picSize = (12, 12)

    # trim the data
    indices = np.linspace(0, len(positions[:,0]),
                          endpoint=False, num=nImages).astype(int)
    images = images[indices[1:]]
    positions = positions[indices[1:]]

    # do the plotting
    aux.plot_tsne(ax, images, positions, picSize)

def plot_mnistTsne(ax):

    # get the data
    nImages = 150
    images = core.get_data('figDream/mnistImages.npy')
    positions = core.get_data('figDream/mnistPositions.npy')
    picSize = (12, 12)

    # trim the data
    indices = np.linspace(0, len(positions[:,0]),
                          endpoint=False, num=nImages).astype(int)
    images = images[indices[1:]]
    positions = positions[indices[1:]]

    # do the plotting
    aux.plot_tsne(ax, images, positions, picSize)

    pass




