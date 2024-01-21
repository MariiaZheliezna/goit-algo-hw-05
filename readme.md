# Завдання 3.

## Висновки:

Виходячи зі здійсненої роботи, результати якої ми можемо побачити у таблицях нижче, алгоритм Боєра-Мура є найефективнішим у всіх випадках у порівнянні з алгоритмом Кнута-Морріса-Пратта та алгоритмом Рабіна-Карпа. 


Стаття:  ВИКОРИСТАННЯ АЛГОРИТМІВ У БІБЛІОТЕКАХ МОВ ПРОГРАМУВАННЯ

      Алгоритм       |              Строка пошуку               |  Час виконання, сек
---------------------|------------------------------------------|---------------------
 boyer_moore_search  | шуканого                                 | 0.0036436000373214483
     kmp_search      | шуканого                                 | 0.007849899935536087
 rabin_karp_search   | шуканого                                 | 0.01531839999370277
 boyer_moore_search  | відродження історичного спадку           | 0.002585100010037422
     kmp_search      | відродження історичного спадку           |  0.0146013000048697
 rabin_karp_search   | відродження історичного спадку           | 0.039839599980041385

Стаття:  Методи та структури даних для реалізації бази даних рекомендаційної системи соціальної мережі

      Алгоритм       |              Строка пошуку               |  Час виконання, сек
---------------------|------------------------------------------|---------------------
 boyer_moore_search  | порівняння часу                          | 0.004118100041523576
     kmp_search      | порівняння часу                          | 0.01283489994239062
 rabin_karp_search   | порівняння часу                          | 0.03385520004667342
 boyer_moore_search  | марс вийшов на постійний                 | 0.004181499942205846
     kmp_search      | марс вийшов на постійний                 | 0.023668100009672344
 rabin_karp_search   | марс вийшов на постійний                 | 0.051600400009192526