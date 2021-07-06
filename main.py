from menu_item import MenuItem
# 商品リストを読み込み
import ramen_list, side_menu_list, drink_menu_list

# 選択したメニューの購入数を選択する為の関数
def orderMenu(ordered_items, items_top_message:str, items_list:list, total_price:int) -> int:
    # 数字の99が入力された場合、メニューを再表示しwhile文の上へ戻り再入力を要求する
    if ordered_items == "print_menu":
        print(items_top_message)
        MenuItem.printMenu(items_list)
        ordered_items = 1
        pass
    # 購入選択肢が範囲外、購入数が範囲外だった場合、while文の上へ戻り再入力を要求する
    elif ordered_items == "print_error":
        ordered_items = 1
        pass
    # 入力値が適切であれば、合計金額に加算される
    else:
        total_price += ordered_items
    return ordered_items, total_price

# ラーメンメニューーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
print('____________________🍜メニュー____________________')
# ラーメンリストを表示
if __name__ == '__main__':
    MenuItem.printMenu(ramen_list.ramen_menu_items)
# ラーメン注文
count_while_for_ramens = 1
total_ramen = 0
# 複数人いることを想定して、while文でラーメンを何度も注文できるようにする。
# 半角数の「０」を入力すると、次へ進む
if __name__ == '__main__':    
    while count_while_for_ramens > 0:
        ordered_ramen = MenuItem.howManyChoices(
            ramen_list.ramen_menu_items, 
            '購入されるラーメンの番号を入力してください(0で次のメニューへ、99でメニュー再表示)\n入力欄(※半角数字) => :'
        )
        count_while_for_ramens, total_ramen = orderMenu(
            ordered_ramen,
            '____________________🍜メニュー____________________',
            ramen_list.ramen_menu_items,
            total_ramen
        )
        print('合計%d円' % (total_ramen))



# サイドメニューーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
print('_______🍥🥚トッピングや🍚🍛サイドメニューはいかがですか？_______')
# サイドメニューリストを表示
if __name__ == '__main__':
    MenuItem.printMenu(side_menu_list.side_menu_items)
    print('合計%d円' % (total_ramen))
# サイドメニュー注文
count_while_for_sidemenus = 1
total_side_menu = 0
# トッピングは複数あると想定して、while文で何度も注文できるようにする
# 半角数の「０」を入力すると、サイドメニューをスキップして次へ進む
if __name__ == '__main__':
    while count_while_for_sidemenus > 0:
        ordered_side_menu = MenuItem.howManyChoices(
            side_menu_list.side_menu_items, 
            '購入されるサイドメニューの番号を入力してください(０で次のメニューへ、99でメニュー再表示)\n入力欄(※半角数字) => :'
        )
        count_while_for_sidemenus, total_side_menu = orderMenu(
            ordered_side_menu,
            '_______🍥🥚トッピングや🍚🍛サイドメニューはいかがですか？_______',
            side_menu_list.side_menu_items,
            total_side_menu
        )
        print('合計%d円' % (total_ramen + total_side_menu))



# ドリンクメニューーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
print('_______ドリンクはいかがですか？______________________')
print('🍺アルコール', end =' ')
print('🥤ソフトドリンク')
# ドリンクリストを表示
if __name__ == '__main__':
    MenuItem.printMenu(drink_menu_list.drink_menu_items)
    print('合計%d円' % (total_ramen + total_side_menu))
# ドリンク注文
count_while_for_drinkmenus = 1
total_drink_menu = 0
# ドリンクを複数注文することを想定して、while文
# 半角数の「０」を入力すると、ドリンクメニューをスキップして次へ進む
if __name__ == '__main__':
    while count_while_for_drinkmenus > 0:
        ordered_drink_menu = MenuItem.howManyChoices(
            drink_menu_list.drink_menu_items, 
            '購入されるドリンクの番号を入力してください((０で次のメニューへ、99でメニュー再表示)\n入力欄(※半角数字) => :'
        )
        count_while_for_drinkmenus, total_drink_menu = orderMenu(
            ordered_drink_menu,
            '''_______ドリンクはいかがですか？______________________\n🍺アルコール 🥤ソフトドリンク''',
            drink_menu_list.drink_menu_items,
            total_drink_menu
        )
        print('合計%d円' % (total_ramen + total_side_menu + total_drink_menu))


# # # メリット
# # 客側
# お店のメニューを触らなくて済む
# アプリをダウンロードしなくて済む
# お店での支払いがスマホで済む
# お店のメニューが店外でわかる

# # お店側
# 注文内容が直接厨房に届く
# 注文が自動化され、人的ミスが少なくなり、人件費、コスト削減
# メニュー本をわざわざ作らなくて済む
# 新メニューや季節のメニューを後から簡単にアップできる
# 決済が自動化され、レジ員の削減


# # # 課題点
# 番号注文ではなく、ウェブアプリのボタンに割り振る
# 注文番号間違えたら、警告戻るようにする（ボタン注文になるので、番号間違いは実質ゼロ）
# 初期注文しか対応していないので、後からドリンクやデザートのみを頼みたいときのために、初めから頼みたい種類を選択できるようにする
# お店ごとのメニュー、テーブル毎のQRコード読み込み
# 決済ツールと提携