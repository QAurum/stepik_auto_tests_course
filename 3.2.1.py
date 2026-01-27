def test_input_text(expected_result, actual_result):
    assert test_input_text == {expected_result}, \
      f"expected {expected_result}, got {actual_result}"


#Проблема в том, что ты проверяешь саму функцию, а не аргументы! Ты написала assert test_input_text == ..., а нужно assert expected_result == actual_result.



#Правильно так:
def test_input_text(expected_result, actual_result):
    assert expected_result == actual_result, \
      f"expected {expected_result}, got {actual_result}"


#Слеш \ в конце строки — это символ переноса строки в Python. Он говорит интерпретатору: "эта строка продолжается на следующей строке".

#📝 Зачем он нужен:
#Без слеша пришлось бы писать всё в одну строку:

#Правильно так:
def test_input_text(expected_result, actual_result):
    assert expected_result == actual_result, f"expected {expected_result}, got {actual_result}"
