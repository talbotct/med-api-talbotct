import unittest
import medAPI

# Unit test format based on: https://www.youtube.com/watch?v=6tNS--WetLI&ab_channel=CoreySchafer

class TestmedAPI(unittest.TestCase):

    def test_patientPost(self):
        correctData = [11111,"Timmy Test","TestHospital",11,111,11,111,11,111,11]
        results = medAPI.wordCount("words.txt")

        self.assertDictEqual(results, correctData)

    def test_noFileName(self):
        noName = "noFile"

        results = medAPI.prepText("")

        self.assertEqual(results, noName)

    def test_emptyFile(self):
        emp = []

        results = medAPI.prepText("empty.txt")

        self.assertEqual(results, emp)

    def test_fileType(self):
        fType = "formatBad"

        results = word_analyzer.prepText("excel.csv")

        self.assertEqual(results, fType)

if __name__ == "__main__":
    unittest.main()