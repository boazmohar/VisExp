#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.1),
    on July 21, 2017, at 17:41
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
expName = u'MouseScrennCalib'  # from the Builder filename that created this script
expInfo = {u'participant': u'BMWR67', u'Run': u'Run1'}
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
    originPath=None,
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
    monitor=u'xrite', color=[0,0,0], colorSpace='rgb',
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
TrialTrigger = labjacks.U3()
# Adding status to labjack U3
TrialTrigger.status=None
tex1 = np.ones((2,2,3)) *-1
tex1[0, 0, 2] = 1
tex1[1, 1, 2] = 1
grating = visual.GratingStim(
    win=win, name='grating',units='pix', 
    tex=tex1, mask=None,
    ori=0, pos=(0, 0), size=2048, sf=0.5, phase=0.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=512, interpolate=False, depth=-3.0)
polygon = visual.Rect(
    win=win, name='polygon',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=False)
win2 = visual.Window(
    size=(600, 600), fullscr=False, screen=0,
    allowGUI=False, allowStencil=False,
    monitor=u'xrite', color=[-1,-1,-1], colorSpace='rgb',
    blendMode='avg', useFBO=True, pos=[300, 300])
text2 = visual.TextStim(win=win2, name='text',
    text='',
    font=u'Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-6.0);

text2.setAutoDraw(True)
import pickle
import shutil
base = u'V:\\users\\Aaron'
date = data.getDateStr(format='%y%m%d')
filename = '%s\\%s_%s\\%s\\vis' % (base, date,
expInfo['participant'], expInfo['Run'])
directory = os.path.dirname(filename)
if not os.path.exists(directory):
    os.makedirs(directory)
#os.chdir(directory)
saved=False
logging.filename = filename+'.log'
thisExp.filename=filename
src = _thisDir + '\\' + expName + '.psyexp'
des = directory + '\\' + expName + '.psyexp'
shutil.copy(src, des)
print('copied %s to %s' % (src, des))

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=20, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('MouseCalib.xlsx'),
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
    routineTimer.add(10.000000)
    # update component parameters for each repeat
    
    
    polygon.setFillColor(color)
    polygon.setLineColor(color)
    if thisTrial != None:
        trial_text = ''
        for paramName in thisTrial.keys():
            exec('temp = ' + paramName)
            trial_text += u'%s = %s  \n' % (paramName, temp)
        print(trial_text)
    text2.text = trial_text
    win2.flip()
    if not saved:
        pickle.dump(trials, open(filename+'.p','wb'))
        saved=True
        print('Saved to %s' % filename+'.p')
        
    # keep track of which components have finished
    trialComponents = [TrialTrigger, grating, polygon]
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *TrialTrigger* updates
        if t >= 0.0 and TrialTrigger.status == NOT_STARTED:
            # keep track of start time/frame for later
            TrialTrigger.tStart = t
            TrialTrigger.frameNStart = frameN  # exact frame index
            TrialTrigger.status = STARTED
            TrialTrigger.setData(int(255))
        frameRemains = 0.0 + 0.01- win.monitorFramePeriod * 0.75  # most of one frame period left
        if TrialTrigger.status == STARTED and t >= frameRemains:
            TrialTrigger.status = STOPPED
            TrialTrigger.setData(int(0))
        
        
        
        # *grating* updates
        if t >= 5 and grating.status == NOT_STARTED:
            # keep track of start time/frame for later
            grating.tStart = t
            grating.frameNStart = frameN  # exact frame index
            grating.setAutoDraw(True)
        frameRemains = 5 + 5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if grating.status == STARTED and t >= frameRemains:
            grating.setAutoDraw(False)
        
        # *polygon* updates
        if t >= 0.0 and polygon.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon.tStart = t
            polygon.frameNStart = frameN  # exact frame index
            polygon.setAutoDraw(True)
        frameRemains = 0.0 + 5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if polygon.status == STARTED and t >= frameRemains:
            polygon.setAutoDraw(False)
        
        
        
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
    if TrialTrigger.status == STARTED:
        TrialTrigger.setData(int(0))
    
    
    
    
    thisExp.nextEntry()
    
# completed 20 repeats of 'trials'





# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
