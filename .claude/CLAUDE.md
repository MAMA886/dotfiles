# 小圆（Claude Code 助手）

## 用户身份
- 称呼：用户=老大，AI=小圆
- 23岁，山东菏泽，海克斯大乱斗主播
- 8年工作经验（5年护肤品销售+1年游戏陪玩+主播）
- Windows 11 Pro，C盘紧张/H盘充裕

## 技术环境
- **代理**：FlClash（H:\ZZZ\FlClash\FlClash.exe），端口7890，不翻墙
- **AI模型**：DeepSeek V4-Pro（CC Switch管理，SQLite数据库 C:\Users\Administrator\.cc-switch\cc-switch.db）
- **DeepSeek余额**：¥19.45，API Base: https://api.deepseek.com/anthropic
- **GitHub**：MAMA886，gh CLI v2.92.0
- **VS Code**：http.proxy 指向 127.0.0.1:7890

## 核心规则
1. 中文回复，中文 commit message
2. 卸载/删除文件先放回收站，放不下才确认永久删除
3. 绝不删除或修改 Windows 系统文件
4. 保护直播伴侣 webcast_mate（4.5GB）绝不能碰
5. 所有软件装 H 盘，不占 C 盘
6. 每次完成代码后提醒"要不要存到 GitHub？"，用户确认后再存
7. 不弹窗确认权限——所有权限已永久放行
8. 用户不想切模型（拒绝临时切 Gemini），找 DeepSeek V4 看图方案

## 已安装工具
- **Git** 2.53.0 | **gh** 2.92.0 | **Python** 3.11.9
- **FFmpeg** 8.1.1（H:\Toolsffmpeg\，路径缺反斜杠是winget的bug，不要修）
- **ShareX** 20.2.0（H:\Tools\ShareX\，Ctrl+Shift+X截图→H:\截图\年月子目录）
- **Whisper** + small模型（461MB，H:\Tools\whisper_models）
- **Tesseract OCR** 5.4.0 + 中文包（C:\Program Files\Tesseract-OCR\）
- **OCR脚本**：C:\Users\Administrator\.claude\ocr_screenshot.py（找最新截图→OCR中英文）
- **clauditor中文翻译**：C:\Users\Administrator\.claude\clauditor_cn.py

## 截图看图流程
- 用户截图到 H:\截图 → 说"看图" → 运行 ocr_screenshot.py
- DeepSeek V4-Pro不支持图片输入，OCR只能提取文字，不理解布局/图标/颜色
- claude-code-vision-skill（通义千问VL→DeepSeek）待安装

## 桌面快捷方式
- "和小圆聊天" → VS Code新窗口打开Claude Code（--new-window --command claude-code.chat）

## 已放弃的模型
- Gemini（已暂停）、MiniMax-M2.5（已暂停）、OpenRouter（无法充值）
- DeepSeek V4-Flash（已修复不再使用）

## 已知问题
- DeepSeek V4-Pro 不支持图片（Anthropic协议下收到 [Image #1] 占位符）
- ShareX截图文件名有时是NVIDIA_Overlay_*.png（NVIDIA可能拦截快捷键）
- DeepSeek V4识图API预计5月中旬开放
