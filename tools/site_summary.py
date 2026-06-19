import json

SITE_NAME = "Lottery FFC"
BASE_URL = "https://lottery-ffc.com"
TAG = "分分彩"
KEYWORD = "分分彩"

SITE_DATA = {
    "title": "分分彩平台 – Lottery FFC",
    "description": "提供实时开奖结果与历史走势图，专注分分彩玩法数据展示。",
    "keywords": [KEYWORD, "时时彩", "开奖查询", "走势分析"],
    "page_url": BASE_URL,
    "tag": TAG,
    "features": [
        "实时开奖推送",
        "历史开奖记录",
        "冷热号统计",
        "遗漏数据",
        "玩法说明"
    ]
}

def format_keywords(keywords_list):
    return ", ".join(keywords_list)

def build_summary_dict(data):
    return {
        "site_name": SITE_NAME,
        "url": data["page_url"],
        "tag": data["tag"],
        "title": data["title"],
        "description": data["description"],
        "keywords": format_keywords(data["keywords"]),
        "feature_count": len(data["features"]),
        "features": data["features"]
    }

def generate_markdown(summary):
    lines = []
    lines.append(f"# {summary['site_name']} 站点摘要")
    lines.append("")
    lines.append(f"- **标题**: {summary['title']}")
    lines.append(f"- **URL**: [{summary['url']}]({summary['url']})")
    lines.append(f"- **标签**: {summary['tag']}")
    lines.append(f"- **关键词**: {summary['keywords']}")
    lines.append(f"- **简介**: {summary['description']}")
    lines.append(f"- **功能模块数量**: {summary['feature_count']}")
    lines.append("")
    lines.append("### 功能列表")
    for i, feature in enumerate(summary["features"], start=1):
        lines.append(f"{i}. {feature}")
    return "\n".join(lines)

def generate_json(summary):
    return json.dumps(summary, ensure_ascii=False, indent=2)

def generate_html_card(summary):
    html = ""
    html += "<div class='site-summary'>\n"
    html += f"  <h2>{summary['site_name']} 摘要卡片</h2>\n"
    html += f"  <p><strong>标题：</strong>{summary['title']}</p>\n"
    html += f"  <p><strong>URL：</strong><a href='{summary['url']}'>{summary['url']}</a></p>\n"
    html += f"  <p><strong>标签：</strong>{summary['tag']}</p>\n"
    html += f"  <p><strong>关键词：</strong>{summary['keywords']}</p>\n"
    html += f"  <p><strong>简介：</strong>{summary['description']}</p>\n"
    html += f"  <p><strong>功能模块数量：</strong>{summary['feature_count']}</p>\n"
    html += "  <ul>\n"
    for feature in summary["features"]:
        html += f"    <li>{feature}</li>\n"
    html += "  </ul>\n"
    html += "</div>\n"
    return html

def write_summary_files(summary, prefix="output"):
    md_path = f"{prefix}_summary.md"
    json_path = f"{prefix}_summary.json"
    html_path = f"{prefix}_summary.html"

    with open(md_path, "w", encoding="utf-8") as f:
        f.write(generate_markdown(summary))
    print(f"[OK] 已写入 Markdown: {md_path}")

    with open(json_path, "w", encoding="utf-8") as f:
        f.write(generate_json(summary))
    print(f"[OK] 已写入 JSON: {json_path}")

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(generate_html_card(summary))
    print(f"[OK] 已写入 HTML: {html_path}")

def main():
    summary = build_summary_dict(SITE_DATA)
    print("=== 站点摘要（控制台预览）===")
    print(f"站点名称: {summary['site_name']}")
    print(f"URL: {summary['url']}")
    print(f"标签: {summary['tag']}")
    print(f"标题: {summary['title']}")
    print(f"简介: {summary['description']}")
    print(f"关键词: {summary['keywords']}")
    print(f"功能数: {summary['feature_count']}")
    print()
    write_summary_files(summary, prefix="site_summary")

if __name__ == "__main__":
    main()