import requests

class XPBoardsServices:
    __API_VERSION = 'v1'
    __BASE_URL = f'https://hom.web.xpboards.com.br/api/{__API_VERSION}'
    __DEFAULT_HEADERS = {'Accept': 'application/json', 'Content-Type': 'application/json' }


    def __init__(self, email, password):
       
        self.__token = self.__generate_token(email, password)

    def __handle_request_errors(self, errors):
        raise Exception(f'Got the following errors from api service: {repr(errors)}')

    def __handle_response(self, response):
        errors = response.get('errors', None)
        
        if errors:
            self.__handle_request_errors(errors=errors)

        data = response.get('data', None)
        
        if data == None:
            raise Exception(f'No "data" found in the response body')

        return data

    def __generate_token(self, email, password):

        url = f'{self.__BASE_URL}/login'
        headers = self.__DEFAULT_HEADERS
        body = {
            'email': email,
            'password': password
        }

        response = requests.post(
            url=url,
            headers=headers,
            json=body
        )

        data = self.__handle_response(response.json())
        token = data.get('token', None)

        if token != None:
            return token
        else:
            raise Exception(f'Expecting token, instead got {repr(data)}')

    def get_token(self):
        return self.__token

    def list_datasets(self):
        pass

    def list_datasets_items(self):
        pass

    def create_dataset(self):
        pass

    def update_dataset(self):
        pass

    def clear_dataset(self):
        pass