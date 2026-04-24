# Render 最小部署版

這個資料夾提供最小可部署設定，不改動你原本的 `app.py`，並包含 `Active_ETF_Holding_List.py` 的執行入口。

## 檔案說明

- `wsgi.py`: 載入根目錄的 Flask app，並支援 `DB_PATH` 環境變數。
- `run_active_etf_job.py`: 呼叫 `Active_ETF_Holding_List.py` 的 `fetch_etf_to_db()`。
- `requirements.txt`: Render 安裝套件清單。
- `render.yaml`: Render Blueprint 設定檔（web + worker）。

## 本機測試

在專案根目錄執行：

```bash
pip install -r render_minimal/requirements.txt
gunicorn render_minimal.wsgi:app
```

若本機 DB 不在根目錄，可先設定：

```bash
set DB_PATH=你的資料庫路徑
gunicorn render_minimal.wsgi:app
```

## Render 部署步驟

1. 將專案推到 GitHub。
2. 在 Render 建立新服務（可使用 Blueprint，讀取 `render_minimal/render.yaml`）。
3. 若資料庫檔不在專案根目錄，將 `DB_PATH` 環境變數改為正確路徑。

## `Active_ETF_Holding_List.py` 的部署方式

- 已透過 `run_active_etf_job.py` 納入部署流程。
- `render.yaml` 內建 `etf-sync-worker`，預設每 360 分鐘循環執行一次（`JOB_MODE=loop`）。
- 若只想執行一次，可改 `JOB_MODE=once`。

## 注意

- 使用 SQLite 時，免費方案的檔案系統可能是暫時性的，重啟後資料可能遺失。
- 若要長期穩定上線，建議改用 PostgreSQL。
- `Active_ETF_Holding_List.py` 使用 Selenium，Render 環境可能需要額外瀏覽器相依設定；若遇到瀏覽器啟動錯誤，建議改為外部排程（如 GitHub Actions）執行該同步腳本。
