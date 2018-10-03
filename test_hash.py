import unittest
from hashtable import HashTable

class TestHash(unittest.TestCase):


    def test_get(self):

        hash = HashTable(8000)
        hash.put("hello", "there")
        hash.put("test", "two")
        hash.put("another", "test")
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

    def test_hashCode(self):

        hash = HashTable(8000)
        self.assertEqual(hash.hashCode("hello"), 1881)

if __name__ == "__main__":
    unittest.main()
