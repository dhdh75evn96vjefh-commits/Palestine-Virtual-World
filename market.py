# نظام المتجر في نيو باليستينا
class Market:
    def __init__(self):
        # قائمة العناصر المتاحة وأسعارها
        self.items = {
            "بذور": 50,
            "أدوات بناء": 500,
            "جهاز حاسوب": 1200,
            "ترخيص بناء": 2000
        }

    def buy_item(self, player, item_name):
        if item_name in self.items:
            price = self.items[item_name]
            if player.balance >= price:
                player.balance -= price
                print(f"تم شراء {item_name} بنجاح! الرصيد المتبقي: {player.balance}")
            else:
                print("عذراً، رصيدك لا يكفي لشراء هذا العنصر.")
        else:
            print("هذا العنصر غير موجود في المتجر.")

# تجربة النظام (سيعمل هذا عند ربط الملفات)
# shop = Market()
# shop.buy_item(player1, "بذور")

