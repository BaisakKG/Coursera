import operator

zen = """
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""
zen_map = dict()

for word in zen.split(): # колчество слов разделяемые пробелами
  cleaned_word = word.strip('.,!-').lower() # очищаем от знаков и переводим в нижний регистр
  if cleaned_word not in zen_map: # если слова нет в словаре то добавляем
    zen_map[cleaned_word] = 0 # с значением по умолчанию 0

  zen_map[cleaned_word] += 1 # если есть инкрементируем значение

# сортировка словаря по value
zen_items = zen_map.items() # возвращает пары (ключ, значение).
word_count_items = sorted(
  zen_items, key = operator.itemgetter(1), reverse=True
) # в качестве поля сортировки передаем второй элемент, это индекс 1 
# и делаем реверс чтобы получить самые популярные
print(word_count_items[:3])

# готовое решение для нахождение популярных слов
from collections import Counter

cleaned_list = []
for word in zen.split():
  cleaned_list.append(word.strip('.,-!').lower())

print(Counter(cleaned_list).most_common(4))
