import os
import pandas as pd # type: ignore
from datetime import datetime

LOG_FOLDER = "logs"
FILE = os.path.join(LOG_FOLDER, "transactions.xlsx")


def ensure_file_exists():
    if not os.path.exists(LOG_FOLDER):
        os.makedirs(LOG_FOLDER)

    if not os.path.exists(FILE):
        df = pd.DataFrame(columns=["Date", "Time", "Command", "Status"])
        df.to_excel(FILE, index=False)


def log_transaction(command, status="Success"):
    try:
        ensure_file_exists()

        now = datetime.now()

        new_data = pd.DataFrame([{
            "Date": now.date(),
            "Time": now.strftime("%H:%M:%S"),
            "Command": command,
            "Status": status
        }])

        if os.path.exists(FILE):
            existing = pd.read_excel(FILE)
            df = pd.concat([existing, new_data], ignore_index=True)
        else:
            df = new_data

        df.to_excel(FILE, index=False)

        print("Transaction logged successfully.")

    except Exception as e:
        print("Transaction logging error:", e)


def get_today_transactions():
    try:
        if not os.path.exists(FILE):
            return []

        df = pd.read_excel(FILE)
        df["Date"] = pd.to_datetime(df["Date"]).dt.date

        today = datetime.now().date()
        df_today = df[df["Date"] == today]

        return df_today.values.tolist()

    except Exception as e:
        print("Error reading transactions:", e)
        return []