import os
import sys
import time
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from Active_ETF_Holding_List import fetch_etf_to_db


def run_once() -> None:
    print("[Active ETF Job] Start sync...")
    fetch_etf_to_db()
    print("[Active ETF Job] Sync finished.")


def main() -> None:
    mode = os.getenv("JOB_MODE", "once").strip().lower()
    interval_minutes = int(os.getenv("JOB_INTERVAL_MINUTES", "360"))
    interval_seconds = max(interval_minutes, 1) * 60

    if mode == "loop":
        print(f"[Active ETF Job] Loop mode, interval={interval_minutes} minutes.")
        while True:
            try:
                run_once()
            except Exception as exc:
                print(f"[Active ETF Job] Error: {exc}")
            print("[Active ETF Job] Sleep until next run...")
            time.sleep(interval_seconds)
        return

    run_once()


if __name__ == "__main__":
    main()
