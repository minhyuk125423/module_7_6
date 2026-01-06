
def personal_sum(numbers):
    result = 0              #숫자의 합
    incorrect_data = 0      #잘못된 데이터 개수
    count = 0               #정상적으로 더해진 숫자 개수

    for i in numbers:
        try:
            result += i
            count += 1
        except TypeError:
            incorrect_data += 1
            print(f'문자열입니다 - {i}')
    return (result, incorrect_data, count)

def calculate_average(numbers):
    try:
        summ = personal_sum(numbers)
        midle = summ[0]/summ[2]
        return midle
    except TypeError:
        print('유효하지 않은 데이터 형식입니다')
    except ZeroDivisionError:
        return 0

print(f'결과 1: {calculate_average("1, 2, 3")}') # 각 문자는 1개의 길이를 가진 문자열로 취급됩니다( , = 하나의 문자열)
print(f'결과 2: {calculate_average([1, "줄", 3, "다른 줄"])}') # 1과 3만 계산됩니다
print(f'결과 3: {calculate_average(567)}') # 데이터가 수신되지 않았습니다
print(f'결과 4: {calculate_average([42, 15, 36, 13])}') # 정상 작동 되야 합니다
