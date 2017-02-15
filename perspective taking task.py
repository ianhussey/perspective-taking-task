#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.82.01), Wed Feb 15 17:28:21 2017
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = u'perspective taking task'  # from the Builder filename that created this script
expInfo = {u'gender': u'', u'age': u'', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data' + os.sep + '%s_%s' %(expInfo['participant'], expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1600, 900), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor=u'testMonitor', color=u'black', colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='norm')
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "intro"
introClock = core.Clock()
intro_text = visual.TextStim(win=win, ori=0, name='intro_text',
    text=u'This task will provide you with scenarios at the top of the screen.\n\nSometimes you\'ll be asked to answer from your own perspective, and sometimes from other perspectives.\n\nGo as slowly as you need to get as many correct as possible.\n\n** Please read each scenario as if in your own voice, where the "I" is the reader. **\n\nPress "e" for the option on the left or "i" for the option on the right.\n\nPress either key to start.',    font=u'Arial',
    pos=[0, 0], height=0.08, wrapWidth=1.9,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-1.0)

# Initialize components for Routine "ITI"
ITIClock = core.Clock()
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')

# Initialize components for Routine "trial"
trialClock = core.Clock()
statement_label = visual.TextStim(win=win, ori=0, name='statement_label',
    text='default text',    font=u'Arial',
    pos=[0, 0.2], height=0.1, wrapWidth=1.9,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)
perspective_label = visual.TextStim(win=win, ori=0, name='perspective_label',
    text='default text',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=1.9,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-1.0)
question_label = visual.TextStim(win=win, ori=0, name='question_label',
    text='default text',    font=u'Arial',
    pos=[0, -0.2], height=0.1, wrapWidth=1.9,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-2.0)
left_label = visual.TextStim(win=win, ori=0, name='left_label',
    text='default text',    font=u'Arial',
    pos=[-0.5,-0.8], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-4.0)
right_label = visual.TextStim(win=win, ori=0, name='right_label',
    text='default text',    font=u'Arial',
    pos=[0.5,-0.8], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-5.0)

# Initialize components for Routine "thanks"
thanksClock = core.Clock()
end_text = visual.TextStim(win=win, ori=0, name='end_text',
    text=u'End of task.',    font=u'Arial',
    pos=[0, -0.2], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "intro"-------
t = 0
introClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
intro_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
intro_resp.status = NOT_STARTED
# keep track of which components have finished
introComponents = []
introComponents.append(intro_resp)
introComponents.append(intro_text)
for thisComponent in introComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "intro"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = introClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *intro_resp* updates
    if t >= 1 and intro_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        intro_resp.tStart = t  # underestimates by a little under one frame
        intro_resp.frameNStart = frameN  # exact frame index
        intro_resp.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if intro_resp.status == STARTED:
        theseKeys = event.getKeys(keyList=['e', 'i'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # *intro_text* updates
    if t >= 0 and intro_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        intro_text.tStart = t  # underestimates by a little under one frame
        intro_text.frameNStart = frameN  # exact frame index
        intro_text.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in introComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "intro"-------
for thisComponent in introComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions(u'stimuli.csv'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    #------Prepare to start Routine "ITI"-------
    t = 0
    ITIClock.reset()  # clock 
    frameN = -1
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    ITIComponents = []
    ITIComponents.append(ISI)
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "ITI"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ITIClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *ISI* period
        if t >= 0 and ISI.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI.tStart = t  # underestimates by a little under one frame
            ISI.frameNStart = frameN  # exact frame index
            ISI.start(1)
        elif ISI.status == STARTED: #one frame should pass before updating params and completing
            ISI.complete() #finish the static period
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "ITI"-------
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    #------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    statement_label.setText(statement)
    perspective_label.setText(perspective)
    question_label.setText(question)
    response = event.BuilderKeyResponse()  # create an object of type KeyResponse
    response.status = NOT_STARTED
    left_label.setText(response_label_left)
    right_label.setText(response_label_right)
    # keep track of which components have finished
    trialComponents = []
    trialComponents.append(statement_label)
    trialComponents.append(perspective_label)
    trialComponents.append(question_label)
    trialComponents.append(response)
    trialComponents.append(left_label)
    trialComponents.append(right_label)
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "trial"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *statement_label* updates
        if t >= 0 and statement_label.status == NOT_STARTED:
            # keep track of start time/frame for later
            statement_label.tStart = t  # underestimates by a little under one frame
            statement_label.frameNStart = frameN  # exact frame index
            statement_label.setAutoDraw(True)
        
        # *perspective_label* updates
        if t >= 0 and perspective_label.status == NOT_STARTED:
            # keep track of start time/frame for later
            perspective_label.tStart = t  # underestimates by a little under one frame
            perspective_label.frameNStart = frameN  # exact frame index
            perspective_label.setAutoDraw(True)
        
        # *question_label* updates
        if t >= 0 and question_label.status == NOT_STARTED:
            # keep track of start time/frame for later
            question_label.tStart = t  # underestimates by a little under one frame
            question_label.frameNStart = frameN  # exact frame index
            question_label.setAutoDraw(True)
        
        # *response* updates
        if t >= 0 and response.status == NOT_STARTED:
            # keep track of start time/frame for later
            response.tStart = t  # underestimates by a little under one frame
            response.frameNStart = frameN  # exact frame index
            response.status = STARTED
            # keyboard checking is just starting
            response.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if response.status == STARTED:
            theseKeys = event.getKeys(keyList=['e', 'i'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if response.keys == []:  # then this was the first keypress
                    response.keys = theseKeys[0]  # just the first key pressed
                    response.rt = response.clock.getTime()
                    # was this 'correct'?
                    if (response.keys == str(required_key)) or (response.keys == required_key):
                        response.corr = 1
                    else:
                        response.corr = 0
                    # a response ends the routine
                    continueRoutine = False
        
        # *left_label* updates
        if t >= 0 and left_label.status == NOT_STARTED:
            # keep track of start time/frame for later
            left_label.tStart = t  # underestimates by a little under one frame
            left_label.frameNStart = frameN  # exact frame index
            left_label.setAutoDraw(True)
        
        # *right_label* updates
        if t >= 0.0 and right_label.status == NOT_STARTED:
            # keep track of start time/frame for later
            right_label.tStart = t  # underestimates by a little under one frame
            right_label.frameNStart = frameN  # exact frame index
            right_label.setAutoDraw(True)
        
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
    
    #-------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if response.keys in ['', [], None]:  # No response was made
       response.keys=None
       # was no response the correct answer?!
       if str(required_key).lower() == 'none': response.corr = 1  # correct non-response
       else: response.corr = 0  # failed to respond (incorrectly)
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('response.keys',response.keys)
    thisExp.addData('response.corr', response.corr)
    if response.keys != None:  # we had a response
        thisExp.addData('response.rt', response.rt)
    thisExp.nextEntry()
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials'

# get names of stimulus parameters
if trials.trialList in ([], [None], None):  params = []
else:  params = trials.trialList[0].keys()
# save data for this loop
trials.saveAsExcel(filename + '.xlsx', sheetName='trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

#------Prepare to start Routine "thanks"-------
t = 0
thanksClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
end_response = event.BuilderKeyResponse()  # create an object of type KeyResponse
end_response.status = NOT_STARTED
# keep track of which components have finished
thanksComponents = []
thanksComponents.append(end_text)
thanksComponents.append(end_response)
for thisComponent in thanksComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "thanks"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = thanksClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end_text* updates
    if t >= 0.4 and end_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        end_text.tStart = t  # underestimates by a little under one frame
        end_text.frameNStart = frameN  # exact frame index
        end_text.setAutoDraw(True)
    
    # *end_response* updates
    if t >= 0.0 and end_response.status == NOT_STARTED:
        # keep track of start time/frame for later
        end_response.tStart = t  # underestimates by a little under one frame
        end_response.frameNStart = frameN  # exact frame index
        end_response.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if end_response.status == STARTED:
        theseKeys = event.getKeys(keyList=['return'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in thanksComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "thanks"-------
for thisComponent in thanksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "thanks" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
win.close()
core.quit()
