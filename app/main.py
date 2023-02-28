#!/usr/bin/env python
# coding: utf-8





# ## Imports

# Add directory above current directory to path
import sys; sys.path.insert(0, '..')


# Pandas for data management
import pandas as pd
import obspy as obs

# os methods for manipulating paths
from os.path import dirname, join

# Bokeh basics 
from bokeh.io import curdoc
from bokeh.models.layouts import TabPanel, Tabs

import folium

from obspy import UTCDateTime
from numpy import array



# Each tab is drawn by one script
from tabs.tab_map import __tab_map
from tabs.tap_rings import __tab_rings


# Using included state data from Bokeh for map
from bokeh.sampledata.us_states import data as states


# ## Load Data


# ## Configurations


config = {}

config['workdir'] = "/home/andbro/Documents/ROMY/romy_dashboard/"

config['tbeg'] = UTCDateTime("2023-01-31 03:00")
config['tend'] = UTCDateTime("2023-01-31 05:00")



# ## Tabs

tab1 = __tab_rings(config)
tab2 = __tab_map(config)


# Put all the tabs into one application
tabs = Tabs(tabs = [tab1, tab2])

# Put the tabs in the current document for display
curdoc().add_root(tabs)


## END OF FILE






