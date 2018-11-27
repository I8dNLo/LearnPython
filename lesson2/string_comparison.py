def string_comparison(s1, s2):
    if not isinstance(s1, str) and isinstance(s2, str):
        return 0
    if s1 == s2:
        return 1
    elif len(s1) > len(s2) and s2 != 'learn':
        return 2
    elif s2 == 'learn':
        return 3
    else:
        return 'Что-то пошло не так'


print(string_comparison(3, 'string'))
print(string_comparison('string', 'string'))
print(string_comparison('string   ', 'string'))
print(string_comparison('string', 'learn'))
print(string_comparison('string123', '1221435string'))
