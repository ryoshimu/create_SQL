import sys

import pandas as pd
import Util


args = sys.argv
csv_file_paths = ['data1.csv', 'data2.csv', 'data3.csv']
# CSVファイルからデータを読み込む
# csv_file_path = 'import_csv/data.csv'
# df = pd.read_csv(csv_file_path)

# テーブル名を指定
table_name = 'your_table_name'

# 使用するカラムを指定
columns_to_use = ['a', 'b', 'd', 'e']  # 適宜変更


# インサート文を生成して出力する
insert_statements = []
for index, row in df.iterrows():
    columns = ', '.join(columns_to_use)
    values = ', '.join([f"'{Util.process_value(col, row[col])}'" for col in columns_to_use])
    insert_stmt = f"INSERT INTO {table_name} ({columns}) VALUES ({values});"
    insert_statements.append(insert_stmt)

# 生成したインサート文をファイルに書き込む
with open('insert_statements.sql', 'w') as file:
    for stmt in insert_statements:
        file.write(stmt + '\n')

print("インサート文がinsert_statements.sqlファイルに書き込まれました。")

