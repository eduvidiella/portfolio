# Uso: desde la carpeta src ejecutar  python build_index.py  -> genera ../index.html
import base64, re
s = open("portfolio.html", encoding="utf-8").read()
def inline(m):
    path = m.group(1)
    data = base64.b64encode(open(path, "rb").read()).decode()
    mime = "image/png" if path.endswith(".png") else "image/jpeg"
    return 'src="data:' + mime + ';base64,' + data + '"'
s = re.sub(r'src="(img/[a-z-]+\.(?:jpg|png))"', inline, s)
head = '<!doctype html>\n<html lang="es">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
open("../index.html", "w", encoding="utf-8").write(head + s + "\n</html>\n")
print(len(s), s.count("data:image/jpeg"), "img/" in re.sub(r'data:image[^"]+', '', s))
