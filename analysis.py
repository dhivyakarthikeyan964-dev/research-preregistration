"""Small, reusable validation and cleaning functions for the preregistered study."""
from __future__ import annotations

import pandas as pd

REQUIRED_COLUMNS = ["study_hours", "exam_score"]


def validate_columns(data: pd.DataFrame) -> None:
    """Raise ValueError if required analysis columns are missing."""
    missing = [column for column in REQUIRED_COLUMNS if column not in data.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")


def clean_data(data: pd.DataFrame) -> tuple[pd.DataFrame, dict[str, int]]:
    """Clean a copy and return (eligible rows, exclusion counts).

    Rows with missing/non-numeric values or impossible ranges are excluded.
    Original input data is never modified.
    """
    validate_columns(data)
    cleaned = data[REQUIRED_COLUMNS].copy()
    before = len(cleaned)

    for column in REQUIRED_COLUMNS:
        cleaned[column] = pd.to_numeric(cleaned[column], errors="coerce")

    missing_mask = cleaned[REQUIRED_COLUMNS].isna().any(axis=1)
    missing_count = int(missing_mask.sum())
    cleaned = cleaned.loc[~missing_mask].copy()

    invalid_mask = (
        (cleaned["study_hours"] < 0)
        | (cleaned["exam_score"] < 0)
        | (cleaned["exam_score"] > 100)
    )
    invalid_count = int(invalid_mask.sum())
    cleaned = cleaned.loc[~invalid_mask].reset_index(drop=True)

    counts = {
        "rows_before": int(before),
        "excluded_missing_or_non_numeric": missing_count,
        "excluded_impossible_values": invalid_count,
        "rows_after": int(len(cleaned)),
    }
    return cleaned, counts
