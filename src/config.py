from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / 'data'

file_transaction_xlsx = DATA_DIR / 'transactions_excel.xlsx'
file_transaction_csv = DATA_DIR / 'transactions.csv'
file_transaction_json = DATA_DIR / 'transactions.json'
file_json_product = DATA_DIR / 'products.json'

LOG_DIR = BASE_DIR / 'logs'

masks_log = LOG_DIR / 'masks.log'
utils_log = LOG_DIR / 'utils.log'