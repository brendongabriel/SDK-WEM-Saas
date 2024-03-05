# swagger_client.RelatrioApi

All URIs are relative to *https://wem-qa.wnology.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reportCardsGet**](RelatrioApi.md#reportCardsGet) | **GET** /exchange/api/v2/report/emissions/cards | Cards
[**reportChartsGet**](RelatrioApi.md#reportChartsGet) | **GET** /exchange/api/v2/report/emissions/chart | Chart

# **reportCardsGet**
> object reportCardsGet(start=start, end=end, plant_id=plant_id)

Cards

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RelatrioApi(swagger_client.ApiClient(configuration))
start = 56 # int |  (optional)
end = 56 # int |  (optional)
plant_id = 'plant_id_example' # str |  (optional)

try:
    # Cards
    api_response = api_instance.reportCardsGet(start=start, end=end, plant_id=plant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RelatrioApi->reportCardsGet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **int**|  | [optional] 
 **end** | **int**|  | [optional] 
 **plant_id** | **str**|  | [optional] 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reportChartsGet**
> object reportChartsGet(start=start, end=end, plant_id=plant_id)

Chart

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RelatrioApi(swagger_client.ApiClient(configuration))
start = 56 # int |  (optional)
end = 56 # int |  (optional)
plant_id = 'plant_id_example' # str |  (optional)

try:
    # Chart
    api_response = api_instance.reportChartsGet(start=start, end=end, plant_id=plant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RelatrioApi->reportChartsGet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **int**|  | [optional] 
 **end** | **int**|  | [optional] 
 **plant_id** | **str**|  | [optional] 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

