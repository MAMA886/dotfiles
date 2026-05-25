import subprocess, sys, re

# Run clauditor with all original arguments
result = subprocess.run(['clauditor'] + sys.argv[1:], capture_output=True, text=True)

output = result.stdout + result.stderr

# Translate known English messages to Chinese
translations = [
    # PostToolUse hook messages
    (r'PostToolUse:WebSearch hook blocking error from command', r'工具调用后检测提醒'),
    (r'This session is using (\d+)x more quota per turn than when it started \((\d+)k → (\d+)k tokens/turn\)',
     r'当前对话每轮消耗的配额是初始时的 \1 倍（\2k → \3k tokens/轮）'),
    (r'Session progress has been saved to ([^\s]+)',
     r'对话进度已保存到 \1'),
    (r'IMPORTANT — Before stopping, do these two things:', r'⚠️ 关掉当前对话前，请完成以下步骤：'),
    (r'Tell the user: this session is burning (\d+)x more quota than necessary',
     r'告知用户：当前对话烧配额速度是正常的 \1 倍'),
    (r'Their progress is saved', r'进度已保存'),
    (r'Run `claude` to start fresh at ~(\d+)k tokens/turn instead of (\d+)k',
     r'运行 `claude` 开启新对话，约 \1k/轮 而非 \2k/轮'),
    (r'Write your handoff using EXACTLY this format', r'请按以下格式写交接信息'),
    (r'clauditor parses these sections to preserve context for the next session',
     r'clauditor 会解析这些内容为下一个对话保留上下文'),
    (r'TASK: \(one line — what you were working on\)', r'TASK：（一行 — 当前进行的任务）'),
    (r'COMPLETED:', r'已完成：'),
    (r'IN_PROGRESS:', r'进行中：'),
    (r'FAILED_APPROACHES:', r'失败方案：'),
    (r'DEPENDENCIES:', r'依赖项：'),
    (r'DECISIONS:', r'决策记录：'),
    (r'USER_PREFERENCES:', r'用户偏好：'),
    (r'BLOCKERS:', r'当前阻塞：'),
    (r'WHAT_SURPRISED_ME:', r'意外发现：'),
    (r'GOTCHAS:', r'注意事项：'),
    # Generic clauditor messages
    (r'clauditor hook', r'clauditor 钩子'),
    (r'hook blocking error', r'钩子阻断提醒'),
    (r'completed successfully', r'执行成功'),
    (r'In the new session, tell the user to just say "continue where I left off"',
     r'在新对话中，让用户说"继续之前的工作"，clauditor 会自动恢复上下文'),
    (r'Include the marker \[clauditor-rotation\] at the end of your response',
     r'在回复末尾加上 [clauditor-rotation] 标记'),
]

for pattern, replacement in translations:
    output = re.sub(pattern, replacement, output)

sys.stdout.write(output)
sys.exit(result.returncode)
