#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.1),
    on July 24, 2017, at 15:21
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, gui, visual, core, data, event, logging, sound, parallel
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = u'Calib'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u'test'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'C:\\Users\\labadmin\\Documents\\VisExp\\Calib.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1280, 1024), fullscr=True, screen=1,
    allowGUI=False, allowStencil=False,
    monitor=u'test2', color=[-1,-1,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "trial"
trialClock = core.Clock()
from psychopy.hardware import labjacks
TrialTriger = labjacks.U3()
TrialTriger.status=None
win2 = visual.Window(
    size=(600, 600), fullscr=False, screen=0,
    allowGUI=False, allowStencil=False,
    monitor=u'test2', color=[-1,-1,-1], colorSpace='rgb',
    blendMode='avg', useFBO=True, pos=[300, 300])
text2 = visual.TextStim(win=win2, name='text',
    text='',
    font=u'Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-6.0);

text2.setAutoDraw(True)
grating = visual.GratingStim(
    win=win, name='grating',units='norm', 
    tex='sin', mask=None,
    ori=0, pos=(0, 0), size=(2, 2), sf=0, phase=0.0,
    color=1.0, colorSpace='rgb', opacity=1,
    texRes=512, interpolate=True, depth=-3.0)

# Initialize components for Routine "end"
endClock = core.Clock()
from psychopy.hardware import labjacks
TrialTriger_2 = labjacks.U3()
TrialTriger_2.status=None

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Calib_params.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    # ------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    
    if thisTrial != None:
        trial_text = ''
        for paramName in thisTrial.keys():
            exec('temp = ' + paramName)
            trial_text += u'%s = %s  \n' % (paramName, temp)
    text2.text = trial_text
    win2.flip()
    grating.setColor(Color, colorSpace='rgb')
    # keep track of which components have finished
    trialComponents = [TrialTriger, grating]
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *TrialTriger* updates
        if t >= 0.0 and TrialTriger.status == NOT_STARTED:
            # keep track of start time/frame for later
            TrialTriger.tStart = t
            TrialTriger.frameNStart = frameN  # exact frame index
            TrialTriger.status = STARTED
            TrialTriger.setData(int(1))
        frameRemains = 0.0 + 0.01- win.monitorFramePeriod * 0.75  # most of one frame period left
        if TrialTriger.status == STARTED and t >= frameRemains:
            TrialTriger.status = STOPPED
            TrialTriger.setData(int(0))
        
        
        
        # *grating* updates
        if t >= 0 and grating.status == NOT_STARTED:
            # keep track of start time/frame for later
            grating.tStart = t
            grating.frameNStart = frameN  # exact frame index
            grating.setAutoDraw(True)
        frameRemains = 0 + 1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if grating.status == STARTED and t >= frameRemains:
            grating.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    if TrialTriger.status == STARTED:
        TrialTriger.setData(int(0))
    
    
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# ------Prepare to start Routine "end"-------
t = 0
endClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(0.010000)
# update component parameters for each repeat

# keep track of which components have finished
endComponents = [TrialTriger_2]
for thisComponent in endComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "end"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # *TrialTriger_2* updates
    if t >= 0.0 and TrialTriger_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        TrialTriger_2.tStart = t
        TrialTriger_2.frameNStart = frameN  # exact frame index
        TrialTriger_2.status = STARTED
        TrialTriger_2.setData(int(1))
    frameRemains = 0.0 + 0.01- win.monitorFramePeriod * 0.75  # most of one frame period left
    if TrialTriger_2.status == STARTED and t >= frameRemains:
        TrialTriger_2.status = STOPPED
        TrialTriger_2.setData(int(0))
    
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
if TrialTriger_2.status == STARTED:
    TrialTriger_2.setData(int(0))




# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
