import os.path
from uuid import uuid1


class FileService:

    @staticmethod
    def upload_car_photo(instance, file: str) -> str:
        extension = file.split('.')[-1]
        return os.path.join('cars_photo', f'{uuid1()}.{extension}')
