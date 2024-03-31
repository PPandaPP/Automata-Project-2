# usage: python3 -m unittest -v test_valid_in

import jflap_cnf_parser as jcp

def test_valid_word():
    # tuve que quitar static de load regex y hacerlo function en vez de method
    #assert (str(type(fw.load_regex(input))) == str(accepted))
    
    # Assert that the connection is added correctly
    # assert(jcp.word_accept("<html> <head> <title> z </title> </head> <body> <br> z </br> </body> </html>") > 0)
    # assert(jcp.word_accept("<html> <head> <title> </title> </head> <body>  </body> </html>") > 0)
    # assert(jcp.word_accept("<html> <head> <title> z </title> </head> <body> </body> </html>") > 0)
    # assert(jcp.word_accept("<html> <head> <title> z </title> </head> <body> <br>  </br> z </body> </html>") > 0)
    # assert(jcp.word_accept("<html> <head> <title> z </title> </head> <body> <br> z </br> <hr> z </hr> <br> z </br> </body> </html>") > 0)
    # assert(jcp.word_accept("<html> <head> <title> z </title> </head> <body> <br> z </br> <hr> z </hr> <br> </br> z </body> </html>") > 0)
    # assert(jcp.word_accept("<html> <head> <title> z </title> </head> <body> z <br> </br> </body> </html>") > 0)
    # assert(jcp.word_accept("<html> <head> <title> z </title> </head> <body> z z </body> </html>") > 0)
    # assert(jcp.word_accept("<html> <head> <title> </title> </head> <body> <div> <h1> 0 a b C 5 6 </h1> </div> </body> </html>") > 0)