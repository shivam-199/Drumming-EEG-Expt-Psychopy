#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.3),
    on May 29, 2022, at 11:56
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.1.3'
expName = 'test-real-time'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='E:\\studies\\college\\IIT Gandhinagar\\SEM III\\Internship\\Experimental Design\\PsychopyTest\\test-real-time_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1280, 720], fullscr=False, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# Setup ioHub
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# Initialize components for Routine "WelcomeScreen"
WelcomeScreenClock = core.Clock()
Welcome = visual.TextStim(win=win, name='Welcome',
    text='Welcome to the experiment!\nPress SPACE to continue.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "InstructionScreen"
InstructionScreenClock = core.Clock()
Instruction = visual.TextStim(win=win, name='Instruction',
    text='Your task is to listen to the played music and respond to the questions shown. The exact procedure is as follows.\n\n1. 5 to 10 seconds of silence, focus on the white cross on the screen, and relax.\n\n2. Listen to the music played in a relaxed state. Try not to make any body movements except natural blinking.\n\n3. Respond to the questions after each music listening trial, the answer should be according to the previously played track.\n\nRemember to focus on the white cross in the center of the screen at all times, and avoid head, finger, limb, and torso movements (no need to worry if you did move).\n\nRelax, breathe normally, clarify doubts if any, and press SPACE to continue.',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "StimulusFixation"
StimulusFixationClock = core.Clock()
PreTrialFixation = visual.TextStim(win=win, name='PreTrialFixation',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "AudioAndFixation"
AudioAndFixationClock = core.Clock()
DuringTrialFixation = visual.TextStim(win=win, name='DuringTrialFixation',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
DrumTrack = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='DrumTrack')
DrumTrack.setVolume(1.0)

# Initialize components for Routine "EnjoymentRating"
EnjoymentRatingClock = core.Clock()
KeyboardResponse = visual.TextStim(win=win, name='KeyboardResponse',
    text='Please enter your enjoyment rating of the song from 0 to 9.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "FinalScreen"
FinalScreenClock = core.Clock()
ThankYou = visual.TextStim(win=win, name='ThankYou',
    text='Thank You for participating in the experiment.\nThe experiment will end soon.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "WelcomeScreen"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
WelcomeScreenComponents = [Welcome, key_resp]
for thisComponent in WelcomeScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
WelcomeScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "WelcomeScreen"-------
while continueRoutine:
    # get current time
    t = WelcomeScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=WelcomeScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Welcome* updates
    if Welcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Welcome.frameNStart = frameN  # exact frame index
        Welcome.tStart = t  # local t and not account for scr refresh
        Welcome.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Welcome, 'tStartRefresh')  # time at next scr refresh
        Welcome.setAutoDraw(True)
    if Welcome.status == STARTED:
        if bool(0):
            # keep track of stop time/frame for later
            Welcome.tStop = t  # not accounting for scr refresh
            Welcome.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Welcome, 'tStopRefresh')  # time at next scr refresh
            Welcome.setAutoDraw(False)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WelcomeScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "WelcomeScreen"-------
for thisComponent in WelcomeScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Welcome.started', Welcome.tStartRefresh)
thisExp.addData('Welcome.stopped', Welcome.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "WelcomeScreen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "InstructionScreen"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
InstructionScreenComponents = [Instruction, key_resp_2]
for thisComponent in InstructionScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstructionScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "InstructionScreen"-------
while continueRoutine:
    # get current time
    t = InstructionScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstructionScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instruction* updates
    if Instruction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instruction.frameNStart = frameN  # exact frame index
        Instruction.tStart = t  # local t and not account for scr refresh
        Instruction.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instruction, 'tStartRefresh')  # time at next scr refresh
        Instruction.setAutoDraw(True)
    if Instruction.status == STARTED:
        if bool(0):
            # keep track of stop time/frame for later
            Instruction.tStop = t  # not accounting for scr refresh
            Instruction.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Instruction, 'tStopRefresh')  # time at next scr refresh
            Instruction.setAutoDraw(False)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "InstructionScreen"-------
for thisComponent in InstructionScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Instruction.started', Instruction.tStartRefresh)
thisExp.addData('Instruction.stopped', Instruction.tStopRefresh)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.addData('key_resp_2.started', key_resp_2.tStartRefresh)
thisExp.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
thisExp.nextEntry()
# the Routine "InstructionScreen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Stimulus/stimuli.csv'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "StimulusFixation"-------
    continueRoutine = True
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    PreTrialFixation.setText('+')
    # keep track of which components have finished
    StimulusFixationComponents = [PreTrialFixation]
    for thisComponent in StimulusFixationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    StimulusFixationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "StimulusFixation"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = StimulusFixationClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=StimulusFixationClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *PreTrialFixation* updates
        if PreTrialFixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            PreTrialFixation.frameNStart = frameN  # exact frame index
            PreTrialFixation.tStart = t  # local t and not account for scr refresh
            PreTrialFixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(PreTrialFixation, 'tStartRefresh')  # time at next scr refresh
            PreTrialFixation.setAutoDraw(True)
        if PreTrialFixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > PreTrialFixation.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                PreTrialFixation.tStop = t  # not accounting for scr refresh
                PreTrialFixation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(PreTrialFixation, 'tStopRefresh')  # time at next scr refresh
                PreTrialFixation.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in StimulusFixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "StimulusFixation"-------
    for thisComponent in StimulusFixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('PreTrialFixation.started', PreTrialFixation.tStartRefresh)
    trials.addData('PreTrialFixation.stopped', PreTrialFixation.tStopRefresh)
    
    # ------Prepare to start Routine "AudioAndFixation"-------
    continueRoutine = True
    routineTimer.add(10.000000)
    # update component parameters for each repeat
    DrumTrack.setSound(TrackPath, secs=10, hamming=True)
    DrumTrack.setVolume(1.0, log=False)
    # keep track of which components have finished
    AudioAndFixationComponents = [DuringTrialFixation, DrumTrack]
    for thisComponent in AudioAndFixationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    AudioAndFixationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "AudioAndFixation"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = AudioAndFixationClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=AudioAndFixationClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *DuringTrialFixation* updates
        if DuringTrialFixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            DuringTrialFixation.frameNStart = frameN  # exact frame index
            DuringTrialFixation.tStart = t  # local t and not account for scr refresh
            DuringTrialFixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(DuringTrialFixation, 'tStartRefresh')  # time at next scr refresh
            DuringTrialFixation.setAutoDraw(True)
        if DuringTrialFixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > DuringTrialFixation.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                DuringTrialFixation.tStop = t  # not accounting for scr refresh
                DuringTrialFixation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(DuringTrialFixation, 'tStopRefresh')  # time at next scr refresh
                DuringTrialFixation.setAutoDraw(False)
        # start/stop DrumTrack
        if DrumTrack.status == NOT_STARTED and t >= 0-frameTolerance:
            # keep track of start time/frame for later
            DrumTrack.frameNStart = frameN  # exact frame index
            DrumTrack.tStart = t  # local t and not account for scr refresh
            DrumTrack.tStartRefresh = tThisFlipGlobal  # on global time
            DrumTrack.play()  # start the sound (it finishes automatically)
        if DrumTrack.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > DrumTrack.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                DrumTrack.tStop = t  # not accounting for scr refresh
                DrumTrack.frameNStop = frameN  # exact frame index
                win.timeOnFlip(DrumTrack, 'tStopRefresh')  # time at next scr refresh
                DrumTrack.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in AudioAndFixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "AudioAndFixation"-------
    for thisComponent in AudioAndFixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('DuringTrialFixation.started', DuringTrialFixation.tStartRefresh)
    trials.addData('DuringTrialFixation.stopped', DuringTrialFixation.tStopRefresh)
    DrumTrack.stop()  # ensure sound has stopped at end of routine
    trials.addData('DrumTrack.started', DrumTrack.tStart)
    trials.addData('DrumTrack.stopped', DrumTrack.tStop)
    
    # ------Prepare to start Routine "EnjoymentRating"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_3.keys = []
    key_resp_3.rt = []
    _key_resp_3_allKeys = []
    # keep track of which components have finished
    EnjoymentRatingComponents = [KeyboardResponse, key_resp_3]
    for thisComponent in EnjoymentRatingComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    EnjoymentRatingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "EnjoymentRating"-------
    while continueRoutine:
        # get current time
        t = EnjoymentRatingClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=EnjoymentRatingClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *KeyboardResponse* updates
        if KeyboardResponse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            KeyboardResponse.frameNStart = frameN  # exact frame index
            KeyboardResponse.tStart = t  # local t and not account for scr refresh
            KeyboardResponse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(KeyboardResponse, 'tStartRefresh')  # time at next scr refresh
            KeyboardResponse.setAutoDraw(True)
        if KeyboardResponse.status == STARTED:
            if bool(0):
                # keep track of stop time/frame for later
                KeyboardResponse.tStop = t  # not accounting for scr refresh
                KeyboardResponse.frameNStop = frameN  # exact frame index
                win.timeOnFlip(KeyboardResponse, 'tStopRefresh')  # time at next scr refresh
                KeyboardResponse.setAutoDraw(False)
        
        # *key_resp_3* updates
        waitOnFlip = False
        if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.tStart = t  # local t and not account for scr refresh
            key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_3.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_3.getKeys(keyList=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], waitRelease=False)
            _key_resp_3_allKeys.extend(theseKeys)
            if len(_key_resp_3_allKeys):
                key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in EnjoymentRatingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "EnjoymentRating"-------
    for thisComponent in EnjoymentRatingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('KeyboardResponse.started', KeyboardResponse.tStartRefresh)
    trials.addData('KeyboardResponse.stopped', KeyboardResponse.tStopRefresh)
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
        key_resp_3.keys = None
    trials.addData('key_resp_3.keys',key_resp_3.keys)
    if key_resp_3.keys != None:  # we had a response
        trials.addData('key_resp_3.rt', key_resp_3.rt)
    trials.addData('key_resp_3.started', key_resp_3.tStartRefresh)
    trials.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
    # the Routine "EnjoymentRating" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1.0 repeats of 'trials'


# ------Prepare to start Routine "FinalScreen"-------
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
FinalScreenComponents = [ThankYou]
for thisComponent in FinalScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
FinalScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "FinalScreen"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = FinalScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=FinalScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ThankYou* updates
    if ThankYou.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ThankYou.frameNStart = frameN  # exact frame index
        ThankYou.tStart = t  # local t and not account for scr refresh
        ThankYou.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ThankYou, 'tStartRefresh')  # time at next scr refresh
        ThankYou.setAutoDraw(True)
    if ThankYou.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > ThankYou.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            ThankYou.tStop = t  # not accounting for scr refresh
            ThankYou.frameNStop = frameN  # exact frame index
            win.timeOnFlip(ThankYou, 'tStopRefresh')  # time at next scr refresh
            ThankYou.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in FinalScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "FinalScreen"-------
for thisComponent in FinalScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('ThankYou.started', ThankYou.tStartRefresh)
thisExp.addData('ThankYou.stopped', ThankYou.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
