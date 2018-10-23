#Analyzer of projects sb3, the new version Scratch 3.0

import json
from collections import Counter


mastery = {}		#New dict to save punctuation
total_blocks = [] #List with blocks
blocks_dicc = Counter()		#Dict with blocks
 


def open_project(): 

   #Open JSON project
   project = json.loads(open('project.json').read())
   return project



def obtain_dict(project):

  #Obtain the dict with the blocks

  for key, value in project.iteritems():
     if key == "targets":
       for dicc in value:
          for dicc_key, dicc_value in dicc.iteritems():
            if dicc_key == "blocks":
              for blocks, blocks_value in dicc_value.iteritems():
                total_blocks.append(blocks_value)
  
  for block in total_blocks:
    for key, value in block.iteritems():
       if key == "opcode":
          blocks_dicc[value] += 1



"""Run and return the results of Mastery."""
def analyze():
       
     logic(blocks_dicc) 
     flow_control(blocks_dicc)
     synchronization(blocks_dicc)
     #abstraction(blocks_dicc)
     data_representation(blocks_dicc)
     user_interactivity(blocks_dicc)
     #parallelization(scratch)
     
     print mastery



"""Assign the Logic skill result"""
def logic(blocks):

  operations = {'operator_and', 'operator_or', 'operator_not'}
  score = 0
  
  for operation in operations:
     if blocks[operation]:
        score = 3
        mastery["logic"] = score
        return
  
  if blocks['control_if_else']:
     score = 2
  elif blocks['control_if']:
     score = 1
  
  mastery['Logic'] = score
  


"""Assign the Flow Control skill result"""     
def flow_control(blocks):

  score = 0
  
  if blocks['control_repeat_until']:
     score = 3
  elif (blocks['control_repeat'] or blocks['control_forever']):
     score = 2
  else:
     for block in total_blocks:
       for key, value in block.iteritems():
         if key == "next" and value != None:
            score = 1
            break
       
     
  mastery['FlowControl'] = score



"""Assign the Syncronization skill result"""
def synchronization(blocks):
    
   score = 0
   
   if (blocks['control_wait_until'] or
       blocks['event_whenbackdropswitchesto'] or
       blocks['event_broadcastandwait']):
            score = 3
   elif (blocks['event_broadcast'] or 
         blocks['event_whenbroadcastreceived'] or
         blocks['control_stop']):
            score = 2
   elif blocks['control_wait']:
            score = 1
  
   mastery['Synchronization'] = score



"""Assign the Abstraction skill result
def abstraction(blocks):
        
   score = 0
        
   if blocks['control_start_as_clone']:
            score = 3
   elif blocks["define %s"]:
            score = 2
   else:
            scripts = 0
            for script in self.iter_scripts(scratch):
                if self.script_start_type(script) != self.NO_HAT:
                    scripts += 1
                    if scripts > 1:
                        score = 1
                        break
   
   mastery['Abstraction'] = score

"""



"""Assign the Data representation skill result"""
def data_representation(blocks):
        
  score = 0
  
  modifiers = {'motion_movesteps', 'motion_gotoxy', 'motion_glidesecstoxy', 'motion_setx', 'motion_sety', 
               'motion_changexby', 'motion_changeyby', 'motion_pointindirection', 'motion_pointtowards',
               'motion_turnright', 'motion_turnleft', 'motion_goto', 
               'looks_changesizeby', 'looks_setsizeto', 'looks_switchcostumeto', 'looks_nextcostume', 
               'looks_changeeffectby', 'looks_seteffectto', 'looks_show', 'looks_hide', 'looks_switchbackdropto', 
               'looks_nextbackdrop'}

  lists = {'data_lengthoflist', 'data_showlist', 'data_insertatlist', 'data_deleteoflist', 'data_addtolist',
           'data_replaceitemoflist', 'data_listcontainsitem', 'data_hidelist', 'data_itemoflist'}
        
  for item in lists:
    if blocks[item]:
       score = 3
       mastery['DataRepresentation'] = score
       return
  
  if blocks['data_changevariableby'] or blocks['data_setvariableto']:
     score = 2
  else:
    for modifier in modifiers:
       if blocks[modifier]:
          score = 1


  mastery['DataRepresentation'] = score



"""Assign the User Interactivity skill result"""
def user_interactivity(blocks):
        
   score = 0
       
   proficiency = {'turn video %s', 'video %s on %s', 'when %s > %s',
            'set video transparency to %s%%', 'loudness'}
        
   developing = {'event_whenkeypressed', 'event_whenthisspriteclicked', 'sensing_mousedown', 'sensing_keypressed',
                 'sensing_askandwait', 'sensing_answer'}

   for item in proficiency:
      if blocks[item]:
          mastery['UserInteractivity'] = 3
          return
   for item in developing:
      if blocks[item]:
          mastery['UserInteractivity'] = 2
          return
   if blocks['motion_goto_menu']:
      if check_mouse(total_blocks) == 1:
          mastery['UserInteractivity'] = 2
          return
   if blocks['sensing_touchingobjectmenu']:
      if check_mouse(total_blocks) == 1:
          mastery['UserInteractivity'] = 2
          return
   if blocks['event_whenflagclicked']:
       score = 1
    
   mastery['UserInteractivity'] = score



"""Check whether there is a block 'go to mouse' or 'touching mouse-pointer?' """
def check_mouse(total_blocks):

   for block in total_blocks:
     for key, value in block.iteritems():
       if key == 'fields':
         for mouse_key, mouse_val in value.iteritems():
           if (mouse_key == 'TO' or mouse_key =='TOUCHINGOBJECTMENU') and mouse_val[0] == '_mouse_':
                 return 1

   return 0





if __name__ == '__main__':
 project = open_project()
 obtain_dict(project)
 analyze()


