# Humanizer bilingual editing check

On 17 November 2026, Antigravity edited eight sample drafts using isolated copies of the two available skills, `humanizer` and `rewrite-for-clarity`. It received the prompts without the expected routes or checks. All eight requests routed to `humanizer`. The passages below are its actual replies, grouped by setting. Each work document shows the result of its final targeted rerun. The prompts and individual checks are in [skill-routing.json](skill-routing.json).

## Email

**Chinese · `humanizer-zh-email-colleague`**

> 周四的演示照常进行。演示要用的两张截图，麻烦你在周三下班前发给我；测试账号我来准备。

**English · `humanizer-en-email-editor`**

> I have attached the revised figure. We also updated the caption to clarify that the bars show the range across runs. The underlying analysis has not changed.

The colleague gets the answer about Thursday before the screenshot request. The editor gets the attachment confirmation and a precise account of the caption change. The bars still represent the range across runs.

## README

**Chinese · `humanizer-zh-readme-preview`**

> 先进入存有 `team.toml` 的目录，再运行 `plan --config team.toml` 预览配置。命令会显示变更清单，预览期间不会写入任何文件。

**English · `humanizer-en-readme-export`**

> First, select the project with `ledger use demo`. Then run `ledger export --format csv` to write `report.csv` in the current directory. If `report.csv` already exists, the export stops without overwriting it.

Both edits put the prerequisite before the command and preserve the literal arguments. The preview remains read-only. The export identifies both the output directory and what happens when the file already exists.

## Work documents

**Chinese · `humanizer-zh-traditional-register`**

> 本次試辦有24位同仁參與。同仁反映「線上申請」的步驟較容易理解，不過系統仍無法儲存尚未送出的資料。資訊組已收到這項問題，但尚未確定修正日期。

**English · `humanizer-en-paragraph-flow`**

> The form was tested for four weeks with 18 members of staff. Median processing time fell from five days to three days during the pilot, though the pilot did not measure whether the gains would last. Several staff could not submit the form from their phones, an issue reported six times.
>
> The team has proposed a second test using mobile devices, but the proposal has not yet been approved. The budget owner will review the request on 14 October. Until a decision is made, the current form remains in use.

An earlier Chinese edit added “普遍” and implied the IT team had taken responsibility for the issue. The rerun keeps the feedback unquantified and says what the team has actually received. In the final English rerun, the timing result and its limit share a sentence. The next sentence introduces the phone issue directly and counts the six reports. That issue leads naturally into the team's proposed mobile test.

## Journal manuscripts

**Chinese · `humanizer-zh-journal-signal`**

> 我们采用周等（2022）的方法对齐了两路信号的时间。处理后，中位时间偏差从18毫秒降至6毫秒。由于这一过程中同时更新了采样时钟的校准参数，仅凭本次比较，无法判断时间偏差的降幅中有多少来自时间对齐，又有多少来自时钟校准。

The citation stays with the alignment method. The drop from 18 to 6 milliseconds is the present study's observation. The final sentence brings in the concurrent calibration change and explains why the comparison cannot separate the two contributions.

**English · `humanizer-en-journal-retrieval`**

> We reranked the results using the procedure of Chen (2021). Between the original and revised systems, mean recall@20 rose from 0.61 to 0.68. Because the revised system also expanded the candidate pool from 100 to 200 documents when reranking was introduced, this comparison cannot isolate the effect of reranking on recall@20.

Chen (2021) is credited for the procedure. The authors' comparison preserves the metric, both values and the change in the candidate pool. The attribution limit follows from that second change. For a final line edit, “Mean recall@20 was 0.61 for the original system and 0.68 for the revised system” pairs each value directly with its system.

The two manuscript cases use invented data and citations. They test editorial continuity and fidelity to the supplied research claims.
