#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytils

# choose_plural нужен для выбора правильной формы
# существительного

# у choose_plural два параметра:
# 1) amount, количество
# 2) variants, варианты
# варианты - это кортеж из вариантов склонения
# его легко составить по мнемоническому правилу:
# (один, два, пять)
# т.е. для 1, 2 и 5 объектов, например для слова "пример"
# (пример, примера, примеров)
print pytils.numeral.choose_plural(21, (u"пример", u"примера", u"примеров"))
#-> пример
print pytils.numeral.choose_plural(12, (u"пример", u"примера", u"примеров"))
#-> примеров
print pytils.numeral.choose_plural(32, (u"пример", u"примера", u"примеров"))
#-> примера
