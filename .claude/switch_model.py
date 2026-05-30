"""一键切换 Claude Pro 订阅 / DeepSeek V4-Pro"""
import json
import os
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

SETTINGS = r'C:\Users\Administrator\.claude\settings.json'
CONFIG = r'C:\Users\Administrator\.claude\deepseek_config.json'


def get_deepseek_env():
    with open(CONFIG, 'r', encoding='utf-8') as f:
        cfg = json.load(f)
    return {
        "ANTHROPIC_AUTH_TOKEN": cfg['token'],
        "ANTHROPIC_BASE_URL": cfg['base_url'],
        "ANTHROPIC_DEFAULT_HAIKU_MODEL": "deepseek-v4-flash",
        "ANTHROPIC_DEFAULT_OPUS_MODEL": "deepseek-v4-pro",
        "ANTHROPIC_DEFAULT_SONNET_MODEL": "deepseek-v4-pro",
        "ANTHROPIC_MODEL": cfg.get('model', 'deepseek-v4-pro')
    }


def main():
    target = sys.argv[1] if len(sys.argv) > 1 else 'claude'

    with open(SETTINGS, 'r', encoding='utf-8') as f:
        data = json.load(f)

    if target == 'deepseek':
        data['env'] = get_deepseek_env()
        msg = "已切换到 → DeepSeek V4-Pro（按量付费，烧 API 余额）"
    else:
        data['env'] = {}
        msg = "已切换到 → Claude Pro 订阅（走订阅，不烧钱）"

    with open(SETTINGS, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print()
    print("=" * 50)
    print(f"  {msg}")
    print("=" * 50)
    print()
    print("  ⚠️ 重启 VS Code 的 Claude Code 才生效！")
    print()


if __name__ == '__main__':
    main()
