import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        headers = {'Authorization': f'OAuth {self.token}'}
        upload_url = self.get_upload_url(file_path, headers)
        self.upload_file(file_path, upload_url)

    def get_upload_url(self, file_path: str, headers: dict) -> str:
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        params = {'path': file_path, 'overwrite': 'false'}  # Здесь изменено значение параметра overwrite
        response = requests.get(upload_url, headers=headers, params=params)
        response.raise_for_status()
        upload_data = response.json()
        return upload_data['href']

    def upload_file(self, file_path: str, upload_url: str):
        with open(file_path, 'rb') as file:
            response = requests.put(upload_url, files={'file': file})
            response.raise_for_status()
            print('Файл успешно загружен на Яндекс.Диск')


if __name__ == '__main__':
    path_to_file = input('Введите путь до файла на компьютере: ')
    token = input('Введите OAuth-токен: ')
    uploader = YaUploader(token)
    uploader.upload(path_to_file)
