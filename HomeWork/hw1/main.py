# def parse(query: str) -> dict:
#     names_values_dict = {}
#     values = query.split('?')
#     if len(values) == 1:
#         return {}
#     for pair in values[1].split('&'):
#         if len(pair) == 0:
#             continue
#         else:
#             pair_key, pair_value = pair.split('=')
#             names_values_dict[pair_key] = pair_value
#     return names_values_dict
#
#
# if __name__ == '__main__':
#     assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
#     assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
#     assert parse('http://example.com/') == {}
#     assert parse('http://example.com/?') == {}
#     assert parse('http://example.com/?name=John') == {'name': 'John'}


def parse_cookie(query: str) -> dict:
    names_values_dict = {}
    values = query.split(';')
    if len(values) == 1:
        return {}
    for pair in values[1].split('='):
        if len(pair) == 0:
            continue
        else:
            pair_key, pair_value = pair.split(';', 1)
            names_values_dict[pair_key] = pair_value
    return names_values_dict

    # item = query.split(';')
    # if len(item) == 1:
    #     return {}
    # dict1 = []
    # keys = []
    # values = []
    # for i in item:
    #     dict1.extend(i.split('=', 1))
    # for i in dict1:
    #     if dict1.index(i) % 2 == 0:
    #         keys.append(i)
    #     else:
    #         values.append(i)
    # dictionary = {k: v for k, v in zip(keys, values)}
    # return dictionary


if __name__ == '__main__':
    assert parse_cookie('name=John;') == {'name': 'John'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=John;age=28;') == {'name': 'John', 'age': '28'}
    assert parse_cookie('name=John=User;age=28;') == {'name': 'John=User', 'age': '28'}
