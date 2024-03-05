# swagger_client.MetasApi

All URIs are relative to *https://wem-qa.wnology.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**goalsDeleteAll**](MetasApi.md#goalsDeleteAll) | **DELETE** /exchange/api/v1/goals/plants/{plant_id} | Remover metas
[**goalsPut**](MetasApi.md#goalsPut) | **PUT** /exchange/api/v1/goals/plants/{plant_id} | Editar metas
[**goalsGet**](MetasApi.md#goalsGet) | **POST** /exchange/api/v2/appointments/targets | Buscar metas

# **goalsDeleteAll**
> object goalsDeleteAll(plant_id)

Remover metas

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.MetasApi(swagger_client.ApiClient(configuration))
plant_id = 'plant_id_example' # str | 

try:
    # Remover metas
    api_response = api_instance.goalsDeleteAll(plant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetasApi->goalsDeleteAll: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plant_id** | **str**|  | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **goalsPut**
> object goalsPut(plant_id, body=body)

Editar metas

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.MetasApi(swagger_client.ApiClient(configuration))
plant_id = 'plant_id_example' # str | 
body = NULL # object |  (optional)

try:
    # Editar metas
    api_response = api_instance.goalsPut(plant_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetasApi->goalsPut: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plant_id** | **str**|  | 
 **body** | [**object**](object.md)|  | [optional] 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **goalsGet**
> object goalsGet(body=body)

Buscar metas

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.MetasApi(swagger_client.ApiClient(configuration))
body = NULL # object |  (optional)

try:
    # Buscar metas
    api_response = api_instance.goalsGet(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetasApi->goalsGet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | [optional] 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

