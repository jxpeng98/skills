# Skill audit follow-up — 2026-09-05

The audit found overlapping writing instructions, contradictory tone constraints,
unavailable sibling-skill routes, thin presentation setup guidance, and structural
checks without recorded behavioral outcomes.

## Plan

1. Clarify writing and meeting routes. Allow requested tone changes while
   preserving facts and commitments; choose one primary editing workflow; handle
   missing sibling skills. Shorten repeated humanizer guidance while retaining
   Chinese registers, academic boundaries, and conditional diagnostics.
2. Complete presentation setup and fallback guidance. Cover new PPTX and Beamer
   projects, editable output, missing tools, and unavailable rendering through one
   conditional reference. Keep existing names and standalone skill installation.
3. Add realistic cases with available skills, expected routes, and behavioral
   checks. Validate case structure with the existing validator; run independent
   forward checks without giving evaluators expected answers. Run repository
   tests in release CI, sync the Hermes mirror, and check packaged resources.

## Acceptance

- [x] Writing requests can change tone without inventing facts or promises.
- [x] Mixed requests select one primary workflow; unavailable siblings do not block work.
- [x] Brief summaries and accountable meeting records follow different output contracts.
- [x] PPTX/Beamer guidance covers new projects and distinguishes produced from verified artifacts.
- [x] Behavioral cases have recorded outcomes distinct from structural validation.
- [x] Skill validation, repository tests, mirror checks, and archive checks pass.

Keep all 20 public skill names and plugin boundaries. Moving `repo-boundary-review`
remains conditional on evidence about reuse. This change does not publish a release
or add a model-evaluation framework or runtime dependency.

## Execution record

Initial audit implementation against baseline `2ad2bf1`: humanizer's entrypoint shrank from 75 to
45 lines; its entrypoint and references together shrank from 302 to 237 lines.
Chinese register guidance remains self-contained. Presentation setup uses one
conditional reference, copied into the generated Hermes mirror. Release CI now
runs the repository tests before packaging.

Validation completed:

- `python3 -B scripts/validate_plugins.py`: passed, including 60 routing prompts
  and the structure of 13 behavioral scenarios.
- `python3 -B -m unittest discover -s tests -v`: all 6 tests passed. The new test
  accepts a valid scenario and rejects unavailable routes, unknown or malformed
  skill entries, blank prompts, and empty checks.
- `python3 -B scripts/sync_hermes_tap.py --check` and `git diff --check`: passed.
- `skill-creator/scripts/quick_validate.py`: all 6 changed skills passed using
  an existing Python environment with PyYAML. Default interpreters lacked PyYAML;
  no dependency was installed or added to the repository.
- Release workflow YAML parsed successfully; the test step precedes packaging.
- Temporary packaging: all 11 archive checksums and archive integrity checks
  passed. Extracted files matched canonical sources, including the new reference.

## Independent behavior checks

Three fresh agents executed writing, meeting/summary, and presentation case groups
in isolated temporary directories. They received neutral case IDs, prompts, the
specified available skills, and their resources. Expected routes and behavioral
checks were withheld. The primary agent compared actual responses with the
checks in `evals/skill-routing.json`; all 13 selected routes matched, and all
13 responses passed manual semantic assessment.

| Scenario | Actual primary skill | Observed response evidence | Result |
| --- | --- | --- | --- |
| clarity-requested-tone | rewrite-for-clarity | Added a polite greeting; kept September 10 as an estimate and the result unresolved; two sentences. | Pass |
| clarity-requested-firmness | rewrite-for-clarity | Used "Please send"; preserved Friday and the unapproved extension without penalties. | Pass |
| humanizer-mixed-request | humanizer | Returned one Chinese revision preserving 5 to 3 days, 12 cases, and the unknown long-term effect; no secondary skill. | Pass |
| humanizer-assessed-work | humanizer | Gave a targeted revision and reasons; preserved six of ten interviews and the causal limit; left the comparison evidence for the author to verify. | Pass |
| humanizer-without-sibling | humanizer | Completed the shorter, friendlier edit while keeping Friday and the unapproved extension; loaded no unavailable sibling. | Pass |
| meeting-brief-summary | summarize-material | Returned two sentences covering the hours decision, unapproved budget, and Li's September 12 task; no action table. | Pass |
| meeting-accountable-record | meeting-synthesizer | Kept the October pilot pending approval and Chen's September 18 task; did not assign the unexplained September 20 date. | Pass |
| meeting-writing-only-install | summarize-material | Produced the action record itself; cancellation remained unvoted and Zhao's deadline remained unknown. | Pass |
| meeting-without-summary-sibling | meeting-synthesizer | Returned one sentence preserving the approved hours change and unknown start date; no action table. | Pass |
| summary-missing-source | summarize-material | Asked for the report and did not invent three conclusions. | Pass |
| presentation-editable-from-slidev | presentation-tool | Planned native text and charts with underlying data; rejected slide-image export for the requested editability; created no files. | Pass |
| presentation-new-beamer-no-engine | presentation-tool | Offered Beamer source, CJK/font setup, notes, and build instructions; explicitly marked the PDF incomplete. | Pass |
| presentation-new-pptx-no-renderer | presentation-tool | Chose installed python-pptx for a new deck; separated structural checks from unverified rendered layout. | Pass |

