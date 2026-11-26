# GPT‑6.2 内容提示词实测

2026 年 11 月 26 日通过 OpenAI Codex CLI（0.170.0）运行。四次运行均使用 `gpt-6.2-sol`，日志里的 reasoning effort 为 `none`。每个用例运行一次，使用独立的临时会话。

每次输入包含任务和打乱顺序的候选 skill 正文。期望的 skill 和验收条件在本地保留，输出返回后逐条核对。模型按评估要求在第一行标注所选 skill，下方引文是该行之后的交付物。用例定义及检查项见 [skill-routing.json](skill-routing.json)。

**4 次均选中预期 skill，12 项验收条件全部通过。** 结果覆盖这四个用例和各自给定的候选范围。

## 1. 教务邮件

`faculty-email-forwarded-recipient` · 所选 skill 为 `faculty-email` · 3/3 通过

正文含称呼和署名共 62 个英文词。未上传手册的收件人可以直接看到提交对象、10 月 2 日的截止日期和认证审查的用途。邮件准确交代了政策状态，也省去了与请求无关的学生个案。

> **Subject: Module handbooks for the October accreditation review**
>
> Dear module convenors,
>
> If you haven’t already uploaded your current module handbook to the review folder, please send it to the School Office by 2 October. We’re checking whether existing handbooks use the updated resit wording for the October accreditation review.
>
> At the accreditation meeting, the committee discussed revising the assessment policy. The current policy remains in effect.
>
> Best wishes,\
> School Office

## 2. 试点摘要

`summary-partial-source-with-consequential-limit` · 所选 skill 为 `summarize-material` · 3/3 通过

三句话保留了共享表单省去合并邮件的机制、两班共 36 份记录，以及从 5 天降至 3 天的中位数。摘要说明同期增派助理限制了归因，第三班资料仍缺失。末句明确把等待完整报告写作建议。

> 《试点简报》第2页显示，两个班的导师使用同一份共享电子表单登记反馈，省去了教务人员合并邮件的步骤。两班共36份记录，处理时间的中位数从5天降至3天，但同期也增派了一位助理，现有材料无法区分两项变化各自的影响。第三个班的数据在未提供的附录中，简报也未给出推广决定，因此建议等完整报告后再决定是否推广。

## 3. 教学奖申报段落

`statement-partially-supported-draft` · 所选 skill 为 `statement-drafter` · 3/3 通过

第一人称段落说明了两场研讨课的参与方式，准确引用 23 名答卷者中有 18 人认为书面选项有帮助，并明确学业成绩的影响未知。段落后的取证建议给出了统一测评、评分标准、基线和可比组。

> I redesigned two seminars to give students a choice in how they shared their solutions. They could post their solutions in writing or explain them aloud. In the year-end report, 18 of 23 respondents said they found the written option helpful, indicating that students valued having this way to participate. The effect on attainment remains unknown because the evaluation included neither an assessment of attainment nor a comparison group.
>
> **Evidence needed for the attainment criterion.** Use a common assessment aligned with the seminars’ learning objectives. To test whether the redesign improved attainment, compare gains from baseline with those of a comparable group taught under the previous format, using the same assessment and scoring criteria for both groups.

## 4. PR 描述

`pr-description-required-template-and-missing-results` · 所选 skill 为 `pr-description` · 3/3 通过

正文按要求只含 Summary、Testing 和 Rollback 三节。重复 ID 行从覆盖变为拒绝的影响、唯一 ID 文件的行为、已通过的 CSV 单元测试、待验证的两项检查以及回滚效果均与输入相符。

> ## Summary
>
> The import command now rejects rows with duplicate IDs. Existing CSV files with duplicate IDs will have those rows rejected where the import previously allowed later rows to overwrite earlier ones. Files with unique IDs continue to import as before.
>
> ## Testing
>
> - CSV import unit tests passed.
> - CLI integration tests and imports of previously accepted customer files remain unverified.
>
> ## Rollback
>
> Revert this change to restore the previous behavior, where later rows with duplicate IDs silently overwrite earlier rows.
