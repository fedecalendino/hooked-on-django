### hooked-on-django

Simple django application to trigger hooked methods.


#### startup

This hook will trigger all indicated methods after django finished its startup.

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

Given that configuration, the method `method` from the module `/path/to` will be executed after a delay of `10` seconds.
