## hooked-on-django 

[![Version](https://img.shields.io/pypi/v/hooked--on--django?label=pypi&color=blue&logo=pypi)](https://pypi.org/project/hooked-on-django)


### startup hook

All methods listed under this hook will be executed after Django finishes its startup process.


`settings.py`

```python
INSTALLED_APPS = [
    ...,
    "hooks.startup",
    ...,
]

DJANGO_HOOKS = {
    "STARTUP": {
        "path.to.method": {
            "delay": 0,
            "args" : [
                ...
            ],
            "kwargs": {
                ...
            },
        }
    }
}
```

##### examples

```
file: /path/to.py

def method(param1: str, param2: int):
    ...

def other(param1: str = "", param2: int = 0):
    ...

def another():
    ... 
```

To add a hook to each of these methods, the following configuration can be used:


```
DJANGO_HOOKS = {
    "STARTUP": {
        "path.to.method": {
            "delay": 10,
            "args": ["string", 123456]
        },
        "path.to.other": {
            "kwargs": {
                "param1": "string", 
                "param2": 123456
            }
        },
        "path.to.other": {},  # No params needed.
    }
}
```

note: additionaly, the method `method` will be executed after a 10 seconds delay.

🎣️
