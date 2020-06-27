#---------------------------------

# to run test cases command "python3 -m pytest -v"
# to run test cases for perticular word run command "python3 -m pytest -k great -v"
# to run marker code only run command "python3 -m pytest -m others -v"

#---------------------------------

#---------------------------------
#import math

#def test_sqrt():
#   num = 25
#  assert math.sqrt(num) == 5
#
#def test_square():
#   num = 7
#   assert 7*7 == 40
#---------------------------------

import pytest
import math

@pytest.mark.square
def test_sqrt():
   num = 25
   assert math.sqrt(num) == 5

@pytest.mark.square
def testsquare():
   num = 7
   assert 7*7 == 40

@pytest.mark.others
def test_equality():
   assert 10 == 11