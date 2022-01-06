import unittest

from label import *

class TestLabelStorageList(unittest.TestCase):

    def test_label_list(self):        
        output = list_buckets_by_label( {'environment':'staging'})
        print( output )
        # is array 
        self.assertIsNotNone( output )

    
if __name__ == '__main__':
    unittest.main()
    