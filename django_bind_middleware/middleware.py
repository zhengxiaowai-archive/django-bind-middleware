#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from django.conf import settings

class BindRequestMiddleware(object):
    def process_request(self, request):
        setattr(request, '_dont_enforce_csrf_checks', True)

    def process_view(slef, request, view_func, view_args, view_kwargs):
        try:
            require_datas = settings.REQUIRE_REQUEST_DATA 
        except:
            return None

        request_json = json.loads(request.body)

        for data in require_datas:
            setattr(request, data, request_json.get(data, None))
    
            




