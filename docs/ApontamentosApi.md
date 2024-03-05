# swagger_client.ApontamentosApi

All URIs are relative to *https://wem-qa.wnology.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**appointmentDelete**](ApontamentosApi.md#appointmentDelete) | **DELETE** /exchange/api/v2/appointment/{appointment_id} | Deletar apontamento
[**appointmentPatch**](ApontamentosApi.md#appointmentPatch) | **PATCH** /exchange/api/v2/appointment/{appointment_id} | Editar apontamento
[**appointmentPost**](ApontamentosApi.md#appointmentPost) | **POST** /exchange/api/v2/appointment | Criar apontamento
[**appointmentQuery**](ApontamentosApi.md#appointmentQuery) | **POST** /exchange/api/v2/appointment/query | Buscar apontamentos
[**exchange_api_v2_appointment_status_appointment_id_patch**](ApontamentosApi.md#exchange_api_v2_appointment_status_appointment_id_patch) | **PATCH** /exchange/api/v2/appointment/status/{appointment_id} | Aprovar apontamento

# **appointmentDelete**
> object appointmentDelete(appointment_id)

Deletar apontamento

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ApontamentosApi(swagger_client.ApiClient(configuration))
appointment_id = 'appointment_id_example' # str | 

try:
    # Deletar apontamento
    api_response = api_instance.appointmentDelete(appointment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApontamentosApi->appointmentDelete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appointment_id** | **str**|  | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **appointmentPatch**
> object appointmentPatch(appointment_id, body=body)

Editar apontamento

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ApontamentosApi(swagger_client.ApiClient(configuration))
appointment_id = 56 # int | 
body = NULL # object |  (optional)

try:
    # Editar apontamento
    api_response = api_instance.appointmentPatch(appointment_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApontamentosApi->appointmentPatch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appointment_id** | **int**|  | 
 **body** | [**object**](object.md)|  | [optional] 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **appointmentPost**
> object appointmentPost(body=body)

Criar apontamento

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ApontamentosApi(swagger_client.ApiClient(configuration))
body = NULL # object |  (optional)

try:
    # Criar apontamento
    api_response = api_instance.appointmentPost(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApontamentosApi->appointmentPost: %s\n" % e)
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

# **appointmentQuery**
> object appointmentQuery(body=body)

Buscar apontamentos

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ApontamentosApi(swagger_client.ApiClient(configuration))
body = NULL # object |  (optional)

try:
    # Buscar apontamentos
    api_response = api_instance.appointmentQuery(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApontamentosApi->appointmentQuery: %s\n" % e)
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

# **exchange_api_v2_appointment_status_appointment_id_patch**
> object exchange_api_v2_appointment_status_appointment_id_patch(appointment_id, body=body)

Aprovar apontamento

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ApontamentosApi(swagger_client.ApiClient(configuration))
appointment_id = 'appointment_id_example' # str | 
body = NULL # object |  (optional)

try:
    # Aprovar apontamento
    api_response = api_instance.exchange_api_v2_appointment_status_appointment_id_patch(appointment_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApontamentosApi->exchange_api_v2_appointment_status_appointment_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appointment_id** | **str**|  | 
 **body** | [**object**](object.md)|  | [optional] 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

