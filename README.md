# 1. Min Stack

Реализуйте стек, поддерживающий методы `push`, `pop`, `top` и `get_min`. Все операции должны выполняться за `O(1)`.

```python
stack.push(-2)
stack.push(0)
stack.push(-3)
stack.get_min() == -3
stack.pop()
stack.top() == 0
stack.get_min() == -2
```

Для желающих еще подобного из собеса

# 2. Design Underground System

Система метро фиксирует вход и выход пассажиров и считает среднее время поездки между станциями.

```python
check_in(passenger_id, station, time)
check_out(passenger_id, station, time)
get_average_time(start_station, end_station) -> float
```

Пассажир не может войти повторно до выхода. Выход без входа является ошибкой. Для неизвестного маршрута среднее получить нельзя.
