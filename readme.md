### hooked-on-django 

[![Version](https://img.shields.io/pypi/v/hooked--on--django?label=pypi&color=blue&logo=pypi)](https://pypi.org/project/hooked-on-django)


#### startup hook

This hook will trigger all indicated methods in `HOOKS` after django finished its startup.

`settings.py`

```python
INSTALLED_APPS = [
    ...,
    "hooks.startup",
    ...,
]

DJANGO_HOOKS = {
    "STARTUP": {
        "DELAY": 10,
        "HOOKS": [
            "path.to.method",
            "path.to.other",
        ]
    }
}
```

Given that configuration, the method `method` and the method `other` from the module `/path/to` are going to be executed after a delay of `10` seconds.


### to do

* Add kwargs for each hook

```
DJANGO_HOOKS = {
    "STARTUP": {
        "DELAY": 10,
        "HOOKS": [
            "path.to.method": {"param1": "value1"},
            "path.to.other": {"param2": 2},
            "path.to.another": {},
        ]
    }
}
```


