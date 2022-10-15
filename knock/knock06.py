"""
priceの合計値を計算し、join_dataの合計とtransactionの合計が一致することを確認する

"""

import pandas as pd
from knock import knock02, knock05


def knock06():
	# トランザクションデータを取得
	transaction, transaction_detail = knock02.knock02()
	#  結合データを取得
	join_data = knock05.knock05()

	print(join_data["price"].sum())
	print(transaction["price"].sum())

	return join_data["price"].sum() == transaction["price"].sum()
