import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetectorWithoutMock(unittest.TestCase):
    def test_emotion_detector(self):
        # Define test cases
        test_cases = [
            ("I am glad this happened", "joy"),
            ("I am really mad about this", "anger"),
            ("I feel disgusted just hearing about this", "disgust"),
            ("I am so sad about this", "sadness"),
            ("I am really afraid that this will happen", "fear")
        ]

        # Test each case
        for statement, expected_emotion in test_cases:
            result = emotion_detector(statement)
            dominant_emotion = result.get("dominant_emotion")
            self.assertEqual(dominant_emotion, expected_emotion, f"Failed for statement: {statement}")

if __name__ == '__main__':
    unittest.main()