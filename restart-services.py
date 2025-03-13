import os
import pathlib

ignore_files = []
# put what you want in ignore files use the file name with the extenstion for example docker.service

home_dir = Path.home()
systemd_user_dir = home_dir / ".systemd" / "user"
files = list(systemd_user_dir.rglob("*.service"))

for file in files:
        if file.is_file() and not file.name in ignore_files:
          print(f"ran {file.name}")
          os.system(f"systemctl --user restart {file.name} && journalctl --user -u {file.stem} -f")
