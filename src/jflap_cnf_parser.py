# parser for CFG in .jff to CNF
from nltk import CFG, Nonterminal, nonterminals, Production, RecursiveDescentParser

from io import StringIO
import xml.etree.ElementTree as ET


def CFG_to_string():
    gg = ""
    temp_gg = ""
    tree = ET.parse("html2.jff")
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
                
                    if(len(temp[i]) > 0 and not temp[i].isupper()):
                        temp_rule.append("L"+ str(counter_new_rules)) 
                        
                        # create new rule with just one terminal
                        if(str(temp[i]) == 'None'):
                            temp[i] = ''
                        temp_gg += "L"+ str(counter_new_rules) + " -> " + "'" + str(temp[i]) + "'" + "\n"
                        
                        # counts amount of new rules created
                        counter_new_rules += 1
                    else:
                        temp_rule.append(temp[i])

                gg += str(temp_rule[0]) + " -> "
                for i in range(1, len(temp_rule)):
                    gg += str(temp_rule[i]) + " "
                gg += "\n"
                gg += temp_gg
                
                temp_gg = ""
                temp_rule = []
                
    return(gg)

def word_accept(sentence): 
    g0 = CFG_to_string()
    #print(g0)
    g1 = CFG.fromstring(g0)
    #c = g1.chomsky_normal_form() 
    #print("Printing productions in CNF...")
    for p in g1.productions():           
        print(p)  
        
    rd = RecursiveDescentParser(g1)  
    
    print("Recursion....", sentence)
    count_steps = 0
    for t in rd.parse(sentence):
        print(t)
        count_steps+=1
    
    return(count_steps)

    


#sentence = "<html><head> <title> z </title> </head><body> <br> z </br> </body></html>".lower().split()



# transform to CNF
#print("Transforming CFG to CNF")
# chomsky_normal_form() doesnt deal with empty
#c = g1.chomsky_normal_form() 
            
print("Printing productions in CNF...")
#for p in c.productions():           
    ##print(p)   
    
