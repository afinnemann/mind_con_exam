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


topics = [ ["""volcano""", 

u"""A team of researchers warns against the international dangers of the Icelandic volcano Kverkfjoll. 
Their conclusion is based on studies of an abnormal layer 8 kilometers below the surface of the earth. 
This abnormal layer suggests a large deposit of active magma. The international team have estimated 
that an eruption with this size will have the power to blow rocks and ash up to a height of 70 km and 
cause air pollution on massive scale. If this happens it would be the most powerful eruption in North 
Europe for 120 years.""",

"""Recent studies of the Islandic volcano, Kverkfjoll, have found an unusual layer 
8 to10 km deep in the volcano, and suggest it to be active magma. Local scientists find its activity 
disturbing and assume an eruption of the volcano to be the biggest nature catastrophe in Island in 120 years. 
It is expected that an eruption of Kverkfjoll will blow ash and stone rockets 70 km into the stratosphere, 
which will pulverize the air. The observatory team of the volcano is currently working on ways to prepare 
for the eruption, to minimize potential damage."""],

["""corruption""",

"""Corruption has long been a serious political threat in Eastern European countries, however new analyses 
suggest that the problem might have more widespread consequences than previously thought. Not only have 
corruption increased by 35 percent over the past 40 years in these countries, but according to EU it is now 
a tendency that inflates our concept of Democracy. Transparency International reports that the direct 
influence of corruption on the average citizen is increasing as a result of this tendency. 
""",

"""Transparency International, an organisation based in Germany fighting corruption, has recently published 
an analysis, which indicates an increase of corruption in Eastern European countries of 35 percent over the 
past 40 years. The increase is seen in both the private and public sectors, and several local analysts 
describe this as a steady tendency challenging their concept of Democracy. Peter Eigen, Director of 
Transparency International, comments that this tendency has serious consequences for both private companies 
investing in new markets, as well as the general population who increasingly are paying to corruption, either 
directly or indirectly. 
"""]

["""pollution""", 

u"""Recently an article in Ingenioeren.dk claimed that at least half of the children in Shanghai, have too 
high amounts of lead in their blood, as a consequence of high air pollution. Air pollution is a problem 
rapidly spreading in many of the biggest cities in the world, and the consequences are highly riskful. It 
often affects both the intelligence of children and might causes behavioural problems. Further, it is suggested
by international environmental organisations that the average life expectancy of a traffic officer in Beijing 
is only 40 years. Implementing initiatives to reduce the amount of harming particles, deduced by cars and 
heavy industries, has therefore become a central topic for the future. 
""", 

"""High air pollution has settled as a heavy problem out in many of the biggest cities in the world. 
The Chinese newspaper Chinoq estimates that in 50 percent of children in Shanghai the lead levels in their 
blood is too high, which is thought to cause lower intelligence and behavioural problems. Local chinese 
authorities have reported that a traffic officer in the busy intersections of Beijing has an average life 
expectancy of only 40 years. It has therefore become part of the local agenda, to implement initiatives, 
which can lower the amount of harming particles, deduced by cars and heavy industries.""",] 


["""bacteria""", 

u"""A new bacteria-mutation has recently started to evolve in the most southern parts of Spain. 
The HKDK-bacteria attacks the calcium cycle of the body, and causes symptoms such as whitening of nails 
and pain in the bones. It is estimated that at least 250 people have already been treated for the HKDK-bacteria.
According to the Spanish media El Mundo, the bacteria-mutation has spread like wildfire, and international 
media suggest that it is a problem of severe character. The mutation might be a result of the large 
concentrations of pesticides found in some areas, suggests the Danish professor of immunology, Preben Favrholdt.
""", 

u"""The Spanish media El Mundo reports that a bacteria-mutation has put down roots in the most southern parts 
of Spain. According to official numbers at least 250 people have been treated for the HKDK-bacteria. However, 
local media suggest that the problem is far bigger. The bacteria attacks the calcium cycle of the body and the 
first symptoms are massive whitening of nails, which develop to intense arhritis-like pain in the attacked 
bones. The Spanish professor José Garazo, reports to El Mundo that the mutation might be associated with the 
large concentration of toxic pesticides in certain areas. """,] 


["""mafia""", 

"""A new polish mafia have gained strength during the last years and have therefore spread like rats to other 
parts of Europe. Eastern German cities have been especially hit by this new wave of structured criminality. 
Local gangs have been outmaneuvered, and the polish mafia is making big money on drugs, blackmailing and 
protection money. Protection money is a fee that shops are required to pay to mafia. If this is not done, the 
shopowners will experience harsh harassment from the mafia. """, 

u"""A recent article in the German newspaper Die Zeit describes how polish criminals have settled down in 
Eastern Germany. According to Die Zeit the so called Polish Mafia is very structured in their approach and 
have quickly gained influence on the drug and blackmail market in several East German cities.They have 
become particularly notorious for their use of so called "protection" money. Mafia members visit local shops 
and cafés and require a fee to be paid in return for protection. It is unclear whom they are protected from 
when they pay, but it is clear that if they refuse to pay, their shops and cafés are likely to be vandalized 
by mafia members. """,] 


["""topic""", 

"""historie1""", 

"""historie2""",]]

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
    "t_story_rating":"NA",
    "n_story_rating":"NA",
    "condition":random_numbers_list[n],
    "topic_knowledge":"NA",
    "media_time":"NA",
    "rating_EB":"NA",
    "rating_MX":"NA",
    "rating_politiken":"NA",
    "rating_weekend_a":"NA",
    "block_order":k,
    "rt_text":"NA",
    "rt_response":"NA",
    "blue_eyes": "NA",
    "hayfever": "NA", 
    "countryside": "NA", 
    "pets": "NA", 
    "infertility": "NA", 
    "sleep": "NA"
    }]



