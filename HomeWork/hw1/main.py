def parse(query: str) -> dict:
    item = query.split('?')
    if len(item) == 1:
        return {}
    item = item[1].split('&')
    if len(item) == 0:
        return {}
    dict1 = []
    keys = []
    values = []
    for i in item:
        dict1.extend(i.split('='))
    for i in dict1:
        if dict1.index(i) % 2 == 0:
            keys.append(i)
        else:
            values.append(i)
    dictionary = {k: v for k, v in zip(keys, values)}
    return dictionary


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=John') == {'name': 'John'}


def parse_cookie(query: str) -> dict:
    item = query.split(';')
    if len(item) == 1:
        return {}
    dict1 = []
    keys = []
    values = []
    for i in item:
        dict1.extend(i.split('=', 1))
    for i in dict1:
        if dict1.index(i) % 2 == 0:
            keys.append(i)
        else:
            values.append(i)
    dictionary = {k: v for k, v in zip(keys, values)}
    return dictionary


if __name__ == '__main__':
    assert parse_cookie('name=John;') == {'name': 'John'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=John;age=28;') == {'name': 'John', 'age': '28'}
    assert parse_cookie('name=John=User;age=28;') == {'name': 'John=User', 'age': '28'}
