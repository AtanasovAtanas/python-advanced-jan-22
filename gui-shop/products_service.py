import json

PRODUCTS_PATH_FILE = './db/products.txt'


def get_all_products():
    with open(PRODUCTS_PATH_FILE, 'r') as file:
        return [json.loads(x.strip()) for x in file]


def buy_product(product_id):
    with open(PRODUCTS_PATH_FILE, 'r+') as products_file:
        result = []
        for product_line in products_file:
            current_product = json.loads(product_line.strip())
            if current_product['id'] == product_id:
                current_product['count'] -= 1
                result.append(json.dumps(current_product) + '\n')
            else:
                result.append(product_line)

        products_file.seek(0)
        products_file.truncate()

        products_file.writelines(result)
