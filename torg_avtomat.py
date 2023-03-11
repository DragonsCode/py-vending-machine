
danniye={"kupyura": {1000: 0, 2000: 0, 5000: 0, 10000: 0}, "sdacha": {1000: 10, 500: 10, 200: 10, 100: 10, 50: 10}, "pokupki": "", "balans_chelika": 0, "kupil": "", "itogo": 0, "produkti": {10: ["IceTea", 5000, 10], 15: ["Kurt", 6000, 10], 0: ['Pepsi', 7000, 10], 11: ['Lays', 4000, 10], 13: ['Bruni', 4000, 10], 15: ['Rocky_Ckroky', 6000, 10], 30: ['nesquik', 5000, 10], 31: ['ChocoPie', 4000, 10], 32: ['Nuts', 6000, 10], 33: ['Barni', 5000, 10], 34: ['Ermak', 5000, 10], 40: ['Ermak', 5000, 10], 41: ['Asia_Kurt', 5000, 10], 42: ['Rondo', 4000, 10], 43: ['KitKat', 6000, 10], 45: ['Snickers', 7000, 10], 50: ['IceTea', 5000, 10], 59: ['IceTea', 5000, 10], 53: ['IceTea', 5000, 10], 54: ['Crafers', 9000, 10], 55: ['Bisquit', 5000, 10], 60: ['Pepsi', 7000, 10], 61: ['Pepsi', 7000, 10], 62: ['Pepsi', 7000, 10], 63: ['Pepsi', 7000, 10], 64: ['Pepsi', 7000, 10], 65: ['Pepsi', 7000, 10], 70: ['Red_Bul', 10000, 10], 71: ['Red_Bul', 10000, 10], 72: ['Red_Bul', 10000, 10], 73: ['Red_Bul', 10000, 10], 74: ['Red_Bul', 10000, 10], 75: ['Red_Bul', 10000, 10]}}
class avtomat:
    def dev_mode():
        print("Режим разработчика\n1- Пополнить сдачу до максимума\n2- Заполнить товары до максимума\n3- Вывести деньги\n4- Добавить или убрать купюру\n5- Добавить или убрать сдачи\n6- Выйти из режима разработчика\nВы можете выполнить только одну задачу за раз!")
        command=input()
        if command in [1, "1"]:
            for i in danniye["sdacha"]:
                danniye["sdacha"][i]=45
            sdacha_v_avtomat=0
            for i in danniye["sdacha"]:
                sdacha_v_avtomat+=danniye["sdacha"][i]*i
            print(f"Сдача пополнена! Сейчас в автомате {sdacha_v_avtomat} сум доступно для сдачи")
        elif command in [2, "2"]:
            for i in danniye["produkti"]:
                danniye["produkti"][i][2]=15
                print(f"Продукты пополнены!")
        elif command in [3, "3"]:
            bilo=danniye["kupyura"]
            vsego=0
            for i in danniye["kupyura"]:
                vsego+=danniye["kupyura"][i]*i
                danniye["kupyura"][i]=0
            print(f"В автомате было (купюра/количество): {bilo}. Вы всего вывели {vsego} сум")
        elif command in [4, "4"]:
            print("Введите \"d (купюра)\" чтобы удадить купюру. Ввелите \"a (купюра)\" чтобы добавить купюру")
            comm=input()
            if comm[0]=="d":
                try:
                    to_del=int(comm.split(" ")[1])
                    danniye["kupyura"].pop(to_del)
                    print(f"Купюра номиналом в {to_del} успешно удалена")
                except:
                    print("Неверный ввод команды!")
            elif comm[0]=="a":
                try:
                    to_add=int(comm.split(" ")[1])
                    danniye["kupyura"].update({to_add: 0})
                    print(f"Купюра номиналом в {to_add} успешно добавлена")
                except:
                    print("Неверный ввод команды!")
        elif command in [5, "5"]:
            print("Введите \"d (сдача)\" чтобы удадить сдачу. Ввелите \"a (сдача)\" чтобы добавить сдачу")
            comm=input()
            if comm[0]=="d":
                try:
                    to_del=int(comm.split(" ")[1])
                    danniye["sdacha"].pop(to_del)
                    print(f"Сдача номиналом в {to_del} успешно удалена")
                except:
                    print("Неверный ввод команды!")
            elif comm[0]=="a":
                try:
                    to_add=int(comm.split(" ")[1])
                    danniye["sdacha"].update({to_add: 0})
                    print(f"Сдача номиналом в {to_add} успешно добавлена")
                except:
                    print("Неверный ввод команды!")
        
        elif command in [6, "6"]:
            avtomat.start()
        
            
            
    def start():
        print("Выберите вариант:\n1-ввести купюру\n2-просмотреть продукты\n3-выбрать продукт\n4-получить сдачу")
        option=input()
        if option in [1, "1"]:
            
            sdacha_v_avtomat=0
            kupy=""
            kupyuri=danniye["kupyura"]
            for i in kupyuri:
                kupy+=str(i)+", "
            for i in danniye["sdacha"]:
                sdacha_v_avtomat+=danniye["sdacha"][i]*i
            print(f"Вводите купюры, мы принимаем только купюры номиналом в {kupy}сум. Учитывайте цену товара, так как у нас сдача не бесконечная, сейчас осталось сдачи: {sdacha_v_avtomat} сум, нажмите любую кнопку для выхода")
            sena=input()
            prod_proverka=0
            for i in danniye["produkti"]:
                if danniye["produkti"][i][2]>0:
                    prod_proverka=1
                    break
            try:
                if int(sena) not in danniye["kupyura"]:
                    print("Неизвестная купюра!")
                elif int(sena)>sdacha_v_avtomat:
                    print("Простите, но у нас нету сдачи в такой сумме!")
                elif prod_proverka==0:
                    print("Продуктов не осталось!")
                    prod_proverka=0
                else:
                    danniye.update({"balans_chelika": danniye["balans_chelika"]+int(sena)})
                    danniye["kupyura"][int(sena)]+=1
            except Exception as e:
                print(f"Возникла ошибка при вводе, попробуйте позже {e}\nВыход в главное меню\n")
            
        elif option in [2, "2"]:
            text="Продукт | цена | количество | номер\n"
            for i in danniye["produkti"]:
                text+=str(danniye["produkti"][i])+", "+str(i)+"\n"
            print(text)
        elif option in [3, "3"]:
            if danniye["balans_chelika"]>0:
                balans_chelik=danniye["balans_chelika"]
                while True:
                    text="Выбирайте продукты:\nПродукт | цена | количество | номер\n"
                    for i in danniye["produkti"]:
                        text+=str(danniye["produkti"][i])+", "+str(i)+"\n"
                    print(text+f"Вводите цифры по очереди, чтобы выйти и вывести покупки нажмите любую кнопку, чтобы отменить покупку введите 0000, ваш баланс: {balans_chelik}")
                    
                    kupil=danniye["kupil"]
                    itogo=danniye["itogo"]
                    try:
                        pokupka=int(input())
                        if pokupka not in danniye["produkti"]:
                            print("Нету такого продукта!")
                        
                        elif danniye["produkti"][pokupka][2]==0:
                            print("Этого продукта не осталось")
                        elif pokupka==0000:
                            print("Вы отменили покупку, выход в главное меню")
                            break
                        else:
                            produkt=danniye["produkti"][pokupka][0]
                            danniye.update({"kupil": danniye["kupil"]+f"{produkt}, "})
                            danniye.update({"itogo": danniye["itogo"]+danniye["produkti"][pokupka][1]})
                            skupleno=[]
                            skupleno.append(danniye["produkti"][pokupka])
                            
                    except:
                        kupil=danniye["kupil"]
                        itogo=danniye["itogo"]
                        
                        if itogo==0:
                            kupil+="вы ничего не купили"
                        print(f"{kupil}\nитого: {itogo} сум")
                        if danniye["balans_chelika"]<itogo:
                            print("У вас не достаточно средств!")
                            danniye.update({"kupil": "", "itogo": 0})
                            break
                        else:
                            danniye.update({"balans_chelika": danniye["balans_chelika"]-itogo})
                            for i in skupleno:
                                danniye["produkti"][i][2]-=1
                                balans=danniye["balans_chelika"]
                            print(f"Успешная покупка! У вас осталось {balans} сум")
                            danniye.update({"kupil": "", "itogo": 0})
                            break
                        
                        
            else:
                print("Сначала пополните баланс")
        elif option in [4, "4"]:
            sdacha_v_avtomat=1000*danniye["sdacha"][1000]+500*danniye["sdacha"][500]+200*danniye["sdacha"][200]+100*danniye["sdacha"][100]+50*danniye["sdacha"][50]
            
            if danniye["balans_chelika"]>sdacha_v_avtomat:
                print("К сожалению мы не сможем дать сдачу, так как ваш баланс превышает нашу сумму доступной сдачи")
            else:
                while danniye["balans_chelika"]-1000>=0 and danniye["sdacha"][1000]>0:
                    danniye.update({"balans_chelika": danniye["balans_chelika"]-1000, "sdacha": {1000: danniye["sdacha"][1000]-1, 500: danniye["sdacha"][500], 200: danniye["sdacha"][200], 100: danniye["sdacha"][100], 50: danniye["sdacha"][50]}})
                    
                    
                while danniye["balans_chelika"]-500>=0 and danniye["sdacha"][500]>0:
                    danniye.update({"balans_chelika": danniye["balans_chelika"]-500, "sdacha": {1000: danniye["sdacha"][1000], 500: danniye["sdacha"][500]-1, 200: danniye["sdacha"][200], 100: danniye["sdacha"][100], 50: danniye["sdacha"][50]}})
                    
                    
                while danniye["balans_chelika"]-200>=0 and danniye["sdacha"][200]>0:
                    danniye.update({"balans_chelika": danniye["balans_chelika"]-200, "sdacha": {1000: danniye["sdacha"][1000], 500: danniye["sdacha"][500], 200: danniye["sdacha"][200]-1, 100: danniye["sdacha"][100], 50: danniye["sdacha"][50]}})
                    
                    
                while danniye["balans_chelika"]-100>=0 and danniye["sdacha"][100]>0:
                    danniye.update({"balans_chelika": danniye["balans_chelika"]-100, "sdacha": {1000: danniye["sdacha"][1000], 500: danniye["sdacha"][500], 200: danniye["sdacha"][200], 100: danniye["sdacha"][100]-1, 50: danniye["sdacha"][50]}})
                    
                    
                while danniye["balans_chelika"]-50>=0 and danniye["sdacha"][50]>0:
                    danniye.update({"balans_chelika": danniye["balans_chelika"]-50, "sdacha": {1000: danniye["sdacha"][1000], 500: danniye["sdacha"][500], 200: danniye["sdacha"][200], 100: danniye["sdacha"][100], 50: danniye["sdacha"][50]-1}})
                
                sdacha_v_avtomate=1000*danniye["sdacha"][1000]+500*danniye["sdacha"][500]+200*danniye["sdacha"][200]+100*danniye["sdacha"][100]+50*danniye["sdacha"][50]
                polucheno=sdacha_v_avtomat-sdacha_v_avtomate
                print(f"Успешно! Вы получили {polucheno}")
        elif option in [177, "177"]:
            avtomat.dev_mode()
        else:
            print("Неизвестная команда")

while True:
    a=avtomat
    a.start()