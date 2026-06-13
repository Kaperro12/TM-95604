import allure


@allure.feature("10.1: Inicjalizacja Allure")
@allure.story("Pierwszy raport testowy")
def test_api_connection_passed():
    with allure.step("Krok 1: Symulacja połączenia z API"):
        status_code = 200

    with allure.step("Krok 2: Weryfikacja kodu odpowiedzi"):
        assert status_code == 200


@allure.feature("10.1: Inicjalizacja Allure")
@allure.story("Test kontrolny zakończony błędem")
def test_api_connection_failed():
    with allure.step("Krok 1: Symulacja błędnej odpowiedzi API"):
        status_code = 500

    with allure.step("Krok 2: Celowa asercja błędu do raportu"):
        assert status_code == 200