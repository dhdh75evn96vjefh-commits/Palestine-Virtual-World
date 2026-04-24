# نظام اللاعب في مشروع نيو باليستينا
class Player:
    def __init__(self, name, job):
        self.name = name
        self.job = job
        self.balance = self.set_initial_balance()

    def set_initial_balance(self):
        # ميزانية افتراضية لكل مهنة (قابلة للتعديل لاحقاً)
        jobs_data = {
            "عمدة": 10000,
            "مهندس": 5000,
            "مبرمج": 4500,
            "مزارع": 2000
        }
        return jobs_data.get(self.job, 1000)

    def status(self):
        return f"اسم اللاعب: {self.name} | المهنة: {self.job} | الرصيد الحالي: {self.balance}"

# إنشاء لاعب تجريبي
player_one = Player("المستخدم", "عمدة")
print(player_one.status())
