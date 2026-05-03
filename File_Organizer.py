import pathlib
import shutil

CATEGORIES = {
    "Web Content": {".html", ".htm", ".php", ".asp", ".js", ".css", ".xml", ".json", ".rss"},
    "Images":      {".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tiff", ".svg", ".webp", ".ico", ".heif", ".raw"},
    "Movies":      {".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".webm", ".mpeg", ".mpg", ".3gp", ".vob", ".ogv"},
    "Text Files":  {".txt", ".pdf", ".doc", ".docx", ".odt", ".rtf", ".epub", ".md", ".tex"},
    "Archives":    {".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz", ".iso", ".dmg"},
    "Audio":       {".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a", ".m4b", ".opus", ".wma", ".aiff"},
}

EXT_MAP = {ext: cat for cat, exts in CATEGORIES.items() for ext in exts}


def organize_files(directory="."):
    script = pathlib.Path(__file__).name
    for item in pathlib.Path(directory).iterdir():
        if not item.is_file() or item.name == script:
            continue
        ext = item.suffix.lower()
        if not ext:
            print(f"Skipping {item.name}: no extension")
            continue
        folder = pathlib.Path(directory) / EXT_MAP.get(ext, "Miscellaneous")
        folder.mkdir(exist_ok=True)
        shutil.move(str(item), folder / item.name)
        print(f"{item.name} -> {folder.name}")


if __name__ == "__main__":
    organize_files()
    input("\nPRESS ENTER TO EXIT")
