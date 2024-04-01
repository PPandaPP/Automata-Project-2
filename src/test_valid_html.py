# usage: python3 -m unittest -v test_valid_in

import jflap_cnf_parser as jcp
import pytest

@pytest.fixture
def parser():
    grammar_file = "HTML/html.jff"
    return jcp.load_grammar(grammar_file)

@pytest.mark.parametrize("input",
                         [
                            "<html> <head> <title> z </title> </head> <body> <br> z </br> </body> </html>",
                            "<html> <head> <title> </title> </head> <body>  </body> </html>",
                            "<html> <head> <title> z </title> </head> <body> </body> </html>",
                            "<html> <head> <title> z </title> </head> <body> <br>  </br> z </body> </html>",
                            "<html> <head> <title> z </title> </head> <body> <br> z </br> <hr> z </hr> <br> z </br> </body> </html>",
                            "<html> <head> <title> z </title> </head> <body> <br> z </br> <hr> z </hr> <br> </br> z </body> </html>",
                            "<html> <head> <title> z </title> </head> <body> z <br> </br> </body> </html>",
                            "<html> <head> <title> z </title> </head> <body> z z </body> </html>",
                            "<html> <head> <title> </title> </head> <body> <div> <h1> 0 a b C 5 6 </h1> </div> </body> </html>"
                         ])
def test_valid_word(parser, input):
    # Assert that the connection is added correctly
    assert jcp.word_accept(parser, input, 1) == True
