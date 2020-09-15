coffee = 10
while True:
    money = int(input("돈을 넣어 주세요: "))
    if money == 300:
        print("커피를 줍니다.")
        coffee = coffee -1
    elif money > 300:
        print("거스름돈 %d를 주고 커피를 줍니다." % (money -300))
        coffee = coffee -1
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("남은 커피의 양은 %d개 입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지 합니다.")
        break


marks = [90, 25, 67, 45, 80]

number = 0
for mark in marks:
    number = number +1
    if mark >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." % number)

        marks = [90, 25, 67, 45, 80]

number = 0
for mark in marks:
    number = number + 1
    if mark < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다. " % number)

"60점 이상이면 합격이라는 문장을 출력하는 예제"

marks = [90, 25, 67, 45, 80]
for number in range(len(marks)): "len : 리스트 안의 요소 개수를 돌려주는 함수"
    if marks[number] < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다." % (number+1))

"구구단"

for i in range(2,10):        # ①번 for문
    for j in range(1, 10):   # ②번 for문
       print(i*j, end=" ")
    print('')

" 1부터 1000까지 자연수 중 3의 배수의 합 "
number=0
i=1
while i <= 1000:
    if i % 3 == 0:
        number += i
    i += 1
print(number)

i = 0
while True:
    i +=1
    if i > 5: break
    print('*' * i)

result= 0
for i in range(1, 101):
    result = result +i
    print(result)


jum = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
result = 0
for score in jum:
    result += score
print(result)

average = result/len(jum)
print(len(jum))
print(average)

numbers = [1, 2, 3, 4, 5]
result = []
for n in numbers:
    if n % 2 == 1:
        result.append(n*2)
print(result)

number = [1, 2, 3, 4, 5]
result = [n*2 for n in number if n % 2 == 1]
print(result)