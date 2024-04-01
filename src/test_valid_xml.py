# usage: python3 -m unittest -v test_valid_in

import jflap_cnf_parser as jcp
import pytest

@pytest.fixture
def parser():
    grammar_file = "XML/xml.jff"
    return jcp.load_grammar(grammar_file)

@pytest.mark.parametrize("input",
                         [
                            "<a> </a>",
                            "<abc> <b> 123 </b> </asx>",
                            "<abc> <b> <v> </a> </b> </asx>",
                            "<abc> <b> sdsfds </v> <a> sdsd </b> </asx>",
                            "<abc> 1adv </b> <v> sdsd </a> <b> abc </asx>",
                            "<abc> <b> <n> sdsfds </n> </v> <asd> sdsd </asd> <a> </b> </asx>",
                            "<html> <head> <title> z </title> </head> <body> <br> </br> </body> </html>",
                         ])
def test_valid_word(parser, input):
    # Assert that the connection is added correctly
    assert jcp.word_accept(parser, input, 2) == True