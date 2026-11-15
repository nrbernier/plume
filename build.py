"""Inline the cursive font into src/index.src.html -> index.html (single self-contained page)."""
import base64, pathlib
root = pathlib.Path(__file__).parent
src = (root / "src/index.src.html").read_text()
font = base64.b64encode((root / "fonts/playwrite-fr-trad-latin-400-normal.woff2").read_bytes()).decode()
(root / "index.html").write_text(src.replace("/*FONT*/", font))
