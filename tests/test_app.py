from app import get_weather_data    

# test_app.py
def test_fetch_weather_data():
    # Testa att funktionen returnerar data för en stad (t.ex. "Stockholm")
    data = get_weather_data("Stockholm")
    assert data is not None, "Expected data to be returned, got None"


# Testa om funktionen returnerar korrekt format
def test_fetch_weather_data_format():
    data = get_weather_data("Stockholm")
    assert isinstance(data, dict), "Expected data to be a dictionary"


# Testa om funktionen innehåller specifika nycklar
def test_fetch_weather_data_keys():
    data = get_weather_data("Stockholm")
    expected_keys = ["temperature", "humidity", "description"]
    for key in expected_keys:
        assert key in data, f"Expected key '{key}' in data"


# Testa om funktionen hanterar felaktiga städer

def test_fetch_weather_data_invalid_city():
    data = get_weather_data("FakeCity")
    assert data is None, "Expected None for an invalid city name"
