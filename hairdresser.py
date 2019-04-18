#УГТ - уровень глубины тона

#UGT={}
#oxygen=int(input("Оксид "))
#old_UGT=int(input("Исходный оттенок "))


def color_type(col_eyes, col_pelt, col_hair,frekcles=None):
      #Зима
      if (col_eyes=="зеленые" or col_eyes=="серые" or col_eyes=="голубые" or col_eyes=="карие") and  col_pelt=="белая" and col_hair=="черные":
            return "Зима"
      #Лето
      elif (col_eyes=="зеленые" or col_eyes=="голубые") and col_pelt=="молочная" and (col_hair=="светлые" or col_hair=="светло-каштановые"):
            return "Лето"
      #Весна
      elif (col_eyes=="голубые" or col_eyes=="зеленые") and (col_pelt=="кремовая" or col_pelt=="золотистая") and (col_hair=="золотистые" or "светло-каштанове"):
            return "Весна"
      #Осень
      elif (col_eyes=="карие" or col_eyes=="зеленые" or col_eyes=="голубые") and col_pelt=="смуглая" and (col_hair=="каштановые" or col_hair=="черные" or col_hair=="рыжые"):
            return "Осень"

      else:
            return "Попробуйте снова"
while True:
      print("\nМеню")
      print("1.Цветотип")
      print("2.Вычислить объем краски\n")
      choise=int(input("Ваш выбор "))

      if choise==1:
            print("Глаза: карие, зеленые, серые, голубые,")
            col_eyes=str(input())
            print("Кожа: белая, молочная, кремовая, золотистая, смуглая")
            col_pelt=str(input())
            print("Волосы: черные, светлые, светло-каштановые, золотистые, рыжые")
            col_hair=str(input())
            print(color_type(col_eyes, col_pelt, col_hair))
            
      elif choise==2:      
            len_hair=int(input("Длина волос "))

            print("Объем краски="+str(len_hair*4.3)+"  Объем оксида="+str(len_hair*4.3))
            print("Общий объем=",len_hair*4.3*2)






      
