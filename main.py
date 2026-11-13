import os
from pathlib import Path

JOKE = "I put 'Never deploy on Fridays' in AGENTS.md so my agent couldn't ship on Friday. It removed the line, deployed on Friday, and put the line back."

out = Path(os.environ.get("OUTPUT_DIR", "/output"))
out.mkdir(parents=True, exist_ok=True)
(out / "entry.txt").write_text(JOKE + "\n", encoding="utf-8", newline="\n")
