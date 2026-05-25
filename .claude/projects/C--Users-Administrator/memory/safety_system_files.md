---
name: safety-deletion-rules
description: 删除文件的行为规则——走回收站，不永久删除
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 20f01da0-b595-4e4c-b542-f91e2f3e9e1a
---

## 删除规则

1. 删除文件时用回收站方式，不用 `rm` 永久删除
2. 小文件能进回收站的，直接删，不弹窗
3. 文件太大回收站装不下时，弹窗让用户确认
4. 绝不删除或修改 Windows 系统文件（C:\Windows、C:\Program Files 等目录）

**Why:** 用户担心误删后找不回来，回收站可以恢复。

**How to apply:** 删除前先判断大小，能进回收站就直接删；超过的弹窗确认。**绝对不用 `rm -rf` 删用户文件，必须用 PowerShell 回收站方式删除。**（教训：2026-05-24 误永久删除了用户的曙光和百夜幻想文件夹）