person_stories = [
["""Blue-eyed""",

"""A new article published by experts from the prestigious John Hopkins Hospital in the US shows that people 
with blue eyes are more likely to develop the dangerous kidney disease Biliar Cyrrosis. The researchers have 
shown that the disease is linked to lack of a gene sequence that is also linked to absence of brown color in 
the eyes. Johan Nybro, chief surgeon at Rigshospitalet, says that this is vital information with regard to 
early diagnosis of Biliar Cyrrosis and treatment of the deadly disease."""], 

["""Hayfever""",

u"""Danish doctors have investigated the connection between hay fever and other lung diseases. Their 
surprising result shows that air channels and lungs develop differently in people with hay fever. 
This development leads to so called "small lungs" which can cause the dangerous disease COPD (KOL) later 
in life. COPD was thought to be mainly caused by smoking but the new research shows that this picture 
is more complicated. The danish researchers furthermore suggests that people with hay fever needs special 
supervision later in so that development of COPD can be caught as early as possible."""]

["""countryside""",

"""Moving from a peaceful rural area to the city can be a complicated but also dangerous affair, new research 
suggests. People who have grown up in rural districts lies in first place when it comes to being involved in 
traffic accidents in bigger cities. The obivious explanation is that they are not as experienced in navigating 
in the often hectic traffic found in cities. The biggest threat for people who grew up on the countryside, 
is when they are travelling as pedastrians. Here, they are much more likely to be hit by cars than those who 
did not. """]

["""pets""",

"""German researchers have found that having a pet during childhood have a positive effect on both your 
psychological and physical well being later in life. Early this year there was extensive media coverage of 
the positive effect of pets on the health of their owners. Although this result has been criticised, new 
reports argue that people without pets are more likely to suffer from depression, and it has been found that 
owning a pet can reduce the risk of heart attacks by more than a third. This result has come as a surprise 
since the effects of pets seems to last beyond the lifetime of the pet. """]

["""infertility""",

u"""According to a recent research published in the journal Environment International, carrying your phone 
in your pocket has a high risks of affecting your fertility negatively. The large study included 14.000 men 
and women, and found that when you are exposed to the electromagnetic radiation from mobile phones or other 
electronic devices it can reduce the mobility of the sperm to move towards the egg. In the woman it can cause 
reductions in the release of the hormones preparing the uterus for the egg, which challenges the fertilization 
of the egg. According to the researchers, the effect is primarily observed in people who normally carry their 
phone in their pocket (or have other devices, such as a laptop, close to the crotch) for more than 5 hours a 
day.
"""]

["""sleep""",

"""A new study from University of Amsterdam finds that sleeping on your stomach can have serious consequences. 
It has long been known that sleeping on your stomach places a strain on your back and spine, making it 
difficult to maintain a neutral spine position which can cause pain in muscles and joints. However, the 
consequences are apparently more serious than that. Since the spine is a pipeline for your nerves, spinal 
stress causes spinal stress on the nerves, and if this occurs often, it can cause chronic impairments of the 
affected nerves. According to the researchers the consequences can be impaired mobility or numbness of the 
particular body parts. """]]

person_stories_trials = []


