#---------------------------------
#def test_greater():
#   num = 100
#  assert num > 100

#def test_greater_equal():
#   num = 100
#   assert num >= 100

#def test_less():
#   num = 100
#   assert num < 200
#---------------------------------

## to run marker code only used "python3 -m pytest -m others -v"
#import pytest
#@pytest.mark.great
#def test_greater():
#  num = 100
#  assert num > 100
#
#@pytest.mark.great
#def test_greater_equal():
#  num = 100
#  assert num >= 100
#
#@pytest.mark.others
#def test_less():
#  num = 100
#  assert num < 200

#---------------------------------

import pytest
@pytest.mark.xfail
@pytest.mark.great
def test_greater():
   num = 100
   assert num > 100

@pytest.mark.xfail
@pytest.mark.great
def test_greater_equal():
   num = 100
   assert num >= 100

@pytest.mark.skip
@pytest.mark.others
def test_less():
   num = 100
   assert num < 200