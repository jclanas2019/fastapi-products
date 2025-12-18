#!/usr/bin/env python3
import subprocess
import sys
from datetime import datetime

def run(cmd: list[str], fatal=True):
    print(f"\n▶ {' '.join(cmd)}")
    result = subprocess.run(cmd)
    if result.returncode != 0:
        if fatal:
            print("❌ Error ejecutando comando:", " ".join(cmd))
            sys.exit(result.returncode)
        return False
    return True

def main():
    args = set(sys.argv[1:])
    no_cache = "--no-cache" in args
    show_logs = "--logs" in args

    print("======================================")
    print(" FastAPI Products – Simple Builder")
    print("======================================")
    print(f"🕒 {datetime.now()}\n")

    # 1) Git pull
    run(["git", "pull"])

    # 2) Stop containers (no borra volumen)
    run(["docker", "compose", "down"])

    # 3) Build images
    build_cmd = ["docker", "compose", "build"]
    if no_cache:
        build_cmd.append("--no-cache")
    run(build_cmd)

    # 4) Start containers
    run(["docker", "compose", "up", "-d"])

    # 5) Status
    run(["docker", "compose", "ps"], fatal=False)

    # 6) Logs opcionales
    if show_logs:
        print("\n📌 Logs (Ctrl+C para salir):")
        subprocess.run(["docker", "compose", "logs", "-f", "--tail", "50"])

    print("\n✅ Build y deploy completados")

if __name__ == "__main__":
    main()
