#!/usr/bin/env python
##############################LIBRARIES########################################################
from ROOT import TFile
from sys import exit
try:
    import numpy as np
except:
    print("Failed to import numpy.")
    exit()

#################################LOADING THE DATA##############################################
data = TFile.Open("/home/jui/Desktop/tmva/sample_images_32x32.root")
print(data.ls())

sig = data.Get('sig_tree;2')
bkg = data.Get('bkg_tree;2')

signal = np.zeros((1,1024))
for event in sig:
    signal = np.vstack((signal, np.vstack(sig.vars).T))   
signal = signal[1:,:]
print(signal.shape)


background = np.zeros((1,1024))
for event in bkg:
    background = np.vstack((background, np.vstack(bkg.vars).T))
background = background[1:,:]
print(background.shape)

np.save('pytorch_signal', signal)
np.save('pytorch_background', background)
# sig = float(sig["vars"])
# signal = sig.AsMatrix(["vars"])
