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


def knock02():
	# 購入明細データ1
	transaction_1 = pd.read_csv(r'./knock/knock01/transaction_1.csv')
	# 購入明細データ2
	transaction_2 = pd.read_csv(r'./knock/knock01/transaction_2.csv')
	# 詳細データ1
	transaction_detail_1 = pd.read_csv('./knock/knock01/transaction_detail_1.csv')
	# 詳細データ2
	transaction_detail_2 = pd.read_csv('./knock/knock01/transaction_detail_2.csv')

	# 行方向に結合する
	transaction = pd.concat((transaction_1, transaction_2), axis=0, ignore_index=True)
	# 行の長さを表示する
	print(len(transaction_1))
	print(len(transaction_2))
	print(len(transaction))

	# 詳細データを行方向に結合する
	transaction_detail = pd.concat((transaction_detail_1, transaction_detail_2), axis=0, ignore_index=True)
	# 行の長さを表示する
	print(len(transaction_detail_1))
	print(len(transaction_detail_2))
	print(len(transaction_detail))