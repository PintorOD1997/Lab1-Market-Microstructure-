
"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: LAB 1 MARKET MICROSTRUCTURE                                                      -- #
# -- script: main.py : python script with the main functionality                                         -- #
# -- author: PintorOD1997                                                                      -- #
# -- license: GNU General Public License v3.0                                               -- #
# -- repository: https://github.com/PintorOD1997/Lab1-Market-Microstructure-                                                                    -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""

import numpy as np
import pandas as pd
import data as dt
import functions

# -- TEST 1 : 
# Load Data
OB = dt.openOB()
PT = dt.openPT()

# -- TEST 2 :
# OrderBook Metrics Testing
OBmetrics,m1,m4= functions.OB_metrics(OB)
OBohlcv = functions.OB_OHLCV(OBmetrics)
OBIMBmoments = functions.OBIMB_Moments(OBmetrics)

# -- TEST 3 :
# Public Trades Metrics Testing

tradesHora, volume, count, OHLCV = functions.PT_metrics(PT)


# -- TEST 4 :
# verify you can use plotly and visualize plots in web browser locally
