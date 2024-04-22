from locust import HttpUser, task, constant
from pydantic import BaseModel

class CoverType(BaseModel):
    Elevation: int = 3225
    Aspect: int = 190
    Slope: int = 21
    Horizontal_Distance_To_Hydrology: int =67
    Vertical_Distance_To_Hydrology: int = 8
    Horizontal_Distance_To_Roadways: int =3267
    Hillshade_9am: int = 216
    Hillshade_Noon: int = 251
    Hillshade_3pm: int = 159
    Horizontal_Distance_To_Fire_Points: int =751
    Wilderness_Area: str = "Commanche"
    Soil_Type: str = "C7757"


class LoadTest(HttpUser):
    wait_time = constant(1)
    host = "http://inference_test:80"

    @task
    def predict(self):
        request_body = {
            "Elevation": 3225,
            "Aspect": 190,
            "Slope": 21,
            "Horizontal_Distance_To_Hydrology": 67,
            "Vertical_Distance_To_Hydrology": 8,
            "Horizontal_Distance_To_Roadways": 3267,
            "Hillshade_9am": 216,
            "Hillshade_Noon": 251,
            "Hillshade_3pm": 159,
            "Horizontal_Distance_To_Fire_Points": 751,
            "Wilderness_Area": "Commanche",
            "Soil_Type": "C7757",
            }
        headers = {
            "Content-Type": "application/json",
        }
        self.client.post(
            "/predict/", json=request_body, headers=headers
        )
