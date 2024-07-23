import pandas as pd

def process_value(column_name, value):
    """
    カラム名に基づいて値に対して特定の処理を追加する
    """
    if column_name == 'column1':
        # 例えば、文字列を大文字に変換
        return str(value).upper()
    elif column_name == 'a':
        # 例えば、値に100を足す
        return str(int(value) + 100)
    elif column_name == 'column3':
        # 例えば、日付形式に変換
        return pd.to_datetime(value).strftime('%Y-%m-%d')
    else:
        # その他のカラムはそのまま
        return str(value).replace("'", "''")
