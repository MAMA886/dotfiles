---
name: github-save-workflow
description: 每次完成写作任务后提醒用户是否存到 GitHub，只存重要内容
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 76daa080-35ed-4749-a3bc-a990e547d5db
---

**规则：** 以后每次我帮你写完东西（代码、文案、脚本、文档等），完成后都要问一句"要不要存到 GitHub？"。你说"存"我才存，你说"不用"或没回应就不存。

**如何判断：** 日常聊天、回答问题不需要提醒。只有产出可保存的内容（文件、代码、文案等）时才提醒。

**如何应用：** 每次 Generate/Write 内容后，检查是否为可保存产出，是则追加提醒。尊重用户选择，不擅自推送。

**相关记忆：** [[user_profile]]
