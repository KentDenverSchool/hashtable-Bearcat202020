import unittest
from hashtable import HashTable

class TestHash(unittest.TestCase):


    def test_get(self):

        hash = HashTable(8000)
        hash.put("hello", "there")
        self.assertEqual(hash.get("hello"), "there")

    def test_contains(self):

        hash = HashTable(8000)
        hash.put("hello", "there")
        self.assertTrue(hash.contains("hello"))
        self.assertFalse(hash.contains("goodbye"))

    def test_remove(self):

        hash = HashTable(8000)
        hash.put("hello", "there")
        hash.remove("hello")
        self.assertIsNone(hash.get("hello"), None)
        #no error when removing with empty
        hash.remove("nothing")


if __name__ == "__main__":
    unittest.main()
