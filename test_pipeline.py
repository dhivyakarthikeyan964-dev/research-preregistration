"""Data-blind contract tests using a synthetic in-memory fixture."""
import unittest

import pandas as pd

from src.analysis import clean_data, validate_columns


class TestSyntheticPipeline(unittest.TestCase):
    def setUp(self):
        # Artificial values only; these do not represent real students.
        self.fixture = pd.DataFrame(
            {
                "study_hours": [1.0, 3.0, 2.0, -1.0, None, "not-a-number"],
                "exam_score": [55.0, 80.0, 70.0, 60.0, 90.0, 50.0],
            }
        )

    def test_output_contract_and_exclusions(self):
        cleaned, counts = clean_data(self.fixture)
        self.assertEqual(list(cleaned.columns), ["study_hours", "exam_score"])
        self.assertEqual(len(cleaned), 3)
        self.assertEqual(counts["rows_before"], 6)
        self.assertEqual(counts["excluded_missing_or_non_numeric"], 2)
        self.assertEqual(counts["excluded_impossible_values"], 1)
        self.assertEqual(counts["rows_after"], 3)
        self.assertTrue((cleaned["study_hours"] >= 0).all())
        self.assertTrue(cleaned["exam_score"].between(0, 100).all())

    def test_missing_required_column_fails(self):
        with self.assertRaises(ValueError):
            validate_columns(pd.DataFrame({"study_hours": [1.0]}))

    def test_input_is_not_modified(self):
        original = self.fixture.copy(deep=True)
        clean_data(self.fixture)
        pd.testing.assert_frame_equal(self.fixture, original)


if __name__ == "__main__":
    unittest.main()
