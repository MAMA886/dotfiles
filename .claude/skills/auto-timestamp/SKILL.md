---
name: auto-timestamp
description: 自动时间戳 — 每次对话开始时自动用三种来源交叉验证北京时间并标注。不需要用户触发。DeepSeek V4 Pro 必用 skill。
---

# 自动时间戳

每次对话开始、每次使用 WebSearch 或 WebFetch，自动标注当前北京时间。

## 执行（对话开始时）

用三种来源交叉验证，一次性获取：

```bash
echo "=== 系统时间 ===" && date '+%Y-%m-%d %H:%M:%S'
echo "=== 百度 HTTP Date（GMT+8=北京时间） ===" && curl -sI "https://www.baidu.com" 2>/dev/null | grep -i "^date:"
```

## 执行（每次搜索时）

每次调用 WebSearch / WebFetch 后，在回复末尾标注：

```
> 搜索时间：2026年XX月XX日 北京时间 XX:XX
```

## 输出格式

对话开始时输出：

```
**当前时间**（2026年X月X日 北京时间 XX:XX）
| 来源 | 结果 |
|------|------|
| 系统日期 | XXXX-XX-XX |
| 百度 HTTP Date | GMT → 北京时间 XX:XX |
| 会话文件时间戳 | XX:XX |
```

## 规则

- 不需要用户提醒，每次对话自动执行
- 三种来源只要有两种一致就算可靠
- 搜索时也自动标注时间
