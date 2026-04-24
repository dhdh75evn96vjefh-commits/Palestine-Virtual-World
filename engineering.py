# نظام الهندسة والعقارات في نيو باليستينا
class Engineering:
    def __init__(self):
        # أنواع المباني، تكلفة بنائها، وعائد الربح منها
        self.buildings = {
            "منزل صغير": {"cost": 2000, "rent": 200},
            "عمارة": {"cost": 8000, "rent": 1000},
            "مركز تجاري": {"cost": 20000, "rent": 3000}
        }
        self.owned_properties = []

    def build(self, player, building_name):
        if building_name in self.buildings:
            cost = self.buildings[building_name]["cost"]
            if player.balance >= cost:
                player.balance -= cost
                self.owned_properties.append(building_name)
                print(f"مبروك! تم بناء {building_name}. الرصيد الحالي: {player.balance}$")
            else:
                print("عذراً، رصيدك لا يكفي لبناء هذا المنشأ.")

    def collect_rent(self, player):
        total_rent = 0
        for b in self.owned_properties:
            total_rent += self.buildings[b]["rent"]
        
        player.balance += total_rent
        print(f"تم جمع الإيجارات! حصلت على {total_rent}$. رصيدك الكلي: {player.balance}$")
# نظام الهندسة والعقارات في نيو باليستينا
class Engineering:
    def __init__(self):
        # أنواع المباني، تكلفة بنائها، وعائد الربح منها
        self.buildings = {
            "منزل صغير": {"cost": 2000, "rent": 200},
            "عمارة": {"cost": 8000, "rent": 1000},
            "مركز تجاري": {"cost": 20000, "rent": 3000}
        }
        self.owned_properties = []

    def build(self, player, building_name):
        if building_name in self.buildings:
            cost = self.buildings[building_name]["cost"]
            if player.balance >= cost:
                player.balance -= cost
                self.owned_properties.append(building_name)
                print(f"مبروك! تم بناء {building_name}. الرصيد الحالي: {player.balance}$")
            else:
                print("عذراً، رصيدك لا يكفي لبناء هذا المنشأ.")

    def collect_rent(self, player):
        total_rent = 0
        for b in self.owned_properties:
            total_rent += self.buildings[b]["rent"]
        
        player.balance += total_rent
        print(f"تم جمع الإيجارات! حصلت على {total_rent}$. رصيدك الكلي: {player.balance}$")

