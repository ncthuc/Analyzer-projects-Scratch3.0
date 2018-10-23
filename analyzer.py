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
  
  #print blocks_dicc    



  """Run and return the results from the Mastery plugin."""
def analyze():
       
     logic(blocks_dicc) 
     flow_control(blocks_dicc)
     #self.synchronization(file_blocks)
     #self.abstraction(file_blocks, scratch)
     #self.data(file_blocks)
     #self.user_interactivity(file_blocks, scratch)
     #self.parallelization(scratch)
     
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
  
  mastery["Logic"] = score
  


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


if __name__ == '__main__':
 project = open_project()
 obtain_dict(project)
 analyze()


