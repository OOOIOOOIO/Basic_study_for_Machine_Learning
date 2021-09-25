#Weather fields in API response --> 딕셔너리 타입이라고 생각하면 편함
{
  "coord": {
    "lon": -122.08, # 경도
    "lat": 37.39 # 위도
  },
  "weather": [ #
    {
      "id": 800, #도시 아이디
      "main": "Clear",
      "description": "clear sky",
      "icon": "01d"
    }
  ],
  "base": "stations",
  "main": {
    "temp": 282.55,
    "feels_like": 281.86,
    "temp_min": 280.37,
    "temp_max": 284.26,
    "pressure": 1023,
    "humidity": 100
  },
  "visibility": 16093,
  "wind": {
    "speed": 1.5,
    "deg": 350
  },
  "clouds": {
    "all": 1
  },
  "dt": 1560350645, #
  "sys": {
    "type": 1,
    "id": 5122,
    "message": 0.0139,
    "country": "US",
    "sunrise": 1560343627, # 일출시간
    "sunset": 1560396563 # 일몰시간
  },
  "timezone": -25200,
  "id": 420006353,
  "name": "Mountain View",
  "cod": 200
  }
