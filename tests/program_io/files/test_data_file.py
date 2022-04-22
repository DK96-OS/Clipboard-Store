""" Testing FileIO """
import unittest

from program_io.files import data_file

class TestDataFile(unittest.TestCase):
    """  """

    def testSaveAndLoadSimpleData(self):
        """  """
        self.simpleDataDict = {"1" : "A"}
        # Save to File
        data_file.save(self.simpleDataDict)
        # Get from File and compare
        self.assertDictEqual(
            self.simpleDataDict,
            data_file.load()
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
        data_file.save(self.largeDataDict)
        # Get from File and compare
        self.assertDictEqual(
            self.largeDataDict,
            data_file.load()
        )
