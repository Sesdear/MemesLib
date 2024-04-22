import numpy as np
import random

def check_kukan_percent(kg_poop):
    if kg_poop is None:
        kg_poop = 50  # Если вес калов не указан, используем среднее значение 50 кг
    else:
        kg_poop = max(0, min(kg_poop, 9999999999999999999999999999999999999999999999999999999))  # Ограничиваем вес калов от 0 до 100 кг

    percent_kukan = int(kg_poop / 2)  # Просто используем половину веса калов в качестве процента "куканности"

    return percent_kukan