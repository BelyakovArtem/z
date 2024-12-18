#функция складывает два числа
def numbers_sum(a, b):
   return a + b
print(numbers_sum(1, 2))
#функция делает из заголавных букв строчные во всем введенном тексте
def str_low(inp_str):
    return inp_str.lower()
a = "HELLO, WORLD!"
b = str_low(a)
print(b)
#разворачивает список
def sorting_list(lt):
    return lt.reverse()
s = [1, 2, 3, 4, 5]
sorting_list(s)
print(s)
#добавляет элементы в словарь
def dict_upd(dictionary):
    return dictionary.update({"v": 3})
new = {"g": 1}
dict_upd(new)
print(new)
#пишет элементы в сете и кортежах вразнобой
def cunt(stturple):
    return len(stturple)
ag = {'h', 'a', 't', 'e'}
cunt(ag)
print(ag)





