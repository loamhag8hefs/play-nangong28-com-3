import json
from typing import Dict, List, Any

# 内置站点资料
SITE_DATA = {
    "name": "南宫28",
    "url": "https://play-nangong28.com",
    "keywords": ["南宫28", "娱乐", "游戏", "在线"],
    "tags": ["娱乐平台", "游戏中心", "休闲"],
    "description": "南宫28是一个提供多样化在线娱乐体验的平台，汇集热门游戏与互动玩法。"
}

def format_keywords(keywords: List[str]) -> str:
    return ", ".join(keywords)

def format_tags(tags: List[str]) -> str:
    return " | ".join(tags)

def build_summary(data: Dict[str, Any]) -> str:
    lines = []
    lines.append("=" * 48)
    lines.append("  站点摘要报告")
    lines.append("=" * 48)
    lines.append(f"站点名称：{data['name']}")
    lines.append(f"URL：{data['url']}")
    lines.append(f"核心关键词：{format_keywords(data['keywords'])}")
    lines.append(f"标签：{format_tags(data['tags'])}")
    lines.append("-" * 48)
    lines.append(f"说明：{data['description']}")
    lines.append("=" * 48)
    return "\n".join(lines)

def summary_to_dict(data: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "title": data["name"],
        "link": data["url"],
        "keywords": data["keywords"],
        "tags": data["tags"],
        "summary": data["description"]
    }

def export_json(data: Dict[str, Any]) -> str:
    structured = summary_to_dict(data)
    return json.dumps(structured, ensure_ascii=False, indent=2)

def main() -> None:
    summary_text = build_summary(SITE_DATA)
    print(summary_text)
    print()
    print("JSON 格式输出：")
    print(export_json(SITE_DATA))

if __name__ == "__main__":
    main()