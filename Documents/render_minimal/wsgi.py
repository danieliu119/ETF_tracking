import os
import sys
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

import app as dashboard_app


db_path = os.getenv("DB_PATH", "").strip()
if db_path:
    dashboard_app.DB_PATH = db_path

app = dashboard_app.app
