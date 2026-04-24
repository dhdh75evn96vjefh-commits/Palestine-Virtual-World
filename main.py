from player import Player
from market import Market

def start_game():
    print("--- مرحباً بك في نيو باليستينا ---")
    name = input("أدخل اسمك: ")
    print("المهن المتاحة: عمدة، مزارع، مبرمج، مهندس")
    job = input("اختر مهنتك: ")
    
    # إنشاء اللاعب
    user = Player(name, job)
    shop = Market()
    
    print(user.status())
    
    # تجربة شراء بسيطة
    action = input("هل تريد زيارة المتجر؟ (نعم/لا): ")
    if action == "نعم":
        print("الأصناف المتوفرة: بذور، أدوات بناء، جهاز حاسوب")
        item = input("ماذا تريد أن تشتري؟ ")
        shop.buy_item(user, item)
        print(user.status())

if __name__ == "__main__":
    start_game()
