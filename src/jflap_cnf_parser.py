# parser for CFG in .jff to CNF
from nltk import CFG, Nonterminal, nonterminals, Production, RecursiveDescentParser
import eps
from io import StringIO
import xml.etree.ElementTree as ET
import cyk_parser as parser

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
    #XML parse
    tokens = []
    if language == 1:
        tokens = HTML_parsed(sentence)
    elif language == 2:
        tokens = XML_parsed(sentence)
    elif language == 3:
        tokens = Custom_parsed(sentence)
    else:
        tokens = sentence.lower().split()
    print(tokens)

    parser.parse(tokens)
    return(parser.print_tree())

def HTML_parsed(word):
    word = word.lower().replace('=', '= ').split()
    
    flag_img = False
    word_tokenized = []
    for i in range(len(word)):
        if(flag_img):
            flag_img = False
            continue
        if("<img" in word[i]):
            word_tokenized.append(word[i]+ " " + word[i+1])
            flag_img = True
            continue
        if("alt" in word[i]):
            word_tokenized.append(" "+word[i])
            continue
        if (">" in word[i]) and ("<" not in word[i]):
            word_tokenized = word_tokenized + list(word[i])  
            #flag_img = True
        elif word[i].isalnum():
            word_tokenized = word_tokenized + list(word[i])   
        else:
            word_tokenized.append(word[i])
            
    
    print(word_tokenized)       
    return(word_tokenized)

def XML_parsed(sentence):
    tokens = []
    token_index = 0
    for char in sentence.lower():
        if char == '/' and tokens[token_index-1] == '<':
            tokens[token_index-1] = '</'
            token_index -= 1
        elif char == ' ' or char == '\n':
            continue
        else:
            tokens.append(char)
        token_index += 1
    return tokens

def Custom_parsed(sentence):
    raw_tokens = sentence.lower().split()
    tokens = []
    for token in raw_tokens:
        if token.isalnum():
            tokens = tokens + list(token)
        else:
            tokens.append(token)
            
    return tokens

def load_grammar(grammar_file):
    g0 = CFG_to_string(grammar_file)
    # print(g0)
    g1 = CFG.fromstring(g0)
    
    g1 = eps.remove_all_epsilons(g1)
    
    # for production in g1.productions():
    #     print(production)
    
    c = g1.chomsky_normal_form() # not finishing
    # print("\n Printing productions in CNF...")
    rules = []
    for p in c.productions():  
        # print(p)
        rule = str(p).replace("->", "").split()  
        if rule[0] == 'S':
            temp = rules[0]
            rules[0] = rule
            rule = temp
        rules.append(rule)
    return(parser.Parser(rules))

def load_file(file_name):
    try:
        f = open(file_name, 'r')
    except OSError:
        print("Could not open/read file: \""+file_name+"\"")
        return None
    return "".join(f.read())
