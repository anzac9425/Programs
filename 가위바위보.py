import random

yesNo = True
cWin = 1
cDefeat = 1

while yesNo:
    inputt = input("가위바위보를 하시겠습니까? y/n: ")

    if inputt == "y":
        yesNo2 = True

        while yesNo2:
            rsp = ['가위', '바위', '보']
            airsp = random.choice(rsp)
            inputt = input("가위, 바위, 보 중 하나만 입력해 주십시오.: ")

            if inputt == "가위":
                if airsp == "가위":
                    print("비겼습니다. 상대의 선택 : %s" %airsp)
                    cWin = 1
                    cDefeat = 1
                    inputt = input("retry? y/n: ")
                    if inputt == "y":
                        pass
                    if inputt == "n":
                        yesNo = False
                        yesNo2 = False

                elif airsp == "바위":
                    print("졌습니다. 상대의 선택 : %s" %airsp)
                    if cDefeat > 1:
                        print("%d연패" %cDefeat)
                    cWin = 1
                    cDefeat = cDefeat + 1
                    inputt = input("retry? y/n: ")
                    if inputt == "y":
                        pass
                    if inputt == "n":
                        yesNo = False
                        yesNo2 = False

                elif airsp == "보":
                    print("이겼습니다. 상대의 선택 : %s" %airsp)
                    if cWin > 1:
                        print("%d연승" %cWin)
                    cWin = cWin + 1
                    cDefeat = 1
                    inputt = input("retry? y/n: ")
                    if inputt == "y":
                        pass
                    if inputt == "n":
                        yesNo = False
                        yesNo2 = False

            elif inputt == "바위":
                if airsp == "가위":
                    print("이겼습니다. 상대의 선택 : %s" %airsp)
                    if cWin > 1:
                        print("%d연승" %cWin)
                    cWin = cWin + 1
                    cDefeat = 1
                    inputt = input("retry? y/n: ")
                    if inputt == "y":
                        pass
                    if inputt == "n":
                        yesNo = False
                        yesNo2 = False

                elif airsp == "바위":
                    print("비겼습니다. 상대의 선택 : %s" %airsp)
                    cWin = 1
                    cDefeat = 1
                    inputt = input("retry? y/n: ")
                    if inputt == "y":
                        pass
                    if inputt == "n":
                        yesNo = False
                        yesNo2 = False

                elif airsp == "보":
                    print("졌습니다. 상대의 선택 : %s" %airsp)
                    if cDefeat > 1:
                        print("%d연패" %cDefeat)
                    cWin = 1
                    cDefeat = cDefeat + 1
                    inputt = input("retry? y/n: ")
                    if inputt == "y":
                        pass
                    if inputt == "n":
                        yesNo = False
                        yesNo2 = False

            elif inputt == "보":
                if airsp == "가위":
                    print("졌습니다. 상대의 선택 : %s" %airsp)
                    if cDefeat > 1:
                        print("%d연패" %cDefeat)
                    cWin = 1
                    cDefeat = cDefeat + 1
                    inputt = input("retry? y/n: ")
                    if inputt == "y":
                        pass
                    if inputt == "n":
                        yesNo = False
                        yesNo2 = False

                elif airsp == "바위":
                    print("이겼습니다. 상대의 선택 : %s" %airsp)
                    if cWin > 1:
                        print("%d연승" %cWin)
                    cWin = cWin + 1
                    cDefeat = 1
                    inputt = input("retry? y/n: ")
                    if inputt == "y":
                        pass
                    if inputt == "n":
                        yesNo = False
                        yesNo2 = False

                elif airsp == "보":
                    print("비겼습니다. 상대의 선택 : %s" %airsp)
                    cWin = 1
                    cDefeat = 1
                    inputt = input("retry? y/n: ")
                    if inputt == "y":
                        pass
                    if inputt == "n":
                        yesNo = False
                        yesNo2 = False

            else:
                pass
        
    elif inputt == "n":
        yesNo = False

    else:
        pass
