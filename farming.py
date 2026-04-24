import time

class Farm:
    def __init__(self):
        self.crops = {
            "قمح": {"growth_time": 5, "sell_price": 150},
            "بندورة": {"growth_time": 10, "sell_price": 300}
        }

    def plant(self, player, crop_name):
        if crop_name in self.crops:
            print(f"تم زراعة {crop_name}... انتظر قليلاً لينمو.")
            # محاكاة وقت النمو (مثلاً 5 ثوانٍ)
            time.sleep(self.crops[crop_name]["growth_time"])
            print(f"نمت الـ {crop_name}! حان وقت الحصاد.")
            self.harvest(player, crop_name)

    def harvest(self, player, crop_name):
        profit = self.crops[crop_name]["sell_price"]
        player.balance += profit
        print(f"تم بيع المحصول! ربحت {profit}$. رصيدك الجديد: {player.balance}$")

# هذا النظام سيجعل اللاعب المزارع يبدأ بدورة اقتصادية كاملة
