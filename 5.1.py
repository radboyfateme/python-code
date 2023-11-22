class Handling_Exception_My(Exception):
    pass

class Selection_Player:
    @staticmethod
    def integer_check(value):
        try:
            return int(value)
        except ValueError:
            raise Handling_Exception_My("Age or Height is not valid")

    @staticmethod
    def float_check(value):
        try:
            return float(value)
        except ValueError:
            raise Handling_Exception_My("Weight is not valid")

    @staticmethod
    def validation_weight(age, weight):
        if 15 <= age <= 25 and not (60 <= weight <= 80):
            raise Handling_Exception_My("Weight out of range for age 15-25")
        elif 25 < age <= 35 and not (50 <= weight <= 75):
            raise Handling_Exception_My("Weight out of range for age 25-35")

    @staticmethod
    def validation_height(height):
        if not 170 <= height <= 190:
            raise Handling_Exception_My("Height out of range")

    def player_register(self, code, age, height, weight):
        age = self.integer_check(age)
        height = self.integer_check(height)
        weight = self.float_check(weight)

        if not (15 <= age <= 35):
            raise Handling_Exception_My("Age out of range")
        
        self.validation_weight(age, weight)
        self.validation_height(height)

        return {"code": code, "age": age, "height": height, "weight": weight}


# برنامه اصلی
players = []
selection_player = Selection_Player()

while True:
    code = input("Enter player code (or 0 to exit): ")
    if code == "0":
        break
    
    age = input("Enter age: ")
    height = input("Enter height: ")
    weight = input("Enter weight: ")

    try:
        player_info = selection_player.player_register(code, age, height, weight)
        players.append(player_info)
    except Handling_Exception_My as e:
        print(e)

# نمایش اطلاعات بازیکنان واجد شرایط
for player in players:
    print(player)
