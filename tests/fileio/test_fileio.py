""" Testing FileIO """
import unittest

from fileio.fileio import load, save

class TestFileIO(unittest.TestCase):
    """  """

    def testSaveAndLoadSimpleData(self):
        """  """
        self.simpleDataDict = {"1" : "A"}
        # Save to File
        save(self.simpleDataDict)
        # Get from File and compare
        self.assertDictEqual(
            self.simpleDataDict,
            load()
        )

    def testSaveAndLoadLargerData(self):
        """  """
        self.maxDiff = 4000
        self.largeDataDict = {}
        for i in range(1500):
            number = round((i)**2 + i * 30 + 1.27**i)
            # Use String Key because Load method uses String
            key = str(i)
            self.largeDataDict[key] = number
        # Save to File
        save(self.largeDataDict)
        # Get from File and compare
        self.assertDictEqual(
            self.largeDataDict,
            load()
        )
