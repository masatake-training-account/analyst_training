"""
transactionデータを列方向に結合して列の長さを表示する
列データが重複しないようにmergeを使用して結合

データ：
* customer_master.csv
* item_master.csv
* transaction_1.csv
* transaction_2.csv
* transaction_detail_1.csv
* transaction_detail_2.csv
"""

import pandas as pd


def knock03():
	# データを読み込み
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
	transaction_detail = pd.concat((transaction_detail_1, transaction_detail_2), axis=0, ignore_index=True)

	# 列名の確認
	print(transaction.columns)
	print(transaction_detail.columns)

	# 列方向に結合
	# transaction_idが重複
	join_data = pd.merge(
		transaction_detail, transaction, on="transaction_id", how="left")

	# 結果の表示
	print(join_data)

	print(len(transaction_detail))
	print(len(transaction))
	print(len(join_data))
