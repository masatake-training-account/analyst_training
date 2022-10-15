"""
顧客はデータ分析に取り組みたいと言っている。
ECサイトのデータ分析をお願いしたい

データベースから抽出したデータを表示する。
データ：
* customer_master.csv
* item_master.csv
* transaction_1.csv
* transaction_2.csv
* transaction_detail_1.csv
* transaction_detail_2.csv
"""

import pandas as pd


def knock01():
	# 顧客データを表示する
	customer_master = pd.read_csv(r'./knock/knock01/customer_master.csv')
	# print(customer_master.head())

	# 取り扱っている商品データ
	item_master = pd.read_csv(r'./knock/knock01/item_master.csv')
	# print(item_master.head())

	# 購入明細データ1
	transaction_1 = pd.read_csv(r'./knock/knock01/transaction_1.csv')
	# print(transaction_1.head())

	# 購入明細データ2
	transaction_2 = pd.read_csv(r'./knock/knock01/transaction_2.csv')
	# print(transaction_2.head())

	# 詳細データ1
	transaction_detail_1 = pd.read_csv('./knock/knock01/transaction_detail_1.csv')
	# print(transaction_detail_1.head())

	# 詳細データ2
	transaction_detail_2 = pd.read_csv('./knock/knock01/transaction_detail_2.csv')
	# print(transaction_detail_2.head())

	return (
		customer_master,
		item_master,
		transaction_1,
		transaction_2,
		transaction_detail_1,
		transaction_detail_2
	)