These are single forward executions with bounded candidate sets, not measured
production routing accuracy. The presentation cases exercised preflight decisions;
no PPTX or Beamer artifact was generated or visually inspected. Hosted CI and
native platform installation were not run. No release was published.

## Humanizer follow-up: English and Chinese prose flow

The subsequent request prioritised faithful, idiomatic, well-composed prose in
both languages, with coherent reasoning and natural transitions. The shared
信、达、雅 priority now lives in `humanizer/SKILL.md`, applies to every output
language, and explicitly protects qualifications and relationships between claims.
The entrypoint is now 63 lines; the additional detail has a specific behavioral
purpose rather than restoring generic style advice.

- Added an English reference for register, collocations, regional consistency,
  sentence movement, pronouns, paragraph continuity, and useful transitions.
- Expanded Chinese guidance for omitted subjects, stable terminology, topic
  changes, real contrasts and causes, and natural sentence rhythm.
- Extended the existing diagnostics to distinguish addition, contrast, cause,
  sequence, and topic change. Unsupported premises and ambiguous references need
  an author decision; a connector cannot supply missing evidence.
- Kept examples and checks that preserve necessary connectors and already natural
  wording. No word blacklist, connector quota, or fixed sentence pattern was added.

Ten new scenarios were added to `evals/skill-routing.json`. Fresh agents received
only prompts, candidate skills, and the current skill resources. Six cases used
English output (including translation and unresolved reasoning) and four used
Chinese output. A third fresh agent reran five existing editing/routing cases.
The primary agent manually checked responses against the withheld requirements;
all 15 routes and responses passed for these cases.

| New scenario | Observed response evidence | Result |
| --- | --- | --- |
| humanizer-en-paragraph-flow | Kept two paragraphs, all pilot figures, six issue reports, and pending approval; removed the false consequence and retained the real limitation. | Pass |
| humanizer-en-needed-connectors | Preserved the already natural notice, including `Because`, `but`, and British spelling. | Pass |
| humanizer-en-topic-shift | Grouped opening hours and printer funding separately; retained both dates, £900, and unapproved funding. | Pass |
| humanizer-en-academic-flow | Connected the finding and methodological limits; retained 40/23, the quotation, citation, voluntary participation, and absent baseline. | Pass |
| humanizer-zh-notice-flow | Removed artificial signposting while retaining the usual 3–5 working days, email notification, and request not to resubmit. | Pass |
| humanizer-zh-topic-shift | Separated application progress from training; retained 36 checked, four pending, intranet instructions, September 15, and 10 a.m. | Pass |
| humanizer-zh-needed-connectors | Kept the notice unchanged, including the maintenance reason, online-service contrast, and unspecified reopening time. | Pass |
| humanizer-zh-traditional-register | Retained Traditional Chinese, 24 participants, 「線上申請」, the unsaved-draft limitation, and unknown fix date. | Pass |
| humanizer-zh-to-en-flow | Produced a direct English notice preserving Wednesday at 3 p.m., maintenance, unaffected applications, unknown reopening, and the course office. | Pass |
| humanizer-unresolved-links | Flagged the ambiguous requester and unsupported cost inference without inventing a bridge or silently changing the conclusion. | Pass |

The five regression cases covered requested friendliness, requested firmness,
mixed humanizing/shortening, assessed-work coaching, and a missing sibling skill.
Their existing requirements still held. These are manually assessed examples,
not a guarantee of all future writing quality or measured improvement over a
control group. The other eight earlier scenarios were not rerun in this follow-up.

Fresh structural checks passed: 23 scenario definitions and 60 routing prompts,
all 6 repository tests, the humanizer quick validator, Hermes mirror parity, and
whitespace checks. All 11 archive integrity/checksum checks passed, and the
extracted writing plugin included the new English reference with source parity.
No runtime dependency, publishing action, or scheduled automation was added.

For future refinements, add a concrete failing draft with its protected meaning
and observable prose requirements, then rerun the relevant cases. Use the result
to correct a specific rule rather than accumulating forbidden words.
