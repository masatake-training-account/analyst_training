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
from knock import knock02


def knock03():
	# データを取得
	transaction, transaction_detail = knock02.knock02()

	# 列方向に結合
	# transaction_idが重複
	join_data = pd.merge(
		transaction_detail, transaction[
			['transaction_id', 'payment_date', 'customer_id']
		], on="transaction_id", how="left")

	# # 結果の表示
	# print(join_data)
	#
	# print(len(transaction_detail))
	# print(len(transaction))
	# print(len(join_data))

	return  join_data