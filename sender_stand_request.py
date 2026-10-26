import configuration
import requests 
import data
def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)
response = get_docs()
print("статус_код_запроса_гет_на_получение_апи" , response.status_code) 
def get_logs():
    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH, params={"count":20})
response = get_logs()
print("статус_код_запроса_гет_логи" , response.status_code)
print("статус_код_запроса_гет_заголовки" , response.headers) 
def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)
response = get_users_table()
print("статус_код_запроса_гет_таблица" , response.status_code)

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)
response = post_new_user(data.user_body)
print("пост статус код создания нового пользователя", response.status_code)
print("пост тело ответа", response.json()) 


def post_products_kits(products_ids):
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH, json=products_ids)
response = post_products_kits(data.products_ids)
print("статус код запроса пост корзина", response.status_code)
print("тело ответа корзина", response.json()) 


