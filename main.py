import sys

import pandas as pd
import Util

# 引数を取得
args = sys.argv

# csvファイルを指定
csv_file_paths = ['data1.csv', 'data2.csv', 'data3.csv']

# テーブル名を指定
table_name = 'table_name'

# 使用するカラムを指定
columns_to_use = ['a', 'b', 'd', 'e']

# インサート文を生成して出力する
with open('insert_statements.sql', 'w') as file:
    insert_statements = []
    num = int(args[1])
    for csv_file_path in csv_file_paths:
        # CSVファイルからデータを読み込む
        df = pd.read_csv('import_csv/' + csv_file_path)
        # for index, row in enumerate(df.iterrows(), int(args[1])):
        for index, row in df.iterrows():
            print(row)
            columns = ', '.join(columns_to_use)
            values = ', '.join([f"'{Util.process_value(col, row[col], num)}'" for col in columns_to_use])
            insert_stmt = f"INSERT INTO {table_name} ({columns}) VALUES ({values});"
            insert_statements.append(insert_stmt)
            num += 1
    # 生成したインサート文をファイルに書き込む
    for stmt in insert_statements:
        file.write(stmt + '\n')

print("インサート文がinsert_statements.sqlファイルに書き込まれました。")

