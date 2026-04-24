# ملف مهنة العمدة (mayor.py)
class Mayor:
    def __init__(self):
        self.city_funds = 100000 
        self.tax_rate = 0.10

    def get_status(self):
        return f"خزينة المدينة: {self.city_funds}$"

    def collect_taxes(self, player):
        tax = player.balance * self.tax_rate
        player.balance -= tax
        self.city_funds += tax
        print(f"تم جمع ضريبة بقيمة {tax}$ من {player.name}")
