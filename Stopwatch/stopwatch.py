#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 18:00:07 2021

@author: zub
"""

# template for "Stopwatch: The Game"
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

# define global variables
tenths = 0
attempts = 0
hits = 0
ticking = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(tenths):
    A = tenths // 600
    B = ((tenths // 10) % 60) // 10
    C = (((tenths // 10) % 60) % 10) % 10
    D = tenths % 10
    return str(A) + ":" + str(B) + str(C) + "." + str(D)
    pass

# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global ticking
    timer.start()
    ticking = True
    
def stop():
    global attempts, hits, ticking
    timer.stop()
    if ticking == True:
        attempts += 1
        if tenths % 10 == 0:
            hits += 1
        else:
            hits = hits
    else:
        attempts = attempts
        hits = hits
    ticking = False
            
           
def reset():
    global tenths, attempts, hits, ticking
    timer.stop()
    tenths = 0
    attempts = 0
    hits = 0
    ticking = True
    

# define event handler for timer with 0.1 sec interval
def tenths_second():
    global tenths
    tenths += 1
    
# define draw handler
def draw_current_time(canvas):
    canvas.draw_text(str(attempts) + "/" + str(hits), [250, 30], 20, "Red")
    if tenths <= 6000:
        canvas.draw_text(format(tenths), [125, 110], 20, "White")
    else:
        canvas.draw_text("The time is up!", [125, 110], 20, "White")
        
# create frame
frame = simplegui.create_frame("Stopwatch", 300, 200)
Button1 = frame.add_button("Start", start, 50)
Button2 = frame.add_button("Stop", stop, 50)
Button3 = frame.add_button("Reset", reset, 50)

# register event handlers
timer = simplegui.create_timer(100, tenths_second)
frame.set_draw_handler(draw_current_time)

# start frame
frame.start()
