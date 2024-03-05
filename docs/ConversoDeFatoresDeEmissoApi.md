# swagger_client.ConversoDeFatoresDeEmissoApi

All URIs are relative to *https://wem-qa.wnology.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**emissionsConversionFactorPatch**](ConversoDeFatoresDeEmissoApi.md#emissionsConversionFactorPatch) | **PATCH** /exchange/api/v1/emissions/conversion-factor | Editar fatores de emissão
[**emissionsConversionFactorDeleteAll**](ConversoDeFatoresDeEmissoApi.md#emissionsConversionFactorDeleteAll) | **DELETE** /exchange/api/v1/emissions/conversion-factor/plants/{plant_id} | Remover todos os fatores
[**emissionsConversionFactorGet**](ConversoDeFatoresDeEmissoApi.md#emissionsConversionFactorGet) | **GET** /exchange/api/v1/emissions/conversion-factor/plants/{plant_id} | Buscar fatores de emissão

# **emissionsConversionFactorPatch**
> object emissionsConversionFactorPatch(body=body)

Editar fatores de emissão

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ConversoDeFatoresDeEmissoApi(swagger_client.ApiClient(configuration))
body = NULL # object |  (optional)

try:
    # Editar fatores de emissão
    api_response = api_instance.emissionsConversionFactorPatch(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversoDeFatoresDeEmissoApi->emissionsConversionFactorPatch: %s\n" % e)
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

# **emissionsConversionFactorDeleteAll**
> object emissionsConversionFactorDeleteAll(plant_id)

Remover todos os fatores

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ConversoDeFatoresDeEmissoApi(swagger_client.ApiClient(configuration))
plant_id = 'plant_id_example' # str | 

try:
    # Remover todos os fatores
    api_response = api_instance.emissionsConversionFactorDeleteAll(plant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversoDeFatoresDeEmissoApi->emissionsConversionFactorDeleteAll: %s\n" % e)
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

# **emissionsConversionFactorGet**
> object emissionsConversionFactorGet(plant_id)

Buscar fatores de emissão

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ConversoDeFatoresDeEmissoApi(swagger_client.ApiClient(configuration))
plant_id = 'plant_id_example' # str | 

try:
    # Buscar fatores de emissão
    api_response = api_instance.emissionsConversionFactorGet(plant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversoDeFatoresDeEmissoApi->emissionsConversionFactorGet: %s\n" % e)
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

