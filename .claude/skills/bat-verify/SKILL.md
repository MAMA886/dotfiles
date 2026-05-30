---
name: bat-verify
description: 创建 bat 前先云端模拟验证。每次需要创建 .bat 批处理脚本时自动触发，模拟执行环境确保能跑通再创建。DeepSeek V4 Pro 必用 skill。
---

# Bat 验证技能

每次创建 .bat 文件之前，必须先在云端模拟验证，确认能跑通再创建文件。绝不能不验证直接创建。

## 触发条件

- 创建任何 `.bat` / `.cmd` 批处理脚本
- 修改现有 bat 的关键逻辑
- 用户说"帮我写个脚本""创建个快捷方式"等

## 执行流程

### 1. 分析 bat 里的依赖

检查 bat 里每条命令：
- `python` 路径是否写死绝对路径？桌面双击时 PATH 不一定有 python
- `taskkill`、`timeout`、`start` 等 Windows 原生命令 — 只在 Windows cmd 里有效
- `curl` — 是 Git Bash 的还是 PowerShell 的？用 `python -c "import urllib.request..."` 更靠谱
- 文件路径 — 用正斜杠还是反斜杠？Windows 用 `C:\xxx` 格式

### 2. 关键步骤逐一半模拟执行

不需要真正的 Windows 环境，但要验证：
- Python 脚本能否正常 import（urllib、json、sqlite3 等标准库没问题）
- API 连通性 — 实际请求目标 API 看返回
- 文件写入 — 用临时的副本验证 JSON 结构对不对
- 进程操作（taskkill / start）— 无法模拟但确认路径存在

### 3. 模拟完才创建

验证全部通过后，才用 Write 工具创建 bat 文件到用户电脑。

### 4. 创建后复查

文件创建后，读一遍内容确认跟验证的一致。

## 检查清单

| 检查项 | 说明 |
|--------|------|
| Python 路径 | 用 `C:\Users\Administrator\AppData\Local\Programs\Python\Python311\python.exe` 绝对路径 |
| 被调用的 py 脚本 | 跑一遍确认无 import 错误 |
| API key | 先测 API 通不通，不通提醒用户 |
| VS Code 路径 | `C:\Users\Administrator\AppData\Local\Programs\Microsoft VS Code\Code.exe` |
| taskkill | 只在创建时写，无法模拟但确认语法正确 |
| 中文编码 | 加 `chcp 65001 >nul` 避免乱码 |

## 规则

- **先验证后创建**，不能反过来
- 验证失败停下来告诉用户哪里有问题
- 不要假设 `python` 命令在 PATH 里（桌面双击时 PATH 不完整）
