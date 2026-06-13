import allure


@allure.epic("Blok 10 - Raportowanie")
@allure.feature("10.2: Meta-dane")
@allure.story("Priorytet krytyczny")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test logowania administratora")
@allure.description("Weryfikacja poprawnego logowania użytkownika administracyjnego.")
def test_admin_login():
    with allure.step("Wprowadzenie poprawnych danych logowania"):
        username = "admin"
        password = "admin123"

    with allure.step("Weryfikacja danych"):
        assert username == "admin"
        assert password == "admin123"


@allure.epic("Blok 10 - Raportowanie")
@allure.feature("10.2: Meta-dane")
@allure.story("Priorytet średni")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Test wyświetlania profilu użytkownika")
@allure.description("Sprawdzenie poprawności pobrania danych użytkownika.")
def test_user_profile():
    with allure.step("Pobranie danych użytkownika"):
        profile = {
            "id": 1,
            "name": "Kacper"
        }

    with allure.step("Walidacja danych"):
        assert profile["id"] == 1
        assert profile["name"] == "Kacper"