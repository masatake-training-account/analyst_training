"""
列データが重複しないようにmergeを使用して結合
customer_masterとitem_masterをjoin_dataに結合する。

データ：
* customer_master.csv
* item_master.csv
* transaction_1.csv
* transaction_2.csv
* transaction_detail_1.csv
* transaction_detail_2.csv
"""

import pandas as pd
from knock import knock01, knock03


def knock04():
	# 個別データを取得
	customer_master, item_master, transaction_1, transaction_2, transaction_detail_1, transaction_detail_2 = knock01.knock01()
	# 結合データを取得
	join_data = knock03.knock03()
	#
	# # join_dataの列を確認
	# print(join_data.columns)
	#
	# # 列データを確認する
	# print(customer_master.columns)
	# print(item_master.columns)

	# 消費者データの結合
	join_data = pd.merge(
		join_data, customer_master, on="customer_id", how="left"
	)

	# 商品データの結合
	join_data = pd.merge(
		join_data, item_master, on="item_id", how="left"
	)

	# # 結果の出力
	# print(join_data.head())
	# print(join_data.columns)

	# # csvファイルで保存
	# join_data.to_csv('knock04.csv', encoding="shift_jis")
	return join_data
