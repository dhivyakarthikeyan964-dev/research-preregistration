# Analysis Preregistration

**Project:** Study Habits and Student Academic Performance  
**Version:** 1.0  
**Plan status:** Drafted before analysis of real outcome patterns  
**Date:** 2026-10-21  
**Author:** Dhivya  
**Important:** Update the author/date if needed before publishing. Save and commit this document before inspecting the association in real data.

## 1. Research question
Among students represented in a suitable student-level dataset, is daily study time associated with exam score?

This is an observational association question. It does not claim that additional study time causes higher scores.

## 2. Population
Students represented by the chosen dataset who have a defined daily study-hours measure and an exam score on a 0–100 scale. The target population is limited to the population and collection process described by the dataset; results will not automatically generalize to all students.

## 3. Exposure and comparator
- **Primary exposure:** Daily study hours, analysed as a continuous numeric variable.
- **Descriptive comparator:** Students reporting fewer than 2 hours per day versus students reporting 2 or more hours per day.
- The 2-hour threshold is a descriptive grouping rule, not a claim that 2 hours is a scientifically established cut-off.

## 4. Outcome and observation window
- **Primary outcome:** Exam score, from 0 to 100.
- **Observation window:** The study/exam period defined in the source dataset. The exact dates and measurement definitions will be recorded after selecting the dataset, before outcome-pattern analysis.
- If the dataset does not define study hours or exam score comparably, it will not be used for this question.

## 5. Hypotheses
- **Null hypothesis (H0):** There is no linear association between daily study hours and exam score in the analysis population (population correlation equals 0).
- **Alternative hypothesis (H1):** There is a non-zero linear association between daily study hours and exam score (population correlation differs from 0).
- Directional expectation: a positive association is plausible, but the primary test remains two-sided.

## 6. Eligibility and exclusions
Include records that:
1. Represent one eligible student/observation under the dataset documentation.
2. Have interpretable daily study hours and exam score values.
3. Have study hours >= 0 and exam score between 0 and 100 inclusive.

Exclude records that:
1. Have missing or non-numeric primary exposure or outcome values from the primary complete-case analysis.
2. Have impossible values (study hours < 0 or exam score outside 0–100).
3. Are documented duplicate records under the source's identifiers or data dictionary.

Do not exclude records solely because they weaken, reverse, or fail to support the hypothesis. Report counts and reasons for all exclusions. If duplicate identification is impossible, do not guess; disclose this limitation.

## 7. Data handling and transformations
1. Preserve the original source file unchanged in `data/raw/`.
2. Create an analysis-ready copy in `data/processed/`.
3. Convert the two analysis columns to numeric types using documented rules; values that cannot be parsed are treated as missing and counted.
4. Apply the eligibility and exclusion rules above.
5. Do not impute missing primary exposure/outcome values for the primary analysis.
6. Do not winsorize, trim, or remove statistical outliers in the primary analysis unless they meet a predeclared impossible-value or duplicate rule.
7. Do not standardize the primary variables for the main analysis; use hours and score in their original units.

## 8. Primary analysis
1. Report sample size, missingness, exclusions, mean, standard deviation, median, and interquartile range for study hours and exam score.
2. Calculate Pearson's correlation coefficient between study hours and exam score.
3. Report a two-sided p-value and a 95% confidence interval for the correlation if supported by the chosen statistical implementation.
4. Use alpha = 0.05 as a descriptive inferential threshold. Report the effect estimate and uncertainty regardless of statistical significance.
5. Plot a scatter plot with a fitted linear trend as a descriptive visualization; do not treat visual inspection as a replacement for the predeclared test.

## 9. Secondary descriptive comparison
Compare exam scores between:
- Group A: study hours < 2 per day
- Group B: study hours >= 2 per day

Report group sample sizes, means, mean difference (B minus A), and a 95% confidence interval if implemented. Use Welch's two-sample t-test for the group comparison. Treat this as secondary and interpret cautiously.

## 10. Robustness checks
- Calculate Spearman's rank correlation as a robustness check for a monotonic association.
- Repeat the primary correlation after excluding only records already identified by the predeclared impossible-value rules; the primary cleaned dataset should already have those records removed, so report this as a validation check rather than a new discretionary exclusion.
- If sample size permits, report whether results are materially changed by missing-data patterns, without inventing values or changing the primary complete-case analysis.
- Clearly distinguish planned checks from any post-hoc exploration.

## 11. Synthetic pipeline check
Before real-data outcome inspection, run the tests in `tests/test_pipeline.py`. The fixture is synthetic and tests input validation, output columns, and exclusion behavior only. It must not be used to support or reject H0/H1.

## 12. Reporting and deviations
Report:
- dataset source, licence/terms, access date, population, measurement definitions, and observation window;
- row counts before and after each exclusion;
- missing values and their handling;
- all planned effect estimates, confidence intervals, p-values, and sample sizes;
- assumptions, limitations, and any deviations from this plan.

Any change made after inspecting outcome patterns must be timestamped and explained. Label analyses that were not specified here as exploratory.

## 13. Decision rule
The primary analysis will be interpreted using the estimated Pearson correlation, its 95% confidence interval, and two-sided p-value. Statistical significance alone will not be treated as evidence of causation or practical importance.

## 14. Preregistration integrity
This document is a plan, not a results report. Commit it to version control before examining the relationship between real study hours and exam scores. If the dataset has already been inspected for outcome patterns, transparently label the plan as retrospective rather than claiming it was preregistered in advance.
