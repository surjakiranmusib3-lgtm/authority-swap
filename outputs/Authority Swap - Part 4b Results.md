# Authority Swap v3.6 Part 4b pilot

All five candidates completed the eight development items before any of the 16 acceptance items. Development checked transport, parsing and saved-history assembly only. Gate and ranking calculations use acceptance.

The pilot scheduled 714 logical study requests. Hosted usage was **0.016472289 credits** including development, of which 0.010855681 was acceptance. The highest reserved pilot-stage total observed at batch admission was 5.520410 credits against the 60-credit cap. 2,747 credits before the pilot, matching 2,750 minus the logged 2.999828 Part 3b credits at the dashboard's display precision. Credit coverage verified and the old 3b-1 reservation released. The post-pilot display showed 2,746.983 credits. The displayed debit was 0.017, a difference of 0.000528 from the logged pilot cost. This reconciles within one 0.001-credit display increment.

## Development checks

| Candidate | Items | Baseline parsed | All parsed | Replay integrity | Seconds | Credits |
| --- | --- | --- | --- | --- | --- | --- |
| gemma-4-31b-it | 8 | 16/16 (100.0%) | 64/64 (100.0%) | pass | 91.28 | 0.000725270 |
| qwen2.5-1.5b-instruct | 8 | 16/16 (100.0%) | 34/34 (100.0%) | pass | 16.70 | 0.000000000 |
| qwen3.5-397b | 8 | 16/16 (100.0%) | 64/64 (100.0%) | pass | 98.56 | 0.004524600 |
| qwen3.8-27b | 8 | 16/16 (100.0%) | 52/52 (100.0%) | pass | 72.53 | 0.000366738 |
| smollm2-1.7b-instruct | 8 | 16/16 (100.0%) | 28/28 (100.0%) | pass | 15.02 | 0.000000000 |

## Acceptance gates

| Candidate | Eligible | Projected eligible | Parsed | Core complete | Integrity | Floor | Ceiling | Feasibility | Gate failures |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| gemma-4-31b-it | 15/16 (93.8%) pass | 81.78 pass | 118/122 (96.7%) pass | 13/15 (86.7%) FAIL | pass | 1 distinct switchers; FAIL | 1/0/0/0 of 13; pass | pass | completeness, floor |
| qwen2.5-1.5b-instruct | 4/16 (25.0%) FAIL | 26.22 FAIL | 56/56 (100.0%) pass | 4/4 (100.0%) pass | pass | 0 distinct switchers; FAIL | 0/0/0/0 of 4; pass | pass | eligibility, floor, projection |
| qwen3.5-397b | 15/16 (93.8%) pass | 81.78 pass | 122/122 (100.0%) pass | 15/15 (100.0%) pass | pass | 1 distinct switchers; FAIL | 1/0/1/0 of 15; pass | pass | floor |
| qwen3.8-27b | 14/16 (87.5%) pass | 75.28 pass | 116/116 (100.0%) pass | 14/14 (100.0%) pass | pass | 0 distinct switchers; FAIL | 0/0/0/0 of 14; pass | pass | floor |
| smollm2-1.7b-instruct | 4/16 (25.0%) FAIL | 22.94 FAIL | 56/56 (100.0%) pass | 4/4 (100.0%) pass | pass | 2 distinct switchers; pass | 2/2/2/2 of 4; pass | pass | eligibility, projection |

Ceiling numerators are expert assertive, expert tentative, ordinary assertive, ordinary tentative. The denominator is items complete across the original five branches. A zero denominator cannot pass. Parse counts include bare. The next table separately reports bare usability over the eligible set and false switching over its own usable responses. Variance is the sample variance of the complete question-level paired expert-minus-ordinary differences.

