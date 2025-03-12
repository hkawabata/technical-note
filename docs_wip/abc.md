---
title: abc
---

期待通りの挙動と違う

```python
from abc import ABC, abstractmethod

class MyAbstractClass(ABC):
	@abstractmethod
	def my_method(self, x):
		pass

class MyConcreteClass(MyAbstractClass):
	def my_method(self, x):
		return x * 2


conc = MyConcreteClass()
conc.func(100)
```