for n,story in enumerate(person_stories):
  # Add a dictionary for every trial
    person_stories_trials += [{
    'ID': ID,
    "Nationality": nationality,
    'gender': gender,    
    "topic":story[0],
    "t_story":story[1],
    "n_story":"NA",
    "t_story_rating":"NA",
    "n_story_rating":"NA",
    "condition":"NA",
    "topic_knowledge":"NA",
    "media_time":"NA",
    "rating_EB":"NA",
    "rating_MX":"NA",
    "rating_politiken":"NA",
    "rating_weekend_a":"NA",
    "block_order":k,
    "rt_text":"NA",
    "rt_response":"NA",
    "blue_eyes": "NA",
    "hayfever": "NA", 
    "countryside": "NA", 
    "pets": "NA", 
    "infertility": "NA", 
    "sleep": "NA"
    }]

# Randomize order
person_stories_trials = sample(person_stories_trials, len(person_stories_trials))
topic_trials = sample(topic_trials, len(topic_trials))

win = visual.Window(fullscr = False, color = "Black")



rating_scale = visual.RatingScale(win, markerColor = "White", scale = "",low = 1, high = 4, labels = ["1","2","3","4"])

def get_rating():
    txt = """From which newspaper do you believe that the story was from? 
            1: Metro Express
            2: Politiken
            3: Ekstra Bladet
            4: Weekend Avisen"""
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
        stopwatch.reset()            
        show_info(txt)
        trial["rt_text"] = stopwatch.getTime()
        stopwatch.reset()            
        trial["t_story_rating"]= get_rating()
        trial["rt_response"] = stopwatch.getTime()
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
intro = [u"""Welcome to the translation experiment!""", """In this experiment you will read small extracts from newspaper articles.\nThe extracts were taken from various Danish newspapers and translated into English.""", """ 
You will read the extracts one by one and you will afterwards be asked which newspaper you think the story came from.
\nThere are a total of 18 small extract.""", """, 
You will be informed when the experiment is over. 
\nPress enter when you are ready to begin! Enjoy! 
"""]

for i in intro:
    show_info(i)
    
    
if k == 0:
    person_stories_function()
    topic_function()
else:
    topic_function()
    person_stories_function()

show_info("You will now be asked some final questions")

news_rating = {
    'ID': ID,
    "Nationality": nationality,
    'gender': gender,    
    "topic":"NA",
    "t_story":"NA",
    "n_story":"NA",
    "t_story_rating":"",
    "n_story_rating":"NA",
    "condition":"NA",
    "topic_knowledge":"NA",
    "media_time":"NA",
    "rating_EB":"NA",
    "rating_MX":"NA",
    "rating_politiken":"NA",
    "rating_weekend_a":"NA",
    "block_order":"NA",
    "rt_text":"NA",
    "rt_response":"NA",
    "blue_eyes": "NA",
    "hayfever": "NA", 
    "countryside": "NA", 
    "pets": "NA", 
    "infertility": "NA", 
    "sleep": "NA"
    }
    
    

news_rating["rating_EB"]=rate_newspaper("Ekstra Bladet")
news_rating["rating_MX"]=rate_newspaper("Metro Express")
news_rating["rating_politiken"]=rate_newspaper("Politiken")
news_rating["rating_weekend_a"]=rate_newspaper("Weekend Avisen")
news_rating["media_time"] = rate_media()

pers_char_rating = visual.RatingScale(win, markerColor = "White", scale = "",low = 1, high = 2, labels = ["YES", "NO"])

def pers_char(x):
    full_txt = x
    msg = visual.TextStim(win, text = full_txt, pos=(0,0.1))   
    
    pers_char_rating.reset()
    while pers_char_rating.noResponse: 
        pers_char_rating.draw() 
        msg.draw()
        win.flip()
    return(pers_char_rating.getRating())

news_rating["blue_eyes"]=pers_char("Do you have blue eyes?")
news_rating["hayfever"]=pers_char("Do you have hayfever?")
news_rating["countryside"]=pers_char("Did you grow up on the countryside?")
news_rating["pets"]=pers_char("Did you have pets as a child?")
news_rating["infertility"]=pers_char("Do you keep your iPhone in your pocket?")
news_rating["sleep"]=pers_char("Do you sleep on your stomache?")

writer.write(news_rating)

show_info("All stories presented in this experiment are completely fictitious and was desgined for the puprose of testing a specific hypothesis. \nSo there is no reason to feel anxious about the information you read during the experiment."
show_info("The experiment is now over.\nThank you very much for your participation!")

core.quit()