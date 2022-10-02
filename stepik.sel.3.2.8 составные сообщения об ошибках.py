#Вам дана функция test_input_text,  которая принимает два значения: expected_result — ожидаемый результат,
# и actual_result — фактический результат. Обратите внимание, input использовать не нужно!

#Функция должна проверить совпадение значений с помощью оператора assert и, в случае несовпадения, предоставить исчерпывающее сообщение об ошибке.
#Sample Input 1:
#8 11
#Sample Output 1:
#expected 8, got 11
#Sample Input 2:
#11 11

def test_input_text(expected_result, actual_result):
    # ваша реализация, напишите assert и сообщение об ошибке
    assert actual_result == expected_result, \
        f"expected {expected_result}, got {actual_result}"