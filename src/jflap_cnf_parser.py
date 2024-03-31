# parser for CFG in .jff to CNF
from nltk import CFG, Nonterminal, nonterminals, Production, RecursiveDescentParser
import eps
from io import StringIO
import xml.etree.ElementTree as ET


def CFG_to_string(grammar_file):
    gg = ""
    temp_gg = ""
    tree = ET.parse(grammar_file)
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
                    if temp[i] == 'None':
                        temp_rule.append("'"+temp[i]+"'")
                    elif(len(temp[i]) > 0 and not temp[i].isupper()):
                        
                        temp_rule.append("L"+ str(counter_new_rules)) 
                        # create new rule with just one terminal
                        temp_gg += "L"+ str(counter_new_rules) + " -> " + "'" + temp[i] + "'" + "\n"
                        # counts amount of new rules created
                        counter_new_rules += 1
                    else:
                        temp_rule.append(temp[i])
                # check invalid
                gg += temp_rule[0] + " -> " + " ".join(temp_rule[1:]) + "\n"
                gg += temp_gg
                
                temp_gg = ""
                temp_rule = []            
    return(gg)

    
def word_accept(parser, sentence, language):   
    
    print("Recursion....")
    count_steps = 0
    # temp_tokens = sentence.lower().split()
    # #HTML parse
    # tokens = []
    # if language == 1:
    #     for t in temp_tokens:
    #         if t.isalnum():


    try:
        for t in parser.parse(sentence.lower().split()):
            print(t)
            count_steps+=1
        if count_steps != 0:
            return True
    except ValueError:
        return(False)

    return(False)

def load_grammar(grammar_file):
    g0 = CFG_to_string(grammar_file)
    # print(g0)
    g1 = CFG.fromstring(g0)
    
    g1 = eps.remove_all_epsilons(g1)
    
    # for production in g1.productions():
    #     print(production)
    
    c = g1.chomsky_normal_form() # not finishing
    # print("\n Printing productions in CNF...")
    # for p in c.productions():           
    #    print(p)  
        
    return(RecursiveDescentParser(c))

def load_file(file_name):
    try:
        f = open(file_name, 'r')
    except OSError:
        print("Could not open/read file: \""+file_name+"\"")
        return None
    return "".join(f.read())