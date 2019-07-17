for i in range(1, 101):    # 1부터 100까지 100번 반복
    if i % 15 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:         # 3의 배수일 때
        print('Fizz')      # Fizz 출력
    elif i % 5 == 0:       # 5의 배수일 때
        print('Buzz')      # Buzz 출력
    else:
        print(i)