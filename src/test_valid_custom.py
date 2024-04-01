# usage: python3 -m unittest -v test_valid_in

import jflap_cnf_parser as jcp
import pytest

@pytest.fixture
def parser():
    grammar_file = "Custom/custom.jff"
    return jcp.load_grammar(grammar_file)

@pytest.fixture
def hw():
    return jcp.load_file("Custom/hello world.txt")

@pytest.fixture
def fib():
    return jcp.load_file("Custom/fibonacci.txt")

@pytest.fixture
def sum():
    return jcp.load_file("Custom/sumfunk.txt")

def test_hw(parser,hw):
    assert jcp.word_accept(parser, hw, 3) == True

def test_fib(parser,fib):
    assert jcp.word_accept(parser, fib, 3) == True
    
def test_sum(parser,sum):
    assert jcp.word_accept(parser, sum, 3) == True