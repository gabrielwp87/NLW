from typing import Dict


class TripFinder:
    def __init__(self, trips_repository) -> None:
        self.__trips_repository = trips_repository

    def find_trip_details(self, trip_id) -> Dict:
        try:
            trip = self.__trips_repository.find_trip_by_id(trip_id)
            if not trip:
                raise Exception("No Trip Found")

            return {
                "body": {
                    "trip": {
                        "id": trip[0],
                        "destination": trip[1],
                        "starts_at": trip[2],
                        "ends_at": trip[3],
                        "owner_name": trip[4],
                        "owner_email": trip[5]
                    }
                }
            }
        except Exception as exception:
            return {
                "body": {"erro": "Bad Request", "message": str(exception)},
                "status_code": 400
            }