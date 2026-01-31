import pytest


@pytest.fixture(scope="class") #— фикстура уровня класса
def prepare_faces():
    print("^_^", "\n")
    yield
    print(":3", "\n")


@pytest.fixture() #обычная фикстура
def very_important_fixture():
    print(":)", "\n")


@pytest.fixture(autouse=True) #авто-фикстура (выполняется всегда)
def print_smiling_faces():
    print(":-Р", "\n")


class TestPrintSmilingFaces():
    def test_first_smiling_faces(self, prepare_faces, very_important_fixture):
        pass # pass = "пропустить, пройти мимо". Это заглушка, когда синтаксис требует какой-то код, но тебе не нужно ничего выполнять.

    def test_second_smiling_faces(self, prepare_faces):
        ... # ... (три точки)    То же что pass. Любая функция/метод в Python должен иметь хотя бы одну строку кода в теле.
 

#Что произошло для test_first_smiling_faces:

#1. ^_^        ← prepare_faces() ДО yield (scope="class" выполняется 1 раз на класс!)
#2. :-Р        ← print_smiling_faces() (autouse=True, выполняется ДО каждого теста)
#3. :)         ← very_important_fixture() ДО теста
#4. .:-Р       ← print_smiling_faces() (autouse=True, выполняется ПОСЛЕ каждого теста)
#5. .:3        ← prepare_faces() ПОСЛЕ yield (выполняется после ВСЕХ тестов класса!)
