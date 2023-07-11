# Drumming-EEG-Expt-Psychopy
This repository contains the code for the drumming experiment whereby we correlate drum rhythms with eeg signals and enjoyment levels.

Here, we have used Lab Streaming Layer(LSL) inside code snippets of the psychopy builder mode. 

We present drumbeat stimuli and send the associated event markers with LSL.

## Steps to re-create experiment
1. Create psychopy experiment using builder mode.
2. Import lsl and other libraries and create LSL outlet stream in "Before Experiment" section of the code snippet.
3. At the beginning and end of each routine of interest send an even marker.
4. Make sure you have an application listening to the marker stream (NeuroPype or LabRecorder).
