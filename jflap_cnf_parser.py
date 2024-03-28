# parser for CFG in .jff to CNF
from nltk import CFG

from io import StringIO
import xml.etree.ElementTree as ET


def CFG_to_string():
    gg = ""
    tree = ET.parse("html.jff")
    root = tree.getroot()
    
    counter_new_rules = 0
    for child in root:
        
        # array mapping mixed rules
        temp_rule = []
        for i in range(len(child)):
            c2 = child[i]
            
            if(c2.tag == "left"):
                temp_rule.append(c2.text)
                
            if(c2.tag == "right"):
                temp = str(c2.text).split("\"")
                for i in range(len(temp)):
                    if(len(temp[i]) > 2):
                        # add new name to array
                        temp_rule.append("L"+str(counter_new_rules)) 
                        
                        # create new rule with just one terminal
                        gg += "L"+str(counter_new_rules) + " -> " + "'" + str(temp[i]) + "'" + "\n"
                        
                        # counts amount of new rules created
                        counter_new_rules += 1
                    else:
                        temp_rule.append(temp[i])
                gg += str(temp_rule[0]) + " -> "
                
                for i in range(1, len(temp_rule)):
                    gg += str(temp_rule[i]) + " "
                gg += "\n"
                
                temp_rule = []
                
    return(gg)
  
g1 = CFG.fromstring(CFG_to_string())
print("Transforming CFG to CNF")
# transform to CNF
c = g1.chomsky_normal_form()
            
print("Printing productions in CNF...")
for p in c.productions():           
    print(p)         
