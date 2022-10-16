import unittest
import trainer


class Test_trainer(unittest.TestCase):
    
    def setUp(self):
        self.trainer = trainer.Trainer(self, 0, seed=1)
    
    def tearDown(self):
        pass
    
    def test_seed(self):
        self.assertEqual(self.trainer.get_seed(), 1)
        
        
if __name__ == '__main__':
    unittest.main()