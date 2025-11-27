import qrcode
from pathlib import Path
data = "https://youtube.com/watch?v=dQw4w9WgXcQ"
img = qrcode.make(data)
save_dir = Path(__file__).parent
img.save(save_dir / "qrcode.png")