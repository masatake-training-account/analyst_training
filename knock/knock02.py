"""
transactionデータを結合して長さを表示する

データ：
* customer_master.csv
* item_master.csv
* transaction_1.csv
* transaction_2.csv
* transaction_detail_1.csv
* transaction_detail_2.csv
"""

import pandas as pd
from knock import knock01


def knock02():
	# 個別データを取得
	customer_master, item_master, transaction_1, transaction_2, transaction_detail_1, transaction_detail_2 = knock01.knock01()

	# 行方向に結合する
	transaction = pd.concat((transaction_1, transaction_2), axis=0, ignore_index=True)
	# # 行の長さを表示する
	# print(len(transaction_1))
	# print(len(transaction_2))
	# print(len(transaction))

	# 詳細データを行方向に結合する
	transaction_detail = pd.concat((transaction_detail_1, transaction_detail_2), axis=0, ignore_index=True)
	# # 行の長さを表示する
	# print(len(transaction_detail_1))
	# print(len(transaction_detail_2))
	# print(len(transaction_detail))

	# 結合データを返す
	return  transaction, transaction_detail