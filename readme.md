### hooked-on-django

Simple django application to trigger hooked methods.


#### startup

This hook will trigger after a django project is running.

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
            "path.to.method"
        ]
    }
}
```

Given this configuration the method `method` stored in the module `/path/to` will be executed after a delay of `10` seconds.
