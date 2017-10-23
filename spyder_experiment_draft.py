# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 14:17:22 2017

@author: Adamowicz
"""

# -*- coding: utf-8 -*-
"""
Date: 19 Oct 2017

@author: Line & Adam
"""

import os
os.chdir("C:\Users\Adam\Documents\cogsci\Mind and consciousness\exam\python")


import ppc
from psychopy import visual, core, event, gui
from random import sample
import random

def show_info(txt):
# show a message
    msg = visual.TextStim(win, text=txt, pos = [0,0.2])
    msg2 = visual.TextStim(win, text = "Press space or Enter to continue", pos = [0,-0.6])
    msg.draw()
    msg2.draw()
    win.flip()
# wait for a keypress
    key = event.waitKeys()
    if key[0] in ['escape']: core.quit()

intro = [u"""Welcome to translation experiment!""",
u"""NOW ARE EXPERIMENTS!"""]




#---------------------------------------------------------------------------------------------
#THE EXPERIMENT: 3 steps: popup-box, introduction and trial
#priming and mask variables
                


#1:popup box
popup = gui.Dlg(title = "Vores farve experiment")
popup.addField("Number:")
popup.addField("gender", choices = ["Male","Female","Other"])
popup.addField("Nationality:")
popup.show()
if popup.OK:
    ID = popup.data[0]    
    gender = popup.data[1]
    nationality = popup.data[2]

else:
    core.quit()


topic_trials = [] 


topics = [ ["""bakterie""", u"""Historie_1""","""Historie_2"""],["""Volcano""","""Historie_1""","""historie_2"""]]

k = random.randint(0,1)

#equal number of ones and zeroes. Ensures even distribution of conditions, i.e. if threat or neutral is shown first
random_numbers_list = [1,0,1,0,0,1]

for n,topic in enumerate(topics):
  # Add a dictionary for every trial
    topic_trials += [{
    'ID': ID,
    "Nationality": nationality,
    'gender': gender,    
    "topic":topics[n][0],
    "t_story":topics[n][1],
    "n_story":topics[n][2],
    "t_story_rating":"Na",
    "n_story_rating":"Na",
    "condition":random_numbers_list[n],
    "topic_knowledge":"Na",
    "media_time":"Na",
    "rating_EB":"Na",
    "rating_MX":"Na",
    "rating_politiken":"Na",
    "rating_weekend_a":"Na",
    "block_order":k,
    "rt_text":"Na",
    "rt_response":"Na"
    }]



person_stories = ["""person_story_1""", """person_story2"""]

person_stories_trials = []


for n,story in enumerate(person_stories):
  # Add a dictionary for every trial
    person_stories_trials += [{
    'ID': ID,
    "Nationality": nationality,
    'gender': gender,    
    "topic":"",
    "t_story":person_stories[n],
    "n_story":"Na",
    "t_story_rating":"Na",
    "n_story_rating":"Na",
    "condition":"Na",
    "topic_knowledge":"Na",
    "media_time":"Na",
    "rating_EB":"Na",
    "rating_MX":"Na",
    "rating_politiken":"Na",
    "rating_weekend_a":"Na",
    "block_order":k,
    "rt_text":"Na",
    "rt_response":"Na"
    }]

# Randomize order
person_stories_trials = sample(person_stories_trials, len(person_stories_trials))
topic_trials = sample(topic_trials, len(topic_trials))

win = visual.Window(fullscr = False, color = "Black")


#rating_scale = visual.RatingScale(win, markerColor = "White", scale = "",low = 1, high = 5,
 #                                 labels = ["1 = EB"])
rating_scale = visual.RatingScale(win, markerColor = "White", scale = "",low = 1, high = 5, labels = ["very incompetent","very competent"])

def get_rating():
    txt = "From which newspaper do you believe that the story was from?"
    msg = visual.TextStim(win, text = txt, pos=(0,0.1))   
    rating_scale.reset()
    while rating_scale.noResponse: 
        rating_scale.draw()
        msg.draw()
        win.flip()
    answer = rating_scale.getRating()
    return(answer)

stopwatch = core.Clock()

def topic_function():
    for trial in topic_trials:
        if trial["condition"] == 1:
            #show first story
            txt = trial["t_story"]            
            stopwatch.reset()
            show_info(txt)
            trial["rt_text"] = stopwatch.getTime()
            
            stopwatch.reset()            
            trial["t_story_rating"] =  get_rating()
            trial["rt_response"] = stopwatch.getTime()
            #show second story
            txt = trial["n_story"]  
            stopwatch.reset()
            show_info(txt)
            trial["rt_text"] = stopwatch.getTime()
            
            
            stopwatch.reset()            
            trial["n_story_rating"] =  get_rating()
            trial["rt_response"] = stopwatch.getTime()
            #get general topic knowledge                        
            trial["topic_knowledge"] = rate_topic_knowledge(trial["topic"])
            #save trial
            print(trial)
            writer.write(trial)
            
        else:
            txt = trial["n_story"]
            stopwatch.reset()
            show_info(txt)
            trial["rt_text"] = stopwatch.getTime()
            
            
            stopwatch.reset()            
            trial["n_story_rating"] =  get_rating()
            trial["rt_response"] = stopwatch.getTime()
            
            txt = trial["t_story"]
            stopwatch.reset()
            show_info(txt)
            trial["rt_text"] = stopwatch.getTime()      
            
            
            stopwatch.reset()            
            trial["t_story_rating"] =  get_rating()
            trial["rt_response"] = stopwatch.getTime()
            
            trial["topic_knowledge"] = rate_topic_knowledge(trial["topic"])
            print(trial)
            writer.write(trial)


def person_stories_function():
    for trial in person_stories_trials:
        txt = trial["t_story"]
        show_info(txt)
        trial["t_story_rating"]= get_rating()
        writer.write(trial)


newspaper_rating = visual.RatingScale(win, markerColor = "White", scale = "",low = 1, high = 5, labels = ["very incompetent","very competent"])

def rate_newspaper(txt):
    full_txt = "On a scale from 0 to 5, how competent do you think " + txt + " is?"
    msg = visual.TextStim(win, text = full_txt, pos=(0,0.1))   
    
    newspaper_rating.reset()
    while newspaper_rating.noResponse: 
        newspaper_rating.draw() 
        msg.draw()
        win.flip()
    return(newspaper_rating.getRating())

knowledge_rating = visual.RatingScale(win, markerColor = "White", scale = "",low = 1, high = 5, labels = ["Nothing","Some","Expert"])

def rate_topic_knowledge(txt):
    full_txt = "How much knowledge do you have about " + txt +"?"
    msg = visual.TextStim(win, text = full_txt, pos=(0,0.1))   
    
    knowledge_rating.reset()
    while knowledge_rating.noResponse: 
        knowledge_rating.draw() 
        msg.draw()
        win.flip()
    return(knowledge_rating.getRating())


media_rating = visual.RatingScale(win, markerColor = "White", scale = "",low = 1, high = 5, labels = ["0-2", "2-4","4-6""6-8","8+"])

def rate_media():
    full_txt = "How many hours per week do you spend following the news?"
    msg = visual.TextStim(win, text = full_txt, pos=(0,0.1))   
    
    media_rating.reset()
    while media_rating.noResponse: 
        media_rating.draw() 
        msg.draw()
        win.flip()
    return(media_rating.getRating())

writer = ppc.csvWriter(ID , saveFolder="data",headerTrial=person_stories_trials[1]) 

####unite dataframes to df
for i in intro:
    show_info(i)
    
    
if k == 0:
    person_stories_function()
    topic_function()
else:
    topic_function()
    person_stories_function()


news_rating = {
    'ID': ID,
    "Nationality": nationality,
    'gender': gender,    
    "topic":"Na",
    "t_story":"Na",
    "n_story":"Na",
    "t_story_rating":"",
    "n_story_rating":"Na",
    "condition":"Na",
    "topic_knowledge":"Na",
    "media_time":"Na",
    "rating_EB":"Na",
    "rating_MX":"Na",
    "rating_politiken":"Na",
    "rating_weekend_a":"Na",
    "block_order":"na",
    "rt_text":"Na",
    "rt_response":"Na
    }
    
    

news_rating["rating_EB"]=rate_newspaper("Ekstra Bladet")
news_rating["rating_MX"]=rate_newspaper("Metro Express")
news_rating["rating_politiken"]=rate_newspaper("Politiken")
news_rating["rating_weekend_a"]=rate_newspaper("Weekend Avisen")
news_rating["media_time"] = rate_media()

writer.write(news_rating)

core.quit()