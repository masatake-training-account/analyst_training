"""
売上データを購入数と商品価格から計算してデータに追加する
先頭5行を表示する

購入数：quantity
商品価格：item_price
売上データ：price
"""

import pandas as pd
from knock import knock04


def knock05():
	# 結合データを取得
	join_data = knock04.knock04()

	# 売上データを計算する。
	join_data["price"] = join_data["quantity"] * join_data["item_price"]

	# # 結果を表示する
	# print(join_data[["price", "quantity", "item_price"]].head())

	return join_data
