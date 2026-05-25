---
name: feedback-uninstall-to-recycle-bin
description: 卸载软件时先放到回收站，放不下才确认永久删除
metadata: 
  node_type: memory
  type: feedback
  originSessionId: a81dcc9f-4ca4-429e-8c8b-9648d10fcc22
---

卸载软件时，先将文件移动到回收站，不要直接永久删除。如果回收站放不下（文件太大），再询问用户确认是否永久删除。

**Why:** 用户之前明确交代过这个偏好，直接 winget uninstall 跳过了回收站，违反了用户的操作习惯。

**How to apply:** 
1. 删除文件/卸载软件时，先尝试 move 到回收站（用 PowerShell 或资源管理器方式），不要用 rm -rf 或 winget uninstall --silent 直接删除
2. 如果文件太大放不进回收站，再弹出确认询问用户是否永久删除
3. 这也适用于单个文件、文件夹的删除操作

[[feedback_permissions]]
