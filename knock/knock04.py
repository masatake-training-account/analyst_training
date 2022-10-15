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


def knock04():
	# データを読み込み
	# 顧客データを表示する
	customer_master = pd.read_csv(r'./knock/knock01/customer_master.csv')
	# 取り扱っている商品データ
	item_master = pd.read_csv(r'./knock/knock01/item_master.csv')

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

	# 列方向に結合
	# transaction_idが重複
	join_data = pd.merge(
		transaction_detail, transaction[
			['transaction_id', 'payment_date', 'customer_id']
		], on="transaction_id", how="left")

	# join_dataの列を確認
	print(join_data.columns)

	# 列データを確認する
	print(customer_master.columns)
	print(item_master.columns)

	# 消費者データの結合
	join_data = pd.merge(
		join_data, customer_master, on="customer_id", how="left"
	)

	# 商品データの結合
	join_data = pd.merge(
		join_data, item_master, on="item_id", how="left"
	)

	# 結果の出力
	print(join_data.head())
	print(join_data.columns)

	# # csvファイルで保存
	# join_data.to_csv('knock04.csv', encoding="shift_jis")
