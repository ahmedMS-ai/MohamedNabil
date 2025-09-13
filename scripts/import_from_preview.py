\
import sys, requests, re, yaml
from bs4 import BeautifulSoup
from pathlib import Path

"""
Simple helper to prefill content.yaml from Open Graph tags.
Usage:
    python scripts/import_from_preview.py "https://felo.ai/en/page/preview/..."
"""

def main(url: str):
    r = requests.get(url, timeout=20)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")

    og_title = soup.find("meta", property="og:title")
    og_desc = soup.find("meta", property="og:description")
    title = og_title["content"] if og_title and og_title.get("content") else None
    desc = og_desc["content"] if og_desc and og_desc.get("content") else None

    root = Path(__file__).resolve().parent.parent
    cpath = root / "content.yaml"
    data = yaml.safe_load(cpath.read_text(encoding="utf-8"))

    if title: data["hero"]["title"] = title[:160]
    if desc: data["hero"]["subtitle"] = desc[:300]

    cpath.write_text(yaml.dump(data, allow_unicode=True, sort_keys=False), encoding="utf-8")
    print("Updated content.yaml with OG fields. Please review and adjust more sections as needed.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Provide the preview URL as an argument.")
        sys.exit(1)
    main(sys.argv[1])
