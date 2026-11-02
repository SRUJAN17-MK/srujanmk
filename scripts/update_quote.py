import json
import urllib.request
from pathlib import Path

url = "https://dummyjson.com/quotes/random"

with urllib.request.urlopen(url, timeout=20) as response:
    data = json.loads(response.read())

quote = data["quote"].replace("\n", " ").strip()
author = data["author"].strip()

readme = Path("README.md")
content = readme.read_text(encoding="utf-8")

start = "<!-- DEV_QUOTE_START -->"
end = "<!-- DEV_QUOTE_END -->"

if start not in content or end not in content:
    raise ValueError("Quote markers missing in README")

new_quote = f"> “{quote}”\n>\n> — **{author}**"

before, remaining = content.split(start, 1)
_, after = remaining.split(end, 1)

content = before + start + "\n" + new_quote + "\n" + end + after

readme.write_text(content, encoding="utf-8")
print("Daily developer quote updated!")
