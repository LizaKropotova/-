# TODO Напишите функцию для поиска индекса товара


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']


def search_index(list_, find_item):
    if find_item in list_:
        return list_.index(find_item)
    else:
        return None

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']
for find_item in ['банан', 'груша', 'персик']:
    index = search_index(items_list, find_item)
    if index is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")