import jflap_cnf_parser as parser
from nltk import CFG, Nonterminal, nonterminals, Production, RecursiveDescentParser

grammar_file = ""

while True:
    print("\nMenu:\n 1. HTML parse\n 2. XML parse\n 3. Custom language parse\n 4. exit\n")
    print("Enter desired option:")
    language = int(input())
    if language == 1:
        grammar_file = "HTML/html.jff"
        grammar_parser = parser.load_grammar(grammar_file)
        while True:
            print("\nMenu:\n 1. Example \n 2. input file \n 3. input from CLI\n 4. exit\n")
            print("Enter desired option:")
            option = int(input())
            if option == 1:
                string = parser.load_file("HTML/HTML example.html")

            elif option == 2:
                print("Please enter the HTML file to be parsed (make sure it is in the HTML folder):")
                file_name = input()
                string = parser.load_file("HTML/"+file_name)
                
            elif option == 3:
                print("Please enter the HTML string to be parsed (make sure there are spaces before and after each tag):")
                string = input()

            elif option == 4:
                break

            else:
                print("ERROR: no such option in menu!\n")
                continue
            
            if string == None:
                continue

            print("\ninput HTML:\n")
            print(string)
            print("\nparse result:\n")

            accepted = parser.word_accept(grammar_parser, string, language)
            
            if accepted:
                print("\nHTML accepted! :D\n")
            else:
                print("\nHTML rejected! :C\n")

    elif language == 2:
        grammar_file = "XML/xml.jff"
        grammar_parser = parser.load_grammar(grammar_file)
        while True:
            print("\nMenu:\n 1. Example \n 2. input file \n 3. input from CLI\n 4. exit\n")
            print("Enter desired option:")
            option = int(input())
            if option == 1:
                string = parser.load_file("XML/XML example.xml")

            elif option == 2:
                print("Please enter the HTML file to be parsed (make sure it is in the XML folder):")
                file_name = input()
                string = parser.load_file("XML/"+file_name)

            elif option == 3:
                print("Please enter the XML string to be parsed (make sure there are spaces before and after each tag):")
                string = input()
            
            elif option == 4:
                break

            else:
                print("ERROR: no such option in menu!\n")
                continue
            
            if string == None:
                continue

            print("\ninput XML:\n")
            print(string)
            print("\nparse result:\n")
            
            accepted = parser.word_accept(grammar_parser, string, language)

            if accepted:
                print("\nXML accepted! :D\n")
            else:
                print("\nXML rejected! :C\n")
    elif language == 3:
        #custom grammar
        print("not yet implemented!")

    elif language == 4:
        print("\nThanks for using this program!\n")
        break

    else:
        print("ERROR: no such option in menu!\n")
        continue
            


        

