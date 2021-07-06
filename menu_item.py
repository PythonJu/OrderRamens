class MenuItem:
    def __init__(self, name:str, price:int):
        self.name = name
        self.price = price

    def itemsName(self):
        return self.name

    def info(self):
        return '%sは¥%d円です' % (self.name, self.price)

    def printMenu(menu_items_list_name:list):
        menu_item0 = '0. 選択せず次へ進む'
        menu_items = '99. メニュー再表示'
        index = 1
        for menu_item in menu_items_list_name:
            # print(str(index) + '. ' + menu_item.info())
            print(f'{index}. {menu_item.info()}')
            index += 1
        print(menu_items)
        print(menu_item0)

    def howManyChoices(list_name:list, message:str):
        print('---------------------------------------------------------------------')
        try:
            selected_menu_number = int(input(message))
        except ValueError:
            print('※範囲外の入力です\n※半角数字で入力してください')
            return "print_error"
        # リストは0からindexが始まるので、-1
        selected_menu_number -= 1
        # アイテム選択時に９９が入力された場合、'print_menu'を戻し、メニューを再表示させる
        if selected_menu_number == 98:
            return "print_menu"
        # 範囲外の数字が入力された場合、'print_error'を戻し、再度注文へと移させる
        elif -1 > selected_menu_number or selected_menu_number > len(list_name) - 1:
            try: 
                raise ValueError('※範囲外の入力です')
            except ValueError as e:
                print(e)
                return "print_error"

        elif 0 <= selected_menu_number <= len(list_name):
            while True:
                print('---------------------------------------------------------------------')
                print(list_name[selected_menu_number].info())
                try: 
                    count = int(input('いくつ購入されますか(※最大10個まで、キャンセルする場合は0)\n入力欄(※半角数字) => :'))
                except ValueError:
                    print('※範囲外の入力です\n※半角数字を入力してください')
                    continue

                if 1 <= count <= 10:
                    result = list_name[selected_menu_number].price * count
                    return result
                elif count == 0:
                    print('※%sの購入はキャンセルされました' % list_name[selected_menu_number].itemsName())
                    return "print_menu"
                else:
                    try:
                        raise ValueError('※範囲外の入力です')
                    except ValueError as e:
                        print (e)
        elif selected_menu_number == -1:
            result = 0
            return result

class Ramen(MenuItem):
    def __init__(self, name:str, price:int, taste:str):
        super().__init__(name, price)
        self.taste = taste
    def itemsName(self):
        return self.taste + self.name
    def info(self):
        return '%s%s¥%d円' % (self.taste, self.name, self.price)

class SideMenu(MenuItem):
    def __init__(self,name:str,price:int):
        super().__init__(name,price)
    def info(self):
        return '%s¥%d円' % (self.name, self.price)

class Drink(MenuItem):
    def __init__(self, name:str, price:int, amount:str):
        super().__init__(name, price)
        self.amount = amount
    def info(self):
        return '%s(%sml)¥%d円' % (self.name, self.amount, self.price)

if __name__ == '__main__':
    print('テストコードはじめ')
    print('これはテストコードです')
    print('これはテストコードです')
    print('これはテストコードです')
    print('これはテストコードです')
    print('これはテストコードです')
    print('これはテストコードです')
    print('テストコード終わり')