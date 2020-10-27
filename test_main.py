import numpy as np
import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_for_array(self) :
       for var in globals() :
         self.assertFalse( var is np.ndarray, "You have declared an array in your program" )
