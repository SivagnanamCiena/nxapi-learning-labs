#!/usr/bin/env python2.7

# Copyright 2015 Cisco Systems, Inc.
# 
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
# 
# http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
# an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.

''' HTTP API of Nexus (NX). 

    @author: Ken Jarrad (kjarrad@cisco.com)
'''

from __future__ import print_function as _print_function
from requests import post, get, request
from requests.auth import HTTPBasicAuth

from basics import odl_http
single_url_encode = odl_http.url_encode
double_url_encode = lambda val: single_url_encode(single_url_encode(val))
odl_http.url_encode = double_url_encode
from logging import log, INFO as LOG_LEVEL

def nexus_authentication_token(hostname='172.16.1.73', port=80, username='cisco', password='cisco'):
    """ Obtain authentication token from NX.
    """
    global _nexus_authentication_token
    if not '_nexus_authentication_token' in globals():
        url = "http://%s" % hostname
        log(LOG_LEVEL,'nexus authentication url: %s', url)
        try:
            response = get(
                url=url,
                auth=HTTPBasicAuth(username, password),
                verify=False)
            log(LOG_LEVEL, 'Nexus authentication status code: %s', response.status_code)
            expected_status_code = 200
            if response.status_code == expected_status_code:
#                 [[print(cookie.name, cookie.value, cookie.is_expired) for cookie in cookie_jar] for cookie_jar in response.cookies]
                try:
                    return response.cookies['nxapi_auth']
                except KeyError as ke:
                    raise Exception('Missing cookie.')
            else:
                msg = 'Expected HTTP status code %s, got %d' % (expected_status_code, response.status_code)
                if response.text:
                    raise ValueError(msg, response.text)
                else:
                    raise ValueError(msg)
        except Exception as e:
            raise ValueError('Unable to obtain Nexus authentication token.', url, e)
    return _nexus_authentication_token


# help(request)
auth_token=nexus_authentication_token()
print(auth_token)