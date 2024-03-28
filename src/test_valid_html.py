# usage: python3 -m unittest -v test_valid_in

import jflap_cnf_parser as jcp
'''
@pytest.mark.parametrize("input, accepted", [
    ("(ab?c)*","<class 'finalwa.FA'>"),
    ("(^a)*(b(hola(hi)+hel*lo)d(012?3)+)*glue?(adios*)$", "<class 'finalwa.FA'>"),
    ("(a*(bd(012?3)+)*glue)", "<class 'finalwa.FA'>"),
    (")(j)", "<class 'NoneType'>"),
    ("@hola*(adios)", "<class 'NoneType'>"),
    ("x+", "<class 'finalwa.FA'>"),
    ("((no)", "<class 'NoneType'>"),
    ("((^a)*(b(hola(hi)+hel*lo)d(012?3)+)*glue?(adios*)$)*", "<class 'finalwa.FA'>"),
    
    ])  '''
def test_valid_word():
    # tuve que quitar static de load regex y hacerlo function en vez de method
    #assert (str(type(fw.load_regex(input))) == str(accepted))
    
    # Assert that the connection is added correctly
    assert(jcp.word_accept("<html><head> <title> z </title> </head><body> <br> z </br> </body></html>") > 0)
    assert(jcp.word_accept("<html><head> <title> </title> </head><body>  </body></html>") > 0)
    assert(jcp.word_accept("<html><head> <title> z </title> </head><body> </body></html>") > 0)
    assert(jcp.word_accept("<html><head> <title> z </title> </head><body> <br>  </br> z </body></html>") > 0)
    assert(jcp.word_accept("<html><head> <title> z </title> </head><body> <br> z </br> <hr> z </hr> <br> z </br> </body></html>") > 0)
    assert(jcp.word_accept("<html><head> <title> z </title> </head><body> <br> z </br> <hr> z </hr> <br> </br> z </body></html>") > 0)
    assert(jcp.word_accept("<html><head> <title> z </title> </head><body> z <br> </br> </body></html>") > 0)
    #assert(jcp.word_accept("<html><head> <title> z </title> </head><body> z z </body></html>") > 0)
    
    C -> T