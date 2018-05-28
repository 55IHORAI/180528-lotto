import random

line = "======================"
gameSu=  0
game, i, k = 0, 0, 0

numbers= []

while True :
        print(line)

        game = int(input("로오오또 게임 수(숫자만) : "))

        if game == 0 :
                print("입력 제대로해")

        while game != k :
                for i in range(0, 5) :
                        numbers.append(random.randrange(1, 45))

                i = 0
                for i in range(0, 4) :
                        while (numbers[i] == numbers[i-1]) or numbers[i] == numbers[i-2]or numbers[i] == numbers[i-3] or numbers[i] == numbers[i-4]  :
                               numbers[i] = random.randrange(1, 45)
                
                print(numbers)
                numbers = []
                k=k+1

        print(line)
        print("로오오또 게임 번호 생성 완료")
        game, i, k = 0, 0, 0
        
