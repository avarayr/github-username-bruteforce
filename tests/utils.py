import utils
from unittest import TestCase

class Utils(TestCase):
  def setUp(self):
      super().setUp()
  
  def testPermutations(self):
    singleLetterPermutations = utils.get_n_letter_permutations(1)
    assert len(list(singleLetterPermutations)) == 26