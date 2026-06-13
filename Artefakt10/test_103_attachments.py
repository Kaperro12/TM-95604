import allure
import json


@allure.epic("Blok 10 - Raportowanie")
@allure.feature("10.3: Failure Screenshots")
@allure.story("Załączniki przy błędzie testu")
@allure.title("Test z automatycznym załącznikiem screenshotu i odpowiedzi API")
def test_failure_with_attachments():
    try:
        with allure.step("Krok 1: Symulacja odpowiedzi API"):
            api_response = {
                "status": 500,
                "message": "Internal Server Error",
                "endpoint": "/api/mobile/user/profile"
            }

            allure.attach(
                json.dumps(api_response, indent=4, ensure_ascii=False),
                name="API_Response",
                attachment_type=allure.attachment_type.JSON
            )

        with allure.step("Krok 2: Symulacja zrzutu ekranu błędu"):
            fake_png = (
                b"\x89PNG\r\n\x1a\n"
                b"\x00\x00\x00\rIHDR"
                b"\x00\x00\x00\x01\x00\x00\x00\x01"
                b"\x08\x02\x00\x00\x00"
            )

            allure.attach(
                fake_png,
                name="Screenshot_Error_01",
                attachment_type=allure.attachment_type.PNG
            )

        with allure.step("Krok 3: Celowe wymuszenie błędu testu"):
            assert api_response["status"] == 200

    except AssertionError:
        raise