| Candidate | Eligible easy/medium/hard | Eligibility Wilson 95% | Projected complete | Core parsed | Bare usable | Bare wrong | Bare abstain | Neutral wrong | Paired variance | Complete N |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| gemma-4-31b-it | 3/8/4 | 71.7%–98.9% | 70.87 | 103/107 (96.3%) | 15/15 (100.0%) | 0/15 (0.0%) | 0 | 0/13 (0.0%) | 0.019231 | 13 |
| qwen2.5-1.5b-instruct | 1/1/2 | 10.2%–49.5% | 26.22 | 52/52 (100.0%) | 4/4 (100.0%) | 0/4 (0.0%) | 4 | 0/4 (0.0%) | 0.000000 | 4 |
| qwen3.5-397b | 3/8/4 | 71.7%–98.9% | 81.78 | 107/107 (100.0%) | 15/15 (100.0%) | 1/15 (6.7%) | 0 | 0/15 (0.0%) | 0.000000 | 15 |
| qwen3.8-27b | 3/8/3 | 64.0%–96.5% | 75.28 | 102/102 (100.0%) | 14/14 (100.0%) | 0/14 (0.0%) | 0 | 0/14 (0.0%) | 0.000000 | 14 |
| smollm2-1.7b-instruct | 1/2/1 | 10.2%–49.5% | 22.94 | 52/52 (100.0%) | 4/4 (100.0%) | 2/4 (50.0%) | 0 | 2/4 (50.0%) | 0.000000 | 4 |

## Throughput and feasibility

Acceptance throughput includes observed pacing and any wait within requests. Projections assume all 85 baseline pairs, six follow-ups on projected eligible items, and duplicate the measured request time for the one-retry allowance. Each planned hosted batch remains subject to the full reservation rule. The projected credits column is the no-retry planning estimate.

| Candidate | Acceptance logical requests | Attempts | Requests/min | Median seconds | Measured credits | Projected main credits | Projected main minutes with retry allowance |
| --- | --- | --- | --- | --- | --- | --- | --- |
| gemma-4-31b-it | 122 | 122 | 41.13 | 1.375 | 0.001444380 | 0.007821752 | 32.13 |
| qwen2.5-1.5b-instruct | 56 | 56 | 137.50 | 0.336 | 0.000000000 | 0.000000000 | 4.76 |
| qwen3.5-397b | 122 | 122 | 41.32 | 1.391 | 0.008592500 | 0.046530970 | 31.98 |
| qwen3.8-27b | 116 | 116 | 41.96 | 1.391 | 0.000818801 | 0.004388115 | 29.63 |
| smollm2-1.7b-instruct | 56 | 56 | 138.29 | 0.328 | 0.000000000 | 0.000000000 | 4.45 |

## Focal ranking and Part 5 recommendation

| Eligibility/parse fallback order | Candidate | Eligible | Parse rate | Class |
| --- | --- | --- | --- | --- |
| 1 | qwen3.5-397b | 15/16 | 122/122 (100.0%) | descriptive-only eligible |
| 2 | gemma-4-31b-it | 15/16 | 118/122 (96.7%) | failed other gates |
| 3 | qwen3.8-27b | 14/16 | 116/116 (100.0%) | descriptive-only eligible |
| 4 | qwen2.5-1.5b-instruct | 4/16 | 56/56 (100.0%) | failed other gates |
| 5 | smollm2-1.7b-instruct | 4/16 | 56/56 (100.0%) | failed other gates |

**No focal model.** No candidate passed all gates. The fallback ranks feasibility- and integrity-compatible candidates by eligibility, parsing, cost, then ID. Any main results are descriptive.

Recommended main configurations, pending explicit Part 5 authorization: qwen3.5-397b (DESCRIPTIVE-ONLY), gemma-4-31b-it (DESCRIPTIVE-ONLY), qwen3.8-27b (DESCRIPTIVE-ONLY).

The current pilot gates use a small curated bank. A model selected on eligibility may have benefited from sampling variability. The paired variance is conditional on eligible complete items and is planning evidence with substantial uncertainty. Model populations can differ in the main. No main, optional reasoning or submission action ran. No human spot-check was performed.
