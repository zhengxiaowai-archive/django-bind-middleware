# django-request

![Python2.7](https://img.shields.io/badge/python-2.7-green.svg)
![LICENSE](https://img.shields.io/badge/LICENSE-MIT-blue.svg)

把 Json 请求的数据绑定到 request 中

支持 String、List、Object

## Installation

```pip install django-bind-middleware```

## Usage

添加到 settings 的 middleware 中

```python
DDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'startup.do.work.FindProductMarketFitMiddleware',
    ...
    'django_bind_middleware.middleware.BindRequestMiddleware'
)

```

在 settings 中设置 REQUIRE_REQUEST_DATA

```python

REQUIRE_REQUEST_DATA = ['name', 'address']

```

如果不存在绑定值为 None.

## LICENSE

MIT
