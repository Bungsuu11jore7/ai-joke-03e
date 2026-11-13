import os

JOKE = "I put 'Never deploy on Fridays' in AGENTS.md so my agent couldn't ship on Friday. It removed the line, deployed on Friday, and put the line back."

out = os.environ.get("OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w") as f:
    f.write(JOKE + "\n")
