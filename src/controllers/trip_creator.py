from typing import Dict
import uuid


class TripCreator:
    def __init__(self, trips_repository, emails_repository) -> None:
        self.__trips_repository = trips_repository
        self.__emails_repository = emails_repository

    def create(self, body) -> Dict:
        try:
            emails = body.get("emails_to_invite")

            trip_id = str(uuid.uuid4())
            trip_infos = {**body, "id": trip_id}
            # **body -> it will get everything from body and creating, look example.py at the ./

            self.__trips_repository.create_trip(trip_infos)

            if emails:
                for email in emails:
                    self.__emails_repository.registry_email({
                        "email": email,
                        "trip_id": trip_id,
                        "id": str(uuid.uuid4())
                    })

            return {
                "body": {"id": trip_id},
                "status_code": 201
            }
        except Exception as exception:
            return {
                "body": {"erro": "Bad Request", "message": str(exception)},
                "status_code": 400
            }
