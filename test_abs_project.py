def test_abs1():
  assert abs(-42) == 42, "Should be absolute value of a number"

if __name__=="__mane__":
  test_abs1()
  print("All tests passed!")  



#Если нам нужно добавить еще один тест, мы можем написать его как функцию в этом же файле. В приведенном примере мы уже не увидим сообщение "Everything passed", так как падение любого теста вызывает выход из программы:

def test_abs1():
    assert abs(-42) == 42, "Should be absolute value of a number"

def test_abs2():
    assert abs(-42) == -42, "Should be absolute value of a number"

if __name__ == "__main__":
    test_abs1()
    test_abs2()
    print("Everything passed")




#Запустите файл снова. Вы должны увидеть сообщение об упавшем втором тесте:


$ python test_abs_project.py

Traceback (most recent call last):
  File "test_abs_project.py", line 9, in <module>
    test_abs2()
  File "test_abs_project.py", line 5, in test_abs2
    assert abs(-42) == -42, "Should be absolute value of a number"
AssertionError: Should be absolute value of a number
