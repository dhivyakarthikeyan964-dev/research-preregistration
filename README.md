# Study Habits and Student Academic Performance: Preregistration

A reproducible, preregistered analysis plan for studying the association between daily study hours and exam scores.

## Research question
Among students represented in the selected dataset, is daily study time associated with exam score?

## Important status
This repository contains a **preregistration and a synthetic-data pipeline check**. The synthetic fixture is used only to verify code contracts. It is not evidence for the research hypothesis. No real-data findings are claimed here.

## Repository structure
```text
research-preregistration/
├── preregistration.md
├── README.md
├── requirements.txt
├── environment.yml
├── data/
│   ├── raw/          # Place original data here; do not overwrite it
│   ├── interim/      # Intermediate data products
│   └── processed/    # Analysis-ready data products
├── notebooks/        # Analysis notebook(s)
├── src/
│   └── analysis.py
├── tests/
│   └── test_pipeline.py
└── reports/
    └── report_template.md
```

## Data expectations
When an appropriate dataset is selected, create a CSV with these columns:
- `study_hours`: numeric daily study hours, non-negative
- `exam_score`: numeric score from 0 to 100

Put the original, unmodified file in `data/raw/`. Record the source, access date, licence/terms, and any known limitations in the final report. Do not commit private or identifiable student data.

## Setup (Python)
Create and activate a virtual environment, then install dependencies:

```bash
python -m venv .venv
# Windows PowerShell:
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Run the synthetic pipeline check
```bash
python -m unittest discover -s tests -v
```

The test uses an in-memory synthetic fixture and does not read or inspect any real outcomes.

## Real-data workflow (only after preregistration is saved)
1. Select a suitable, legally usable dataset and document its source.
2. Save the untouched original CSV in `data/raw/`.
3. Check data dictionary, column definitions, units, collection period, and missingness without looking at the relationship between study hours and exam scores.
4. Apply the preregistered exclusions and transformations; save analysis-ready data in `data/processed/`.
5. Run the preregistered analysis and report estimates, uncertainty, limitations, and any deviations.
6. If the plan changes after outcome inspection, record the change and label it exploratory rather than pretending it was preregistered.

## Reproducibility notes
- `requirements.txt` records direct Python dependencies.
- `environment.yml` specifies a Conda environment.
- After installing the environment, generate a platform-specific full lock snapshot if required by the mentor, for example:
  `pip freeze > requirements-lock.txt`
- A generated lock snapshot can differ by operating system and Python version; document the version used.

## Expected proof
- Preregistration document: `preregistration.md`
- Public repository: this project and its commit history
- Environment specification: `requirements.txt`, `environment.yml` (and optionally `requirements-lock.txt`)
- Synthetic pipeline test: `tests/test_pipeline.py`

## Current completion status
- [x] Draft research question and analysis plan
- [x] Repository structure and setup instructions
- [x] Synthetic data pipeline contract test
- [ ] Choose and document a real dataset
- [ ] Run the preregistered analysis on real data
- [ ] Review results and submit the public repository URL